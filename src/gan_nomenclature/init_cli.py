"""CLI helper to scaffold GAN Excel workbooks."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable, List, Sequence

from openpyxl import Workbook

COLUMNS: Sequence[str] = (
    "Language",
    "Gender",
    "Part",
    "Word",
    "Root",
    "Definition",
    "Explanation",
)

EXAMPLE_ROWS: Sequence[dict[str, str]] = (
    {
        "Language": "L. (Latin)",
        "Gender": "masc.",
        "Part": "n. (noun)",
        "Word": "admissarius",
        "Root": "admissari",
        "Definition": "a stallion used for breeding",
        "Explanation": "horses",
    },
    {
        "Language": "Gr. (Greek)",
        "Gender": "masc.",
        "Part": "n.",
        "Word": "Balios",
        "Root": "Balio",
        "Definition": "a mythical horse",
        "Explanation": "horses",
    },
)

PRIMARY_FILENAME = "gan_roots_primary.xlsx"
SECONDARY_FILENAME = "gan_roots_secondary.xlsx"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate template Excel files compatible with gan-genus.",
    )
    parser.add_argument(
        "-o",
        "--outdir",
        default=".",
        help="Output directory where templates will be saved (default: current directory)",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Populate the templates with example rows",
    )
    return parser


def write_workbook(path: Path, rows: Iterable[dict[str, str]] | None) -> None:
    """Persist a workbook with the canonical GAN header and sample rows."""
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Roots"
    worksheet.append(list(COLUMNS))

    if rows:
        for row in rows:
            worksheet.append([row.get(column, "") for column in COLUMNS])

    workbook.save(path)


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows: Iterable[dict[str, str]] | None = EXAMPLE_ROWS if args.example else None

    primary_path = outdir / PRIMARY_FILENAME
    secondary_path = outdir / SECONDARY_FILENAME

    write_workbook(primary_path, rows)
    write_workbook(secondary_path, rows)

    print(f"Created {primary_path}")
    print(f"Created {secondary_path}")

    if args.example:
        print("Templates populated with example rows.")
    else:
        print("Templates contain headers only.")

    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
