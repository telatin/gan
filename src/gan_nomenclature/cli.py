"""Command line interface for GAN nomenclature."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List

from . import __version__
from .generator import generate_outputs
from .io import read_root_table


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate bacterial genera with Excel input.",
    )
    parser.add_argument("-1", "--first", required=True, help='First Excel file in "GAN" format')
    parser.add_argument("-2", "--second", required=True, help='Second Excel file in "GAN" format')
    parser.add_argument("-3", "--third", help='Third Excel file in "GAN" format')
    parser.add_argument("-o", "--outdir", required=True, help="Output directory")
    parser.add_argument("-p", "--prefix", default="gan", help="Output basename [default: 'gan']")
    parser.add_argument(
        "-c",
        "--connector",
        default="of",
        help="String connecting the explanatory strings [default: 'of']",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase output verbosity",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Show the program's version number and exit",
    )
    return parser


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    first_table = read_root_table(args.first)
    second_table = read_root_table(args.second)
    third_table = read_root_table(args.third) if args.third else None

    filenames = [Path(args.first).name, Path(args.second).name]
    if args.third:
        filenames.append(Path(args.third).name)
    else:
        filenames.append("(not provided)")

    result = generate_outputs(
        first_table,
        second_table,
        third_table,
        connector=args.connector,
        filenames=filenames,
    )

    base = args.prefix
    (outdir / f"{base}.json").write_text(result.to_json(), encoding="utf-8")
    (outdir / f"{base}.html").write_text(result.html, encoding="utf-8")
    (outdir / f"{base}.tex").write_text(result.latex, encoding="utf-8")

    if args.verbose:
        print(f"Generated {len(result.entries)} names.")

    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
