"""Core generation logic for GAN nomenclature."""

from __future__ import annotations

import itertools
import json
import re
from dataclasses import dataclass
from importlib import resources
from string import Template
from typing import List, Optional, Sequence, Tuple

import pandas as pd

PROTECTED_SUFFIXES = (
    "bio",
    "geo",
    "neo",
    "mega",
    "micro",
    "allo",
    "amphi",
    "extra",
    "hetero",
    "iso",
    "iuxta",
    "meso",
    "peri",
    "quasi",
    "ultra",
)

VOWELS = set("aeiouAEIOU")


@dataclass(frozen=True)
class GeneratedName:
    """Representation of a generated bacterial name."""

    name: str
    triplet: Tuple[str, ...]
    etymology_text: str
    etymology_html: str
    tokens: List[Tuple[str, str]]


@dataclass
class GenerationResult:
    """Container for rendered outputs."""

    entries: List[GeneratedName]
    html: str
    latex: str
    json_data: List[dict]

    def to_json(self, **kwargs) -> str:
        """Return the JSON serialisation of the generated words."""

        kwargs.setdefault("indent", 4)
        kwargs.setdefault("sort_keys", True)
        return json.dumps(self.json_data, **kwargs)


def _is_vowel(letter: str) -> bool:
    if not letter:
        return False
    if len(letter) != 1:
        raise ValueError(f"Expected a single character, received {letter!r}.")
    return letter in VOWELS


def _strip_digits(value: str) -> str:
    return "".join(ch for ch in value if not ch.isdigit())


def join_two_roots(first: str, second: str) -> str:
    """Join two roots according to GAN rules."""

    first = _strip_digits(first)
    second = _strip_digits(second)

    if not first:
        return second
    if not second:
        return first

    if first.endswith(PROTECTED_SUFFIXES):
        return first + second

    if _is_vowel(first[-1]) and _is_vowel(second[0]):
        return first[:-1] + second

    return first + second


def combine_roots(roots: Sequence[str]) -> str:
    """Combine two or three roots into a single capitalised word."""

    if not roots:
        raise ValueError("No roots provided")

    iterator = iter(roots)
    word = next(iterator)
    for part in iterator:
        word = join_two_roots(word, part)

    return word.capitalize()


def _value_from_table(table: pd.DataFrame, column: str, key: str) -> Optional[str]:
    if column not in table.columns:
        return None
    value = table[column].get(key)
    if pd.isna(value):
        return None
    return str(value)


def combine_etymology(
    triplet: Sequence[str],
    tables: Sequence[pd.DataFrame],
    *,
    connector: str = "of",
) -> Tuple[str, str, List[Tuple[str, str]]]:
    """Combine metadata from all roots into textual representations."""

    etymology_html_parts: List[str] = []
    tokens: List[Tuple[str, str]] = []

    for index, key in enumerate(triplet):
        table = tables[index]
        for column in ("Language", "Gender", "Part", "Word", "Definition"):
            value = _value_from_table(table, column, key)
            if value is None:
                continue

            if column in {"Language", "Gender", "Part"}:
                etymology_html_parts.append(f'<span class="glossary">{value}</span>')
                tokens.append(("glossary", value))
            elif column == "Word":
                etymology_html_parts.append(f"<em>{value}</em>,")
                tokens.append(("italic", value))
                tokens.append(("separator", ","))
            else:
                etymology_html_parts.append(value)
                tokens.append(("plain", value))

            if column != "Definition":
                etymology_html_parts.append("&nbsp;")
                tokens.append(("separator", " "))

        etymology_html_parts.append("; ")
        tokens.append(("separator", "; "))

    explanations: List[str] = []
    for index, key in enumerate(triplet):
        explanation = _value_from_table(tables[index], "Explanation", key)
        if explanation:
            explanations.append(explanation)

    if explanations:
        hint = f" {connector} ".join(explanations)
    else:
        hint = ""

    hint = re.sub(rf"\s*{re.escape(connector)}\s*$", "", hint).strip()

    tokens.append(("combined", hint))

    return hint, "".join(etymology_html_parts), tokens


def generate_entries(
    tables: Sequence[pd.DataFrame],
    *,
    connector: str = "of",
) -> List[GeneratedName]:
    """Generate names for all combinations of the provided tables."""

    iterables = [table.index.tolist() for table in tables]
    entries: List[GeneratedName] = []

    for triplet in itertools.product(*iterables):
        word = combine_roots(triplet)
        hint, html, tokens = combine_etymology(triplet, tables, connector=connector)
        entries.append(
            GeneratedName(
                name=word,
                triplet=tuple(triplet),
                etymology_text=hint,
                etymology_html=html,
                tokens=tokens,
            )
        )

    return entries


def _load_template(filename: str) -> Template:
    package = "gan_nomenclature.templates"
    try:
        data = resources.files(package).joinpath(filename).read_text(encoding="utf-8")
    except (AttributeError, TypeError):
        # Fallback for older importlib.resources implementations (e.g. Python 3.9)
        data = resources.read_text(package, filename, encoding="utf-8")
    return Template(data)


def _build_html_list(entries: Sequence[GeneratedName]) -> str:
    blocks = []
    for entry in entries:
        blocks.append(
            "<div><p><h3>{name}</h3>\n"
            "<strong>Etymology:</strong> {etymology}<em>{name}</em>: {hint}.</p></div>\n\n".format(
                name=entry.name,
                etymology=entry.etymology_html,
                hint=entry.etymology_text,
            )
        )
    return "".join(blocks)


def _build_latex_list(entries: Sequence[GeneratedName]) -> str:
    parts: List[str] = []

    for entry in entries:
        row = [f"\\textbf{{{entry.name}}} --- "]
        for kind, value in entry.tokens:
            if kind == "italic":
                row.append(f"\\textit{{{value}}}")
            elif kind == "glossary":
                row.append(f"\\dashuline{{{value}}}")
            elif kind == "combined":
                if value:
                    row.append(f"\\textit{{{entry.name}}}: {value}. ")
            else:
                row.append(value)
        row.append("\n\n")
        parts.append("".join(row))

    latex_list = "".join(parts)
    latex_list = latex_list.replace("_", "\\_")
    latex_list = re.sub(
        r"existing\s+genus\s+(\w+)",
        r"existing genus \\textit{\1}",
        latex_list,
    )
    latex_list = re.sub(
        r"existing\s+species\s+(\w+\s+\w+)",
        r"existing genus \\textit{\1}",
        latex_list,
    )
    return latex_list


def generate_outputs(
    first: pd.DataFrame,
    second: pd.DataFrame,
    third: Optional[pd.DataFrame] = None,
    *,
    connector: str = "of",
    filenames: Optional[Sequence[str]] = None,
) -> GenerationResult:
    """Generate all outputs for the provided root tables."""

    tables: List[pd.DataFrame] = [first, second]
    if third is not None:
        tables.append(third)

    entries = generate_entries(tables, connector=connector)
    json_data = [{entry.name: entry.tokens} for entry in entries]

    html_template = _load_template("html.template")
    latex_template = _load_template("latex.template")

    filename1 = filenames[0] if filenames and len(filenames) > 0 else "first"
    filename2 = filenames[1] if filenames and len(filenames) > 1 else "second"
    if third is not None:
        filename3 = filenames[2] if filenames and len(filenames) > 2 else "third"
        count3 = len(third.index)
    else:
        filename3 = (
            filenames[2] if filenames and len(filenames) > 2 else "(not provided)"
        )
        count3 = 0

    html_output = html_template.safe_substitute(
        total=len(entries),
        filename1=filename1,
        filename2=filename2,
        filename3=filename3,
        count1=len(first.index),
        count2=len(second.index),
        count3=count3,
        list=_build_html_list(entries),
    )

    latex_output = latex_template.safe_substitute(
        count1=len(first.index),
        count2=len(second.index),
        count3=count3,
        filename1=filename1.replace("_", "{\\_}"),
        filename2=filename2.replace("_", "{\\_}"),
        filename3=filename3.replace("_", "{\\_}"),
        list=_build_latex_list(entries),
        roots="\\textit{Not implemented in the current version.}",
    )

    return GenerationResult(
        entries=entries, html=html_output, latex=latex_output, json_data=json_data
    )
