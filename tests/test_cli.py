"""Tests for CLI functionality."""

import json
from pathlib import Path

import pandas as pd
import pytest

from gan_nomenclature.cli import build_parser, main


@pytest.fixture
def sample_excel(tmp_path):
    """Create sample Excel files for testing."""
    table1_data = pd.DataFrame([
        {
            "Root": "lacto",
            "Language": "L.",
            "Gender": "masc.",
            "Part": "n.",
            "Word": "lac",
            "Definition": "milk",
            "Explanation": "milk",
        }
    ]).set_index("Root")

    table2_data = pd.DataFrame([
        {
            "Root": "cola",
            "Language": "N.L.",
            "Gender": "fem.",
            "Part": "n.",
            "Word": "cola",
            "Definition": "dweller",
            "Explanation": "dweller",
        }
    ]).set_index("Root")

    table1_path = tmp_path / "table1.xlsx"
    table2_path = tmp_path / "table2.xlsx"

    table1_data.to_excel(table1_path)
    table2_data.to_excel(table2_path)

    return table1_path, table2_path


def test_build_parser():
    """Test that argument parser is built correctly."""
    parser = build_parser()

    # Test that it has the expected arguments
    args = parser.parse_args([
        "-1", "file1.xlsx",
        "-2", "file2.xlsx",
        "-o", "output"
    ])

    assert args.first == "file1.xlsx"
    assert args.second == "file2.xlsx"
    assert args.outdir == "output"
    assert args.prefix == "gan"  # default
    assert args.connector == "of"  # default


def test_parser_with_third_file():
    """Test parser with optional third file."""
    parser = build_parser()

    args = parser.parse_args([
        "-1", "file1.xlsx",
        "-2", "file2.xlsx",
        "-3", "file3.xlsx",
        "-o", "output"
    ])

    assert args.third == "file3.xlsx"


def test_parser_custom_prefix_connector():
    """Test parser with custom prefix and connector."""
    parser = build_parser()

    args = parser.parse_args([
        "-1", "file1.xlsx",
        "-2", "file2.xlsx",
        "-o", "output",
        "-p", "myprefix",
        "-c", "from"
    ])

    assert args.prefix == "myprefix"
    assert args.connector == "from"


def test_parser_verbose_flag():
    """Test verbose flag."""
    parser = build_parser()

    args = parser.parse_args([
        "-1", "file1.xlsx",
        "-2", "file2.xlsx",
        "-o", "output",
        "-v"
    ])

    assert args.verbose is True


def test_parser_missing_required_args():
    """Test that parser fails with missing required arguments."""
    parser = build_parser()

    with pytest.raises(SystemExit):
        parser.parse_args(["-1", "file1.xlsx"])  # missing -2 and -o


def test_main_basic(sample_excel, tmp_path):
    """Test basic main function execution."""
    table1_path, table2_path = sample_excel
    output_dir = tmp_path / "output"

    result = main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-o", str(output_dir),
        "-p", "test"
    ])

    assert result == 0

    # Check output files exist
    assert (output_dir / "test.json").exists()
    assert (output_dir / "test.html").exists()
    assert (output_dir / "test.tex").exists()


def test_main_output_content(sample_excel, tmp_path):
    """Test that output files have expected content."""
    table1_path, table2_path = sample_excel
    output_dir = tmp_path / "output"

    main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-o", str(output_dir),
        "-p", "test"
    ])

    # Check JSON content
    json_path = output_dir / "test.json"
    json_data = json.loads(json_path.read_text())
    assert len(json_data) == 1
    assert "Lactocola" in json_data[0]

    # Check HTML content
    html_path = output_dir / "test.html"
    html_content = html_path.read_text()
    assert "Lactocola" in html_content
    assert "Etymology:" in html_content

    # Check LaTeX content
    tex_path = output_dir / "test.tex"
    tex_content = tex_path.read_text()
    assert "Lactocola" in tex_content
    assert r"\textbf{" in tex_content


def test_main_with_three_files(sample_excel, tmp_path):
    """Test main with three input files."""
    table1_path, table2_path = sample_excel

    # Create third table
    table3_data = pd.DataFrame([
        {
            "Root": "ensis",
            "Language": "L.",
            "Gender": "masc.",
            "Part": "adj.",
            "Word": "ensis",
            "Definition": "from a place",
            "Explanation": "place",
        }
    ]).set_index("Root")

    table3_path = tmp_path / "table3.xlsx"
    table3_data.to_excel(table3_path)

    output_dir = tmp_path / "output"

    result = main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-3", str(table3_path),
        "-o", str(output_dir),
    ])

    assert result == 0

    # Should generate 1 * 1 * 1 = 1 combination
    json_path = output_dir / "gan.json"
    json_data = json.loads(json_path.read_text())
    assert len(json_data) == 1


def test_main_custom_connector(sample_excel, tmp_path):
    """Test main with custom connector."""
    table1_path, table2_path = sample_excel
    output_dir = tmp_path / "output"

    main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-o", str(output_dir),
        "-c", "from"
    ])

    json_path = output_dir / "gan.json"
    json_data = json.loads(json_path.read_text())

    # Check that connector is used in etymology
    tokens = json_data[0]["Lactocola"]
    combined_token = [t for t in tokens if t[0] == "combined"][0]
    assert "from" in combined_token[1]


def test_main_creates_output_directory(sample_excel, tmp_path):
    """Test that main creates output directory if it doesn't exist."""
    table1_path, table2_path = sample_excel
    output_dir = tmp_path / "nonexistent" / "nested" / "output"

    assert not output_dir.exists()

    result = main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-o", str(output_dir),
    ])

    assert result == 0
    assert output_dir.exists()
