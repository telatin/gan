# `tsv2xls` Command Reference

The `tsv2xls` command is a tool for converting a TSV root table into a validated Excel workbook.

## Synopsis

```bash
usage: tsv2xls [-h] -i INPUT [-o OUTPUT] [--sheet-name SHEET_NAME] [-f]
```

## Description

This script takes a single TSV file as input, validates its contents to ensure it conforms to the GAN (Generative Adversarial Nomenclature) format, and then converts it into an Excel workbook. The primary requirement for the input TSV is that it must contain a 'Root' column, which is used as the index.

## Options

*   `-h, --help`: Shows the help message and exits.
*   `-i, --input <file>`: **Required**. Path to the input TSV file (must include a 'Root' column).
*   `-o, --output <file>`: *Optional*. Destination Excel workbook path. Defaults to the input basename with an `.xlsx` extension.
*   `--sheet-name <name>`: *Optional*. The name of the worksheet to use in the Excel output. Defaults to `Roots`.
*   `-f, --force`: *Optional*. Overwrite the output file if it already exists.

## Example

To convert a TSV file named `my_roots.tsv` into an Excel file:

```bash
tsv2xls -i my_roots.tsv -o my_roots.xlsx
```

If `my_roots.xlsx` already exists, you would need to use the `--force` flag to overwrite it:

```bash
tsv2xls -i my_roots.tsv -o my_roots.xlsx --force
```
