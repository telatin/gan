"""Tests for the xls2tsv command line tool."""

from __future__ import annotations

import csv
from pathlib import Path

import pytest
from openpyxl import Workbook

from gan_nomenclature.xls2tsv import main, sanitize_sheet_name


def build_workbook(tmp_path: Path) -> Path:
    """Create a workbook with two worksheets for testing."""
    workbook = Workbook()
    first_sheet = workbook.active
    first_sheet.title = "My Sheet"
    first_sheet.append(["col1", "col2", "col3"])
    first_sheet.append(["a", "b", None])

    second_sheet = workbook.create_sheet(title="Summary 2024")
    second_sheet.append(["value"])
    second_sheet.append([42])

    path = tmp_path / "input.xlsx"
    workbook.save(path)
    return path


def read_tsv(path: Path) -> list[list[str]]:
    """Load a TSV file into memory for assertions."""
    with path.open(encoding="utf-8", newline="") as handle:
        return [row for row in csv.reader(handle, delimiter="\t")]


def test_xls2tsv_converts_each_sheet(tmp_path, capsys):
    """main() should create one TSV per worksheet and report stats."""
    input_path = build_workbook(tmp_path)
    output_dir = tmp_path / "tsv"

    exit_code = main(["-i", str(input_path), "-o", str(output_dir)])
    assert exit_code == 0

    first_sheet_path = output_dir / "My_Sheet.tsv"
    second_sheet_path = output_dir / "Summary_2024.tsv"

    assert first_sheet_path.exists()
    assert second_sheet_path.exists()

    first_rows = read_tsv(first_sheet_path)
    second_rows = read_tsv(second_sheet_path)

    assert first_rows == [["col1", "col2", "col3"], ["a", "b"]]
    assert second_rows == [["value"], ["42"]]

    captured = capsys.readouterr().out
    assert "Created" in captured
    assert "Processed 2 worksheet(s)" in captured


def test_xls2tsv_missing_input(tmp_path):
    """main() should terminate with an error when the input is missing."""
    missing_input = tmp_path / "missing.xlsx"
    output_dir = tmp_path / "tsv"

    with pytest.raises(SystemExit) as excinfo:
        main(["-i", str(missing_input), "-o", str(output_dir)])

    assert excinfo.value.code == 2


def test_xls2tsv_requires_destination(tmp_path):
    """Without --output or --stdout the CLI should abort."""
    input_path = build_workbook(tmp_path)
    with pytest.raises(SystemExit) as excinfo:
        main(["-i", str(input_path)])
    assert excinfo.value.code == 2


def test_xls2tsv_stdout_mode(tmp_path, capsys):
    """--stdout should print each worksheet to the terminal."""
    input_path = build_workbook(tmp_path)
    exit_code = main(["-i", str(input_path), "--stdout"])
    assert exit_code == 0

    output = capsys.readouterr().out
    assert "# Worksheet: My Sheet" in output
    assert "col1\tcol2\tcol3" in output
    assert "# End worksheet (2 rows, 3 columns)" in output
    assert "Processed 2 worksheet(s)" in output


def test_sanitize_sheet_name(tmp_path):
    """sanitize_sheet_name should produce readable filenames."""
    assert sanitize_sheet_name("Report Q1") == "Report_Q1"
    assert sanitize_sheet_name(" /tmp/ ") == "_tmp_"
    assert sanitize_sheet_name("") == "sheet"
