#!/usr/bin/env python3
import argparse
import sys
import pandas
from ganlib import *


def eprint(*args, **kwargs):
    """print to STDERR"""
    print(*args, file=sys.stderr, **kwargs)


if __name__ == "__main__":
    opt_parser = argparse.ArgumentParser(
        description="Generate bacterial genera with Excel input"
    )

    opt_parser.add_argument(
        "-i", "--input", help='Excel file in "autotaxonomer" format', required=True
    )

    opt_parser.add_argument(
        "-p",
        "--print-pass",
        action="store_true",
        help="Print passing steps, not only failing",
    )

    opt_parser.add_argument(
        "-t", "--print-table", action="store_true", help="Print table after checks"
    )

    opt = opt_parser.parse_args()

    eprint(f" [INFO] Validating: {opt.input}")
    errors = 0
    try:
        table = pandas.read_excel(opt.input, sheet_name=0, header=0, index_col="Root")
    except Exception as e:
        eprint(f" [FAIL] Unable to parse Excel file: {e}")
        exit(1)
    if opt.print_pass:
        eprint(" [PASS] Excel file is valid and indexed with column Root")

    for c in columns:
        if c in table:

            if opt.print_pass:
                eprint(f" [PASS] Found column: '{c}'")
            if c in validate:
                for item in table[c]:
                    if item not in validate[c]:
                        eprint(f" [FAIL] Column '{c}' contains invalid value '{item}' ")
                        errors += 1
                if opt.print_pass:
                    eprint(
                        f"        - Column '{c}' checked for correct values: {validate[c]}"
                    )
        else:
            eprint(f" [FAIL] Column {c} not found")
            errors += 1

    if errors:
        eprint(f" [FAIL] {errors} errors found.")
    else:
        eprint(" [PASS] all tests passed.")

    if opt.print_table:
        eprint(" [INFO] Table:")
        print(table)
