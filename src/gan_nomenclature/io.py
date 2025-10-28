"""Input helpers for GAN nomenclature."""

from __future__ import annotations

from pathlib import Path
from typing import Union
import warnings

import pandas as pd

PathLike = Union[str, Path]

REQUIRED_COLUMNS = ["Language", "Gender"]
OPTIONAL_COLUMNS = ["Part", "Definition", "Explanation"]


def _strip_series(series: pd.Series) -> pd.Series:
    return series.apply(
        lambda value: value.strip() if isinstance(value, str) else value
    )


def read_root_table(filename: PathLike) -> pd.DataFrame:
    """Read a root table from an Excel workbook.

    Parameters
    ----------
    filename:
        Path to an Excel workbook that contains a sheet with a ``Root`` column.

    Returns
    -------
    pandas.DataFrame
        Table indexed by the values in the ``Root`` column.

    Raises
    ------
    ValueError
        If one of the required columns is not available.
    """

    table = pd.read_excel(filename, sheet_name=0, header=0, index_col="Root")

    for column in REQUIRED_COLUMNS:
        if column not in table.columns:
            raise ValueError(
                f'Required column "{column}" not found in the Excel file "{filename}".'
            )
        table[column] = _strip_series(table[column])

    for column in OPTIONAL_COLUMNS:
        if column not in table.columns:
            warnings.warn(
                f'Suggested column "{column}" not found in the Excel file "{filename}".',
                stacklevel=2,
            )
        else:
            table[column] = _strip_series(table[column])

    return table
