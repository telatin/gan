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

DEFAULT_MODEL = "openai/gpt-oss-120b:exacto"
QUALITY_KEYS = ("keep", "reason", "issues", "normalized_row")
QUALITY_TRUE_VALUES = {"true", "yes", "1", "ok", "keep", "pass"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate table entries for GAN using an OpenRouter-hosted LLM.",
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Input text file or '-' for stdin"
    )
    parser.add_argument("-o", "--output", required=True, help="Output TSV file path")
    parser.add_argument(
        "--api", dest="api_key", default=None, help="OpenRouter API key"
    )
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


def extract_json_from_response(content: str) -> Any:
    """Strip markdown fences and extract JSON from model response."""
    content = content.strip()

    # Remove markdown code fences if present
    if content.startswith("```"):
        lines = content.split("\n")
        # Remove opening fence (```json or ```)
        if lines[0].startswith("```"):
            lines = lines[1:]
        # Remove closing fence
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        content = "\n".join(lines).strip()

    # Try direct parse
    if content:
        return json.loads(content)

    raise json.JSONDecodeError("Empty response after cleaning", "", 0)


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
                raise RuntimeError(
                    "Unauthorized: invalid or missing OpenRouter API key."
                )
            response.raise_for_status()
            payload = response.json()
            content = payload["choices"][0]["message"]["content"].strip()
            try:
                return extract_json_from_response(content)
            except json.JSONDecodeError as exc:  # pragma: no cover - defensive path
                raise ValueError(
                    f"Model returned non-JSON content: {exc}\n"
                    f"Preview (first 500 chars): {content[:500]}\n"
                    f"Preview (last 300 chars): {content[-300:]}"
                ) from exc
        except (requests.RequestException, ValueError):
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff**attempt)
    raise RuntimeError(
        "Exhausted retries while calling OpenRouter."
    )  # pragma: no cover


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
        raise ValueError(
            f"Quality filter returned non-object JSON: {type(parsed).__name__}"
        )

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
                row, api_key, filter_model, max_retries=max_retries, timeout=timeout
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

            if not all(chosen.get(col, "").strip() for col in REQUIRED_COLS):
                dropped += 1
                missing = [
                    col for col in REQUIRED_COLS if not chosen.get(col, "").strip()
                ]
                emit(
                    f"[DROP] Row {idx}: {row.get('Word', '') or '(unnamed)'} — "
                    f"missing values for {', '.join(missing)}"
                )
                continue

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


def build_messages(context_text: str) -> List[Dict[str, str]]:
    """
    Prompt that asks the LLM to produce raw candidate rows.
    Greek script allowed in Word, but Root must be Latinized ASCII.
    """
    system = (
        "You are a meticulous classical philologist and lexicographer specializing in "
        "scientific nomenclature. You read context passages and propose compact lexicon "
        "tables of relevant Latin, Greek, and New Latin lexemes suitable for binomial nomenclature, "
        "including derivatives, technical terms, and mythological names that illuminate the text's topic."
    )
    user = f"""
CONTEXT:
{context_text}

TASK:
Return ONLY a JSON array (no preface, no code fences), where each element is an object with EXACTLY these keys:
{list(REQUIRED_COLS)}

**CRITICAL OUTPUT FORMAT:**
- Your response MUST start with [ and end with ]
- Do NOT wrap in ```json or ``` markdown code fences
- Do NOT include any explanatory text before or after the JSON
- Do NOT include comments
- Output ONLY valid JSON array

GUIDELINES:
- Language: 
  * 'L.' for Classical Latin
  * 'Gr.' for Classical Greek
  * 'N.L.' for New Latin (modern scientific coinages)
  * Other scholarly abbreviations as appropriate (e.g., 'Fr.', 'It.', 'Ar.')

- Gender: 
  * Use 'masc.', 'fem.', 'neut.' with trailing space for consistency
  * For mixed/variable gender: 'masc./fem.', 'fem./neut.', etc.
  * If unknown or not applicable, leave empty string

- Part:
  * Standard: 'n.' (noun), 'adj.' (adjective), 'v.' (verb), 'adv.' (adverb)
  * Specialized: 'adjectival noun', 'dim. n.' (diminutive), 'suffix', 'n.pl.' (noun plural)
  * If unknown, leave empty string

- Word:
  * The lemma in its original form
  * Greek lexemes SHOULD include Greek script (e.g., 'γᾰστήρ', 'θρίξ', 'κόπρος')
  * Latin lexemes in standard Latin orthography (e.g., 'stomachus', 'bacterium')
  * Use proper diacritics where appropriate

- Root:
  * **CRITICAL**: Must be ASCII-only Latinized form suitable for binomial construction
  * For Latin nouns: provide genitive stem (e.g., 'stomachi' from stomachus, 'denti' from dens)
  * For Greek: provide Latinized combining form (e.g., 'gastro' from γᾰστήρ, 'tricho' from θρίξ)
  * For compounds: use standard scientific combining form (e.g., 'copro', 'entero', 'dermato')
  * Remove all diacritics and Greek characters; must be valid ASCII

- Definition:
  * Concise English gloss including articles ('a', 'an', 'the')
  * Examples: 'the stomach', 'a tooth', 'an archaeon', 'dung', 'the skin'
  * Keep brief but complete (typically 2-6 words)

- Explanation:
  * A topical tag or hierarchical descriptor matching the context theme
  * Can be simple: 'a microbe', 'the mouth', 'faeces', 'the skin'
  * Can be hierarchical: 'Host-associated-Animals-System-Digestive-Oral'
  * Should reflect the main theme inferred from context

FOCUS:
- Analyze the context to identify the main theme (e.g., microbiology, anatomy, horses, etc.)
- Prioritize lexemes directly relevant to that theme
- Include 10–25 high-quality entries
- No duplicates; prefer well-attested classical forms
- For scientific contexts, include both technical terms and anatomical/descriptive roots
- Ensure Root column is always Latinized and ASCII-compatible for valid nomenclature

VALIDATION:
- Word can contain Greek script (γ, θ, ρ, etc.) for Greek lexemes
- Root MUST be ASCII-only (a-z, hyphens) and Latinized
- All fields properly formatted with consistent spacing
- Definitions include appropriate articles
"""

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def build_quality_messages(row: Dict[str, str]) -> List[Dict[str, str]]:
    """
    Craft prompt to validate and score a single lexicon row.
    Enforces that Root is Latinized ASCII while Word can be Greek script.
    """
    system = (
        "You are a classical philologist and nomenclature expert vetting lexicon entries "
        "for scientific binomial nomenclature. You ruthlessly reject entries with improper "
        "Latinization, modern English masquerading as Latin, or malformed roots unsuitable "
        "for taxonomic names."
    )
    row_json = json.dumps(
        row, ensure_ascii=False, indent=2
    )  # Changed to False to preserve Greek
    user = f"""
ENTRY:
{row_json}

TASK:
Return a JSON object with the following keys:
- keep (boolean): true only if the entry is well-formed and suitable for scientific nomenclature
- reason (string <= 160 characters): concise justification referencing any issues
- issues (array of short issue codes): empty if acceptable; use codes like ["not_latin", "bad_gender", "bad_root", "modern_english", "bad_language_tag", "root_not_latinized", "invalid_genitive", "missing_article"]
- normalized_row (object, optional): if minor fixes make the entry acceptable, provide corrected row

**CRITICAL OUTPUT FORMAT:**
- Your response MUST be valid JSON starting with {{ and ending with }}
- Do NOT wrap in ```json or ``` markdown code fences
- Do NOT include explanatory text before or after the JSON
- Output ONLY the JSON object

VALIDATION RULES:

1. **Language Field**:
   - Must be 'L.' (Latin), 'Gr.' (Greek), 'N.L.' (New Latin), or valid scholarly abbreviation
   - Must align with the Word lemma (Greek words need 'Gr.', Latin words need 'L.' or 'N.L.')

2. **Word Field**:
   - Latin words: standard Latin orthography (ASCII or common Latin extensions)
   - Greek words: SHOULD contain Greek script (γ, θ, κ, etc.) OR be Latinized
   - Accept either Greek script or Latinized forms in Word
   - Reject modern English words (e.g., 'insight', 'download')

3. **Root Field** (CRITICAL):
   - **MUST be ASCII-only**: no Greek script, no diacritics
   - **MUST be Latinized**: even for Greek words
   - For Latin nouns: proper genitive stem (e.g., 'stomachi', 'denti', 'cuti')
   - For Greek: proper Latinized combining form (e.g., 'gastro', 'tricho', 'dermato')
   - Check that stem is appropriate for binomial construction
   - Common issue: Greek root not Latinized (contains θ, ρ, etc.)

4. **Gender**:
   - If provided, must be 'masc.', 'fem.', 'neut.' or combinations
   - Should have trailing space for consistency (e.g., 'neut. ')
   - Must be plausible for the lemma
   - Empty string acceptable if unknown

5. **Part of Speech**:
   - Standard: 'n.', 'adj.', 'v.', 'adv.'
   - Specialized: 'adjectival noun', 'dim. n.', 'suffix', 'n.pl.'
   - Must be plausible for the lemma
   - Empty string acceptable if unknown

6. **Definition**:
   - Should include appropriate articles ('a', 'an', 'the')
   - Brief English gloss (2-10 words typically)
   - Should not be empty

7. **Explanation**:
   - Topical tag or hierarchical descriptor
   - Should not be empty or generic filler
   - Examples: 'a microbe', 'the mouth', 'faeces', 'Host-associated-Animals-System-Skin'

GATEKEEPING:
- Reject pop culture, slang, or informal modern terms
- Reject entries where Root contains non-ASCII characters
- Reject entries where Root is not properly Latinized
- Reject obvious modern English words presented as Latin
- Prefer classical or scholarly Neo-Latin vocabulary
- Accept minor formatting issues if normalized_row can fix them
- For Greek words with Greek script in Word, ensure Root is properly Latinized

DECISION:
- If acceptable (with or without normalization): set keep=true
- If minor fixes needed: set keep=true AND include normalized_row
- If fundamentally flawed: set keep=false with clear reason
"""
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
