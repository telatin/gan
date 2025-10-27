import json

import pandas as pd

from gan_nomenclature.generator import generate_entries, generate_outputs


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
