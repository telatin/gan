# `gan-validate` Command Reference

The `gan-validate` command is a tool for validating that an Excel workbook contains GAN-compatible root tables.

## Synopsis

```bash
usage: gan-validate [-h] -i INPUT [-s SHEET] [--print-pass] [--print-table]
```

## Description

This script checks whether an Excel sheet contains valid root tables by inspecting its columns, values, and structure. This ensures that the file adheres to the standards required for use with other tools in the `gan-nomenclature` toolkit. The tool checks for required and optional columns, data integrity, and controlled vocabularies.

## Options

*   `-h, --help`: Shows the help message and exits.
*   `-i, --input <file>`: **Required**. Path to the Excel workbook to validate.
*   `-s, --sheet <name|index>`: *Optional*. The worksheet to validate, specified by name or by index. Defaults to the first sheet (index 0).
*   `--print-pass`: *Optional*. Report passing checks in addition to failures.
*   `--print-table`: *Optional*. Print the parsed table to standard output after successful validation.

## Validation Checks

The tool performs the following validation checks on the specified worksheet:

*   **Required Columns**: Verifies the presence of the required columns: `Root`, `Language`, and `Gender`.
*   **Suggested Columns**: Checks for the presence of suggested columns: `Part`, `Definition`, and `Explanation`, issuing a warning if they are absent.
*   **Data Integrity**:
    *   Ensures no empty values are present in any of the required columns.
    *   Checks for and flags any duplicate values in the `Root` column.
*   **Controlled Vocabularies**:
    *   For the `Language` column, verifies that all values are one of: `L.`, `Gr.`, `N.L.`, `M.E.`, `M.L.`.
    *   For the `Gender` column, verifies that all values are one of: `masc.`, `fem.`, `neut.`, `masc./fem.`.

## Example

To validate the first sheet in an Excel file named `my_roots.xlsx`:

```bash
gan-validate --input my_roots.xlsx
```

To validate a specific sheet named `Sheet2` and print the table if it passes:

```bash
gan-validate --input my_roots.xlsx --sheet Sheet2 --print-table
```
