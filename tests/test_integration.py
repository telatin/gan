"""Integration tests using real test files."""

import json
from pathlib import Path

import pytest

from gan_nomenclature.cli import main
from gan_nomenclature.io import read_root_table


# Path to test data
TEST_DIR = Path(__file__).parent.parent / "test"


@pytest.mark.integration
def test_read_real_test_files():
    """Test reading the actual test Excel files."""
    table1_path = TEST_DIR / "table1.xlsx"
    table2_path = TEST_DIR / "table2.xlsx"

    if not table1_path.exists() or not table2_path.exists():
        pytest.skip("Test Excel files not found")

    # Should not raise
    table1 = read_root_table(table1_path)
    table2 = read_root_table(table2_path)

    # Basic validation
    assert len(table1) > 0
    assert len(table2) > 0
    assert "Language" in table1.columns
    assert "Gender" in table1.columns


@pytest.mark.integration
def test_generate_with_real_test_files(tmp_path):
    """Test full generation pipeline with real test files."""
    table1_path = TEST_DIR / "table1.xlsx"
    table2_path = TEST_DIR / "table2.xlsx"

    if not table1_path.exists() or not table2_path.exists():
        pytest.skip("Test Excel files not found")

    output_dir = tmp_path / "output"

    result = main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-o", str(output_dir),
        "-p", "integration_test"
    ])

    assert result == 0

    # Verify outputs
    json_file = output_dir / "integration_test.json"
    html_file = output_dir / "integration_test.html"
    tex_file = output_dir / "integration_test.tex"

    assert json_file.exists()
    assert html_file.exists()
    assert tex_file.exists()

    # Verify JSON structure
    json_data = json.loads(json_file.read_text())
    assert isinstance(json_data, list)
    assert len(json_data) > 0


@pytest.mark.integration
def test_generate_with_three_real_files(tmp_path):
    """Test generation with all three test files."""
    table1_path = TEST_DIR / "table1.xlsx"
    table2_path = TEST_DIR / "table2.xlsx"
    table3_path = TEST_DIR / "table3.xlsx"

    if not all([table1_path.exists(), table2_path.exists(), table3_path.exists()]):
        pytest.skip("Test Excel files not found")

    output_dir = tmp_path / "output"

    result = main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-3", str(table3_path),
        "-o", str(output_dir),
    ])

    assert result == 0

    # Get the counts
    table1 = read_root_table(table1_path)
    table2 = read_root_table(table2_path)
    table3 = read_root_table(table3_path)

    expected_count = len(table1) * len(table2) * len(table3)

    json_file = output_dir / "gan.json"
    json_data = json.loads(json_file.read_text())

    assert len(json_data) == expected_count


@pytest.mark.integration
@pytest.mark.slow
def test_large_combination_generation(tmp_path):
    """Test that large combinations are handled correctly."""
    table1_path = TEST_DIR / "table1.xlsx"
    table2_path = TEST_DIR / "table2.xlsx"

    if not table1_path.exists() or not table2_path.exists():
        pytest.skip("Test Excel files not found")

    # Read to check size
    table1 = read_root_table(table1_path)
    table2 = read_root_table(table2_path)

    expected_combinations = len(table1) * len(table2)

    if expected_combinations < 10:
        pytest.skip("Test files too small for this test")

    output_dir = tmp_path / "output"

    result = main([
        "-1", str(table1_path),
        "-2", str(table2_path),
        "-o", str(output_dir),
        "-v"  # verbose mode
    ])

    assert result == 0

    json_file = output_dir / "gan.json"
    json_data = json.loads(json_file.read_text())

    assert len(json_data) == expected_combinations

    # Check that all entries are unique
    names = [list(entry.keys())[0] for entry in json_data]
    assert len(names) == len(set(names)), "Duplicate names generated"
