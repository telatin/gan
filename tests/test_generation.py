import json

import pandas as pd
import pytest

from gan_nomenclature.generator import combine_etymology, generate_entries, generate_outputs


PREFIX_ROWS = [
    {
        "Root": "lacto",
        "Language": "L.",
        "Gender": "masc.",
        "Part": "n.",
        "Word": "lac",
        "Definition": "milk",
        "Explanation": "milk",
    },
    {
        "Root": "aero",
        "Language": "Gr.",
        "Gender": "masc.",
        "Part": "n.",
        "Word": "aer",
        "Definition": "air",
        "Explanation": "air",
    },
]

MID_ROWS = [
    {
        "Root": "cola",
        "Language": "N.L.",
        "Gender": "fem.",
        "Part": "n.",
        "Word": "cola",
        "Definition": "dweller",
        "Explanation": "dweller",
    }
]

SUFFIX_ROWS = [
    {
        "Root": "ensis",
        "Language": "L.",
        "Gender": "masc.",
        "Part": "adj.",
        "Word": "ensis",
        "Definition": "from a place",
        "Explanation": "Example",
    }
]


def make_table(rows):
    return pd.DataFrame(rows).set_index("Root")


def test_generate_entries_three_tables():
    prefix = make_table(PREFIX_ROWS)
    mid = make_table(MID_ROWS)
    suffix = make_table(SUFFIX_ROWS)

    entries = generate_entries([prefix, mid, suffix], connector="of")

    assert len(entries) == 2
    assert entries[0].name == "Lactocolensis"
    assert entries[0].etymology_text == "milk of dweller of Example"
    assert ("combined", "milk of dweller of Example") in entries[0].tokens


def test_generate_outputs_rendering():
    prefix = make_table(PREFIX_ROWS)
    mid = make_table(MID_ROWS)
    suffix = make_table(SUFFIX_ROWS)

    result = generate_outputs(
        prefix,
        mid,
        suffix,
        connector="of",
        filenames=["table1.xlsx", "table2.xlsx", "table3.xlsx"],
    )

    assert "<h3>Lactocolensis</h3>" in result.html
    assert "\\textbf{Lactocolensis}" in result.latex

    payload = json.loads(result.to_json())
    assert payload[0]["Lactocolensis"][-1] == ["combined", "milk of dweller of Example"]


def test_generate_outputs_without_suffix():
    prefix = make_table(PREFIX_ROWS[:1])
    mid = make_table(MID_ROWS)

    result = generate_outputs(
        prefix,
        mid,
        connector="of",
        filenames=["table1.xlsx", "table2.xlsx", "(not provided)"],
    )

    assert "(not provided)" in result.html
    assert len(result.entries) == 1


# Additional etymology tests
def test_combine_etymology_basic():
    """Test basic etymology generation."""
    prefix = make_table(PREFIX_ROWS[:1])
    mid = make_table(MID_ROWS)

    hint, html, tokens = combine_etymology(
        ["lacto", "cola"],
        [prefix, mid],
        connector="of"
    )

    assert hint == "milk of dweller"
    assert "L." in html
    assert "masc." in html
    assert any(t[0] == "combined" for t in tokens)


def test_combine_etymology_custom_connector():
    """Test etymology with custom connector."""
    prefix = make_table(PREFIX_ROWS[:1])
    mid = make_table(MID_ROWS)

    hint, html, tokens = combine_etymology(
        ["lacto", "cola"],
        [prefix, mid],
        connector="from"
    )

    assert hint == "milk from dweller"


def test_combine_etymology_missing_explanation():
    """Test etymology when Explanation field is missing."""
    rows_no_expl = [
        {
            "Root": "test",
            "Language": "L.",
            "Gender": "masc.",
            "Part": "n.",
            "Word": "testum",
            "Definition": "a test",
        }
    ]
    table = make_table(rows_no_expl)

    hint, html, tokens = combine_etymology(
        ["test"],
        [table],
        connector="of"
    )

    # Should handle missing Explanation gracefully
    assert isinstance(hint, str)
    assert isinstance(html, str)


def test_generate_entries_count():
    """Test that correct number of entries are generated."""
    prefix = make_table(PREFIX_ROWS)  # 2 rows
    mid = make_table(MID_ROWS)        # 1 row
    suffix = make_table(SUFFIX_ROWS)  # 1 row

    entries = generate_entries([prefix, mid, suffix])

    # Should be 2 * 1 * 1 = 2 combinations
    assert len(entries) == 2
    assert all(hasattr(e, 'name') for e in entries)
    assert all(hasattr(e, 'etymology_text') for e in entries)


def test_generate_entries_two_tables():
    """Test generation with only two tables."""
    prefix = make_table(PREFIX_ROWS)
    mid = make_table(MID_ROWS)

    entries = generate_entries([prefix, mid])

    assert len(entries) == 2
    assert entries[0].name in ["Lactocola", "Aerocola"]


def test_generate_outputs_json_structure():
    """Test that JSON output has correct structure."""
    prefix = make_table(PREFIX_ROWS[:1])
    mid = make_table(MID_ROWS)

    result = generate_outputs(prefix, mid)
    json_str = result.to_json()
    data = json.loads(json_str)

    assert isinstance(data, list)
    assert len(data) == 1
    assert isinstance(data[0], dict)
    # Should have the name as key
    name = list(data[0].keys())[0]
    # Should have tokens as value
    tokens = data[0][name]
    assert isinstance(tokens, list)
    assert all(isinstance(t, list) and len(t) == 2 for t in tokens)


def test_generate_outputs_html_structure():
    """Test that HTML output has expected elements."""
    prefix = make_table(PREFIX_ROWS[:1])
    mid = make_table(MID_ROWS)

    result = generate_outputs(prefix, mid, filenames=["f1.xlsx", "f2.xlsx", ""])

    assert "<h3>" in result.html
    assert "Etymology:" in result.html
    assert "f1.xlsx" in result.html
    assert "f2.xlsx" in result.html


def test_generate_outputs_latex_structure():
    """Test that LaTeX output has expected elements."""
    prefix = make_table(PREFIX_ROWS[:1])
    mid = make_table(MID_ROWS)

    result = generate_outputs(prefix, mid)

    assert r"\textbf{" in result.latex
    assert r"\textit{" in result.latex
    assert r"\dashuline{" in result.latex
