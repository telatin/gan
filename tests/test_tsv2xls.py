"""Tests for TSV to Excel conversion CLI."""

import pandas as pd

from gan_nomenclature.tsv2xls import convert, main


def test_convert_success(tmp_path):
    tsv_path = tmp_path / "roots.tsv"
    output_path = tmp_path / "roots.xlsx"
    tsv_path.write_text(
        "Root\tLanguage\tGender\tPart\tWord\tDefinition\tExplanation\n"
        "equus\tL.\tmasc.\tn.\tequus\thorse\thorses\n",
        encoding="utf-8",
    )

    result = convert(tsv_path, output_path, sheet_name="Roots")
    assert result.ok
    assert output_path.exists()

    frame = pd.read_excel(output_path, sheet_name="Roots", index_col="Root")
    assert "equus" in frame.index
    assert frame.loc["equus", "Language"] == "L."


def test_main_failure_missing_required(tmp_path):
    tsv_path = tmp_path / "bad.tsv"
    output_path = tmp_path / "bad.xlsx"
    tsv_path.write_text(
        "Root\tGender\n"
        "equus\tmasc.\n",
        encoding="utf-8",
    )

    exit_code = main(["-i", str(tsv_path), "-o", str(output_path)])
    assert exit_code == 1
    assert not output_path.exists()
