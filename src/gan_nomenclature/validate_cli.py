"""CLI tool to validate GAN-compatible Excel workbooks."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

import pandas as pd

from .io import OPTIONAL_COLUMNS, REQUIRED_COLUMNS

ALLOWED_VALUES = {
    "Language": {"L.", "Gr.", "N.L.", "M.E.", "M.L."},
    "Gender": {"masc.", "fem.", "neut.", "masc./fem."},
}


@dataclass
class ValidationResult:
    errors: List[str]
    warnings: List[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate that an Excel workbook contains GAN-compatible root tables.",
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Excel workbook to validate"
    )
    parser.add_argument(
        "-s",
        "--sheet",
        default=0,
        help="Worksheet index or name to validate (default: first sheet)",
    )
    parser.add_argument(
        "--print-pass",
        action="store_true",
        help="Report passing checks in addition to failures",
    )
    parser.add_argument(
        "--print-table",
        action="store_true",
        help="Print the parsed table to stdout after validation",
    )
    return parser


def load_table(path: Path, sheet: int | str) -> pd.DataFrame:
    try:
        table = pd.read_excel(path, sheet_name=sheet, header=0)
    except FileNotFoundError:  # pragma: no cover - simple passthrough
        raise
    except Exception as exc:  # pragma: no cover - bubbled up to CLI
        raise RuntimeError(f"Failed to read '{path}': {exc}") from exc

    if "Root" not in table.columns:
        raise ValueError("Expected column 'Root' to be present in the worksheet.")

    table = table.set_index("Root")
    return table


def validate_table(table: pd.DataFrame) -> ValidationResult:
    errors: List[str] = []
    warnings: List[str] = []

    for column in REQUIRED_COLUMNS:
        if column not in table.columns:
            errors.append(f"Missing required column '{column}'.")
        else:
            missing_mask = table[column].isna() | (
                table[column].astype(str).str.strip() == ""
            )
            for root in table.index[missing_mask]:
                errors.append(
                    f"Row '{root}' has empty value in required column '{column}'."
                )

    for column in OPTIONAL_COLUMNS:
        if column not in table.columns:
            warnings.append(f"Suggested column '{column}' not found.")

    for column, allowed in ALLOWED_VALUES.items():
        if column in table.columns:
            invalid_mask = (
                ~table[column].fillna("").astype(str).str.strip().isin(allowed | {""})
            )
            for value in sorted(table.loc[invalid_mask, column].dropna().unique()):
                errors.append(f"Column '{column}' contains invalid value '{value}'.")

    duplicate_roots = table.index[table.index.duplicated()].unique()
    for root in duplicate_roots:
        errors.append(f"Duplicate root '{root}' found (duplicate index).")

    return ValidationResult(errors=errors, warnings=warnings)


def format_messages(messages: Iterable[str]) -> str:
    return "\n".join(messages)


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    path = Path(args.input)
    try:
        table = load_table(path, args.sheet)
    except Exception as exc:
        sys.stderr.write(f"[FAIL] {exc}\n")
        return 1

    sys.stderr.write(f"[INFO] Validating {path} (sheet={args.sheet})\n")

    result = validate_table(table)

    if args.print_pass:
        for column in REQUIRED_COLUMNS:
            if column in table.columns:
                sys.stderr.write(f"[PASS] Required column present: '{column}'\n")
        for column in OPTIONAL_COLUMNS:
            if column in table.columns:
                sys.stderr.write(f"[PASS] Optional column present: '{column}'\n")

    if result.warnings:
        sys.stderr.write(
            format_messages(f"[WARN] {warning}" for warning in result.warnings) + "\n"
        )

    if result.errors:
        sys.stderr.write(
            format_messages(f"[FAIL] {error}" for error in result.errors) + "\n"
        )
        sys.stderr.write(
            f"[FAIL] Validation failed with {len(result.errors)} error(s).\n"
        )
        return 1

    sys.stderr.write("[PASS] Validation successful.\n")

    if args.print_table:
        print(table)

    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
