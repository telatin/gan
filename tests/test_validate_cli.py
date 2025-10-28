"""Tests for the gan-validate CLI helpers."""

import pandas as pd
import pytest

from gan_nomenclature.validate_cli import ValidationResult, validate_table


def make_table(**overrides):
    base = pd.DataFrame(
        [
            {
                "Root": "equus",
                "Language": "L.",
                "Gender": "masc.",
                "Part": "n.",
                "Word": "equus",
                "Definition": "horse",
                "Explanation": "horses",
            }
        ]
    ).set_index("Root")
    for key, value in overrides.items():
        base[key] = value
    return base


def test_validate_table_success():
    table = make_table()
    result = validate_table(table)
    assert isinstance(result, ValidationResult)
    assert result.ok
    assert result.errors == []


def test_validate_missing_required_column():
    table = make_table()
    table = table.drop(columns=["Language"])
    result = validate_table(table)
    assert not result.ok
    assert any("Missing required column 'Language'" in msg for msg in result.errors)


def test_validate_invalid_value():
    table = make_table(Language=["English"])
    result = validate_table(table)
    assert not result.ok
    assert any("invalid value 'English'" in msg for msg in result.errors)


def test_validate_duplicate_roots():
    table = pd.concat([make_table(), make_table()])
    result = validate_table(table)
    assert not result.ok
    assert any("Duplicate root" in msg for msg in result.errors)
