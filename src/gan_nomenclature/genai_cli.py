"""CLI to generate candidate GAN roots with support from an LLM."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set

import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

REQUIRED_COLS: Sequence[str] = (
    "Language",
    "Gender",
    "Part",
    "Word",
    "Root",
    "Definition",
    "Explanation",
)

DEFAULT_MODEL = "openai/gpt-4o-mini"
QUALITY_KEYS = ("keep", "reason", "issues", "normalized_row")
QUALITY_TRUE_VALUES = {"true", "yes", "1", "ok", "keep", "pass"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate table entries for GAN using an OpenRouter-hosted LLM.",
    )
    parser.add_argument("-i", "--input", required=True, help="Input text file or '-' for stdin")
    parser.add_argument("-o", "--output", required=True, help="Output TSV file path")
    parser.add_argument("--api", dest="api_key", default=None, help="OpenRouter API key")
    parser.add_argument(
        "-m",
        "--model",
        dest="model",
        default=None,
        help=f"Completion model identifier (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--quality-model",
        dest="quality_model",
        default=None,
        help="Optional model identifier used exclusively for quality filtering",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress information written to stderr",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="HTTP timeout for OpenRouter calls (seconds)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=4,
        help="Maximum retries for OpenRouter requests",
    )
    return parser


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def coerce_row(row: Dict[str, Any]) -> Dict[str, str]:
    """Ensure all required keys exist and are strings without tabs/newlines."""
    clean: Dict[str, str] = {}
    for key in REQUIRED_COLS:
        value = row.get(key, "")
        if value is None:
            value = ""
        clean[key] = str(value).replace("\t", " ").replace("\n", " ").strip()
    return clean


def ensure_table(data: Iterable[Any]) -> List[Dict[str, str]]:
    """Validate/normalize the JSON response into a list of dict rows."""
    if not isinstance(data, list):
        raise ValueError("Model returned non-list JSON. Expected an array of objects.")
    rows: List[Dict[str, str]] = []
    for item in data:
        if isinstance(item, dict):
            rows.append(coerce_row(item))
    deduped: List[Dict[str, str]] = []
    seen = set()
    for row in rows:
        key = tuple(row[col] for col in REQUIRED_COLS)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
    return deduped


def write_tsv(rows: Iterable[Dict[str, str]], path: str) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\t".join(REQUIRED_COLS) + "\n")
        for row in rows:
            handle.write("\t".join(row.get(col, "") for col in REQUIRED_COLS) + "\n")


def build_messages(context_text: str) -> List[Dict[str, str]]:
    """
    Prompt that asks the LLM to produce raw candidate rows.
    Greek transliterations must use ASCII and Latinized forms.
    """
    system = (
        "You are a meticulous classical philologist and lexicographer. "
        "You read a context passage and propose a compact lexicon table of "
        "relevant lexemes (Latin/Latinized Greek preferred when applicable), including mythic names "
        "and derivatives that illuminate the text's topic."
    )
    user = f"""
CONTEXT:
{context_text}

TASK:
Return ONLY a JSON array (no preface, no code fences), where each element is an object with EXACTLY these keys:
{list(REQUIRED_COLS)}

GUIDELINES:
- Language: use 'L.' for Latin, 'Gr.' for Greek, or a concise scholarly abbreviation (e.g., 'Fr.', 'It.', 'Ar.').
- Gender: masculine 'masc.', feminine 'fem.', neuter 'neut.'; for mixed write 'masc./fem.' etc.; if unknown, leave empty string.
- Part: e.g., 'n.' (noun), 'adj.', 'v.'; if unknown, leave empty string.
- Word: lemma (ASCII only; Greek lexemes MUST be Latinized, e.g., 'hippos' not 'ἵππος').
- Root: plausible stem/root (ASCII only; Latinize Greek stems, e.g., 'hipp-' not 'ἵππ-'); if unknown, provide a reasonable normalized stem or leave empty string.
- Definition: a short gloss (English).
- Explanation: a one- or two-word topical tag best matching the context (e.g., 'horses', 'metagenomics', 'microbiome').
- Focus on the main theme inferred from the context (e.g., if horses are central, prefer equine lexemes such as Latin 'equus', Greek 'hippos').
- Include 10–25 entries, no duplicates, high precision; prefer well-attested forms.
- If the context is not classical, still map to informative roots/loanwords that clarify the topic.
"""

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def unwrap_rows(
    payload: Any,
    *,
    _seen: Optional[Set[int]] = None,
) -> Optional[List[Any]]:
    """Best-effort extraction of the row list from a model response."""
    if isinstance(payload, list):
        return payload

    if not isinstance(payload, dict):
        return None

    if _seen is None:
        _seen = set()

    obj_id = id(payload)
    if obj_id in _seen:
        return None
    _seen.add(obj_id)

    if all(col in payload for col in REQUIRED_COLS):
        return [payload]

    candidate_keys = (
        "data",
        "rows",
        "table",
        "result",
        "items",
        "entries",
        "values",
        "records",
        "response",
        "output",
    )
    for key in candidate_keys:
        if key in payload:
            candidate = unwrap_rows(payload[key], _seen=_seen)
            if candidate is not None:
                return candidate

    for value in payload.values():
        candidate = unwrap_rows(value, _seen=_seen)
        if candidate is not None:
            return candidate

    return None


def request_openrouter(
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    *,
    max_retries: int = 4,
    timeout: int = 60,
) -> Any:
    """Issue a chat completion request and parse the JSON response content."""
    backoff = 1.5
    for attempt in range(max_retries):
        try:
            response = requests.post(
                OPENROUTER_URL,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                data=json.dumps(
                    {
                        "model": model,
                        "messages": messages,
                        "temperature": 0.2,
                        "max_tokens": 1200,
                        "response_format": {"type": "json_object"},
                    }
                ),
                timeout=timeout,
            )
            if response.status_code == 401:
                raise RuntimeError("Unauthorized: invalid or missing OpenRouter API key.")
            response.raise_for_status()
            payload = response.json()
            content = payload["choices"][0]["message"]["content"].strip()
            try:
                return json.loads(content)
            except json.JSONDecodeError as exc:  # pragma: no cover - defensive path
                raise ValueError(
                    f"Model returned non-JSON content: {exc}\n{content[:2000]}"
                ) from exc
        except (requests.RequestException, ValueError) as error:
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff**attempt)
    raise RuntimeError("Exhausted retries while calling OpenRouter.")  # pragma: no cover


def call_openrouter_rows(
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    *,
    max_retries: int = 4,
    timeout: int = 60,
) -> List[Any]:
    parsed = request_openrouter(
        api_key,
        model,
        messages,
        max_retries=max_retries,
        timeout=timeout,
    )
    rows_payload = unwrap_rows(parsed)
    if rows_payload is not None:
        return rows_payload
    raise ValueError(
        "Expected a JSON array or an object containing a list of rows, "
        f"but got keys: {sorted(parsed.keys()) if isinstance(parsed, dict) else type(parsed).__name__}"
    )


def build_quality_messages(row: Dict[str, str]) -> List[Dict[str, str]]:
    """Craft prompt to validate and score a single lexicon row."""
    system = (
        "You are a classical philologist vetting lexicon entries intended as Latin binomial roots. "
        "You ruthlessly reject entries that are modern English, malformed, or improperly Latinized."
    )
    row_json = json.dumps(row, ensure_ascii=True, indent=2)
    user = f"""
ENTRY:
{row_json}

TASK:
Return a JSON object with the following keys:
- keep (boolean): true only if the entry is a well-formed Latin or Latinized Greek component suitable for a binomial.
- reason (string <= 160 characters): concise justification referencing any issues.
- issues (array of short issue codes): empty if the entry is acceptable; use codes such as ["not_latin", "bad_gender", "bad_root", "modern_english", "bad_language_tag"].
- normalized_row (object, optional): if small fixes make the entry acceptable, supply the corrected row with the same keys as the original.

GATEKEEPING RULES:
- Reject modern English words presented as Latin (e.g., 'insight').
- Word/Root must be ASCII and Latin or Latinized Greek; no diacritics or Greek script.
- Language must align with the lemma (e.g., 'L.' for Latin, 'Gr.' for Latinized Greek terms).
- Gender and Part must be plausible for the lemma; leave empty if unknown.
- Definition and Explanation should be brief scholarly English.
- Prefer classical or scholarly Neo-Latin vocabulary. Reject pop culture or informal terms.
- If the entry is acceptable but can be trivially improved (e.g., adjust root ending), set keep=true and include normalized_row with corrections.
- If unacceptable, set keep=false.
"""
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def quality_filter_row(
    row: Dict[str, str],
    api_key: str,
    model: str,
    *,
    max_retries: int,
    timeout: int,
) -> Dict[str, Any]:
    """Evaluate a row and return the filter verdict."""
    parsed = request_openrouter(
        api_key,
        model,
        build_quality_messages(row),
        max_retries=max_retries,
        timeout=timeout,
    )

    if isinstance(parsed, list):
        if parsed and isinstance(parsed[0], dict):
            parsed = parsed[0]
        else:
            raise ValueError(f"Quality filter returned unexpected list: {parsed!r}")

    if not isinstance(parsed, dict):
        raise ValueError(f"Quality filter returned non-object JSON: {type(parsed).__name__}")

    result: Dict[str, Any] = {}
    for key in QUALITY_KEYS:
        if key in parsed:
            result[key] = parsed[key]

    if "keep" not in result:
        raise ValueError(f"Quality filter response missing 'keep': {parsed!r}")

    if "reason" not in result:
        result["reason"] = ""

    issues = result.get("issues", [])
    if not isinstance(issues, list):
        issues = [str(issues)]
    result["issues"] = issues

    normalized = result.get("normalized_row")
    if normalized is not None and not isinstance(normalized, dict):
        result.pop("normalized_row", None)

    keep_raw = result["keep"]
    if isinstance(keep_raw, str):
        keep = keep_raw.strip().lower() in QUALITY_TRUE_VALUES
    elif isinstance(keep_raw, (int, float)):
        keep = bool(keep_raw)
    else:
        keep = bool(keep_raw)
    result["keep"] = keep

    result["reason"] = str(result["reason"]).strip()
    return result


def run(
    api_key: str,
    model: str,
    quality_model: Optional[str],
    input_path: str,
    output_path: str,
    *,
    max_retries: int,
    timeout: int,
    log_enabled: bool,
) -> None:
    def emit(message: str) -> None:
        if log_enabled:
            sys.stderr.write(message.rstrip() + "\n")

    emit(f"Reading context from {input_path}...")
    context_text = read_text(input_path)
    if not context_text.strip():
        raise ValueError("Input text is empty.")

    emit(f"Requesting candidate rows from model '{model}'...")
    messages = build_messages(context_text)
    raw_rows = call_openrouter_rows(
        api_key,
        model,
        messages,
        max_retries=max_retries,
        timeout=timeout,
    )
    emit(f"Received {len(raw_rows)} raw row(s) from model response.")

    rows = ensure_table(raw_rows)
    emit(f"Normalized to {len(rows)} unique row(s) after coercion and de-duplication.")

    filtered_rows: List[Dict[str, str]] = []
    dropped = 0
    filter_model = quality_model or model
    for idx, row in enumerate(rows, start=1):
        try:
            verdict = quality_filter_row(
                row,
                api_key,
                filter_model,
                max_retries=max_retries,
                timeout=timeout,
            )
        except Exception as filter_error:
            emit(
                f"[WARN] Quality filter failed for row {idx} "
                f"'{row.get('Word', '') or '(unnamed)'}': {filter_error}; keeping entry."
            )
            filtered_rows.append(row)
            continue

        keep = verdict.get("keep", False)
        reason = verdict.get("reason") or ""
        issues = verdict.get("issues") or []
        if issues and not reason:
            reason = ", ".join(str(issue) for issue in issues)
        normalized_row = verdict.get("normalized_row")

        if keep:
            chosen = row
            if isinstance(normalized_row, dict) and normalized_row:
                chosen = coerce_row(normalized_row)
            filtered_rows.append(chosen)
            emit(
                f"[KEEP] Row {idx}: {chosen.get('Word', '') or '(unnamed)'} — "
                f"{reason or 'acceptable'}"
            )
        else:
            dropped += 1
            emit(
                f"[DROP] Row {idx}: {row.get('Word', '') or '(unnamed)'} — "
                f"{reason or 'rejected'}"
            )

    emit(f"Quality filter retained {len(filtered_rows)} row(s); dropped {dropped}.")

    if not filtered_rows:
        sys.stderr.write("WARNING: Model returned no rows; writing header only.\n")
    else:
        emit(f"Writing {len(filtered_rows)} row(s) to {output_path}...")

    write_tsv(filtered_rows, output_path)
    emit("Done.")


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    api_key = args.api_key or os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        parser.error("Provide --api or set $OPENROUTER_API_KEY.")

    model = args.model or os.environ.get("OPENROUTER_MODEL") or DEFAULT_MODEL
    quality_model = args.quality_model or os.environ.get("OPENROUTER_QUALITY_MODEL")

    log_enabled = not args.quiet

    try:
        run(
            api_key=api_key,
            model=model,
            quality_model=quality_model,
            input_path=args.input,
            output_path=args.output,
            max_retries=args.max_retries,
            timeout=args.timeout,
            log_enabled=log_enabled,
        )
        return 0
    except KeyboardInterrupt:  # pragma: no cover - user interrupt
        sys.stderr.write("Aborted by user.\n")
        return 130
    except Exception as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
