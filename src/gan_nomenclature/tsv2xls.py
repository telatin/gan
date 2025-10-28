"""CLI tool to convert TSV root tables into validated Excel workbooks."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Sequence

import pandas as pd

from .validate_cli import ValidationResult, validate_table


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a TSV root table into an Excel workbook after validation.",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path to the input TSV file (must include a 'Root' column).",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Destination Excel workbook path. Defaults to input basename with .xlsx extension.",
    )
    parser.add_argument(
        "--sheet-name",
        default="Roots",
        help="Worksheet name to use in the Excel output (default: Roots).",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    return parser


def read_tsv(path: Path) -> pd.DataFrame:
    try:
        frame = pd.read_csv(path, sep="\t", dtype=str).fillna("")
    except FileNotFoundError:
        raise
    except Exception as exc:  # pragma: no cover - reported by CLI
        raise RuntimeError(f"Failed to read TSV '{path}': {exc}") from exc

    if "Root" not in frame.columns:
        raise ValueError("Input TSV must contain a 'Root' column.")

    frame = frame.set_index("Root")
    return frame


def ensure_column_order(frame: pd.DataFrame) -> pd.DataFrame:
    """Reorder columns to keep canonical GAN layout when available."""
    canonical = [
        "Language",
        "Gender",
        "Part",
        "Word",
        "Root",
        "Definition",
        "Explanation",
    ]
    present = [col for col in canonical if col != "Root" and col in frame.columns]
    others = [col for col in frame.columns if col not in present]
    return frame.loc[:, present + others]


def convert(
    input_path: Path,
    output_path: Path,
    *,
    sheet_name: str,
) -> ValidationResult:
    table = read_tsv(input_path)
    validation = validate_table(table)
    if not validation.ok:
        raise ValueError("\n".join(validation.errors))

    ordered = ensure_column_order(table)
    ordered.to_excel(output_path, sheet_name=sheet_name)
    return validation


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    if not input_path.exists():
        parser.error(f"Input TSV '{input_path}' does not exist.")

    output_path = Path(args.output) if args.output else input_path.with_suffix(".xlsx")
    if output_path.exists() and not args.force:
        parser.error(
            f"Output file '{output_path}' already exists. Use --force to overwrite."
        )

    try:
        result = convert(
            input_path=input_path,
            output_path=output_path,
            sheet_name=args.sheet_name,
        )
    except Exception as exc:
        sys.stderr.write(f"[FAIL] {exc}\n")
        return 1

    if result.warnings:
        for warning in result.warnings:
            sys.stderr.write(f"[WARN] {warning}\n")

    sys.stderr.write(f"[PASS] Wrote validated workbook to '{output_path}'.\n")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
