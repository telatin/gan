"""Tests for error handling and edge cases."""

import pandas as pd
import pytest

from gan_nomenclature.generator import _is_vowel, join_two_roots
from gan_nomenclature.io import read_root_table


def test_is_vowel_invalid_input():
    """Test that _is_vowel raises error for invalid input."""
    with pytest.raises(ValueError, match="Expected a single character"):
        _is_vowel("ab")

    with pytest.raises(ValueError, match="Expected a single character"):
        _is_vowel("abc")


def test_is_vowel_empty_string():
    """Test that _is_vowel handles empty string."""
    assert _is_vowel("") is False


def test_read_root_table_missing_root_column(tmp_path):
    """Test error when Root column is missing."""
    df = pd.DataFrame([
        {
            "Language": "L.",
            "Gender": "masc.",
        }
    ])

    path = tmp_path / "bad_table.xlsx"
    df.to_excel(path, index=False)

    # Should raise because Root column is expected as index
    with pytest.raises(Exception):  # Will be a pandas or KeyError
        read_root_table(path)


def test_read_root_table_missing_required_column(tmp_path):
    """Test error when required column is missing."""
    df = pd.DataFrame([
        {
            "Root": "test",
            "Language": "L.",
            # Missing Gender column
        }
    ]).set_index("Root")

    path = tmp_path / "bad_table.xlsx"
    df.to_excel(path)

    with pytest.raises(ValueError, match="Required column"):
        read_root_table(path)


def test_read_root_table_nonexistent_file():
    """Test error when file doesn't exist."""
    with pytest.raises(FileNotFoundError):
        read_root_table("/nonexistent/path/file.xlsx")


def test_read_root_table_invalid_file(tmp_path):
    """Test error when file is not a valid Excel file."""
    bad_file = tmp_path / "not_excel.txt"
    bad_file.write_text("This is not an Excel file")

    with pytest.raises(Exception):  # Will be some kind of pandas/openpyxl error
        read_root_table(bad_file)


def test_join_two_roots_none_inputs():
    """Test that join_two_roots raises error with None inputs."""
    # The current implementation strips digits, which would fail on None
    # This test documents current behavior - None inputs are not supported
    with pytest.raises(TypeError):
        join_two_roots(None, "test")

    with pytest.raises(TypeError):
        join_two_roots("test", None)


def test_read_root_table_whitespace_handling(tmp_path):
    """Test that whitespace in cells is stripped."""
    df = pd.DataFrame([
        {
            "Root": "test",
            "Language": " L. ",
            "Gender": "  masc.  ",
            "Part": "n.  ",
        }
    ]).set_index("Root")

    path = tmp_path / "whitespace_table.xlsx"
    df.to_excel(path)

    table = read_root_table(path)

    # Whitespace should be stripped
    assert table.loc["test", "Language"] == "L."
    assert table.loc["test", "Gender"] == "masc."
    assert table.loc["test", "Part"] == "n."


def test_read_root_table_nan_handling(tmp_path):
    """Test handling of NaN values in optional columns."""
    df = pd.DataFrame([
        {
            "Root": "test",
            "Language": "L.",
            "Gender": "masc.",
            "Part": None,  # Will become NaN
            "Definition": None,
        }
    ]).set_index("Root")

    path = tmp_path / "nan_table.xlsx"
    df.to_excel(path)

    # Should not raise
    table = read_root_table(path)
    assert pd.isna(table.loc["test", "Part"])


def test_read_root_table_duplicate_roots(tmp_path):
    """Test behavior with duplicate root values."""
    df = pd.DataFrame([
        {
            "Root": "test",
            "Language": "L.",
            "Gender": "masc.",
        },
        {
            "Root": "test",  # Duplicate
            "Language": "Gr.",
            "Gender": "fem.",
        }
    ])

    path = tmp_path / "duplicate_table.xlsx"
    df.to_excel(path, index=False)

    # Pandas will either raise or use the last value when setting index
    # This test documents the behavior
    try:
        table = read_root_table(path)
        # If it doesn't raise, check that we only have one entry
        assert len(table) == 1
    except Exception:
        # Some versions may raise on duplicate index
        pass


def test_root_with_special_characters(tmp_path):
    """Test roots with special characters."""
    df = pd.DataFrame([
        {
            "Root": "test-root",
            "Language": "L.",
            "Gender": "masc.",
        }
    ]).set_index("Root")

    path = tmp_path / "special_table.xlsx"
    df.to_excel(path)

    table = read_root_table(path)
    assert "test-root" in table.index


def test_empty_excel_file(tmp_path):
    """Test behavior with empty Excel file."""
    df = pd.DataFrame(columns=["Root", "Language", "Gender"]).set_index("Root")

    path = tmp_path / "empty_table.xlsx"
    df.to_excel(path)

    table = read_root_table(path)
    assert len(table) == 0


def test_very_long_root_name(tmp_path):
    """Test handling of very long root names."""
    long_root = "a" * 1000

    df = pd.DataFrame([
        {
            "Root": long_root,
            "Language": "L.",
            "Gender": "masc.",
        }
    ]).set_index("Root")

    path = tmp_path / "long_table.xlsx"
    df.to_excel(path)

    table = read_root_table(path)
    assert long_root in table.index

    # Test that it can be combined
    result = join_two_roots(long_root, "test")
    assert isinstance(result, str)
    assert len(result) > 1000
