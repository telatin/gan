import pandas as pd
import pytest

from gan_nomenclature.io import read_root_table


def test_read_root_table_roundtrip(tmp_path):
    df = pd.DataFrame(
        [
            {
                "Root": "alpha",
                "Language": "L.",
                "Gender": "masc.",
                "Part": "n.",
                "Word": "alpha",
                "Definition": "first",
                "Explanation": "first",
            }
        ]
    ).set_index("Root")

    path = tmp_path / "table.xlsx"
    df.to_excel(path)

    table = read_root_table(path)

    assert list(table.index) == ["alpha"]
    assert table.loc["alpha", "Language"] == "L."


def test_read_root_table_missing_column(tmp_path):
    df = pd.DataFrame(
        [
            {
                "Root": "alpha",
                "Language": "L.",
            }
        ]
    ).set_index("Root")

    path = tmp_path / "table.xlsx"
    df.to_excel(path)

    with pytest.raises(ValueError):
        read_root_table(path)
