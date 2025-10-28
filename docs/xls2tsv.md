# `xls2tsv` Command Reference

The `xls2tsv` command is a utility for converting each worksheet within an Excel workbook (`.xlsx`) into a separate Tab-Separated Values (TSV) file.

## Synopsis

```bash
usage: xls2tsv [-h] -i INPUT [-o OUTPUT] [-c]
```

## Description

This script reads an Excel workbook and iterates through each of its worksheets. For each worksheet, it creates a corresponding `.tsv` file, converting the cell data into a tab-delimited format. This is useful for converting spreadsheet data into a more accessible, plain-text format for scripting and data analysis.

Output files are named based on their corresponding worksheet titles, which are sanitized to be filesystem-friendly (e.g., spaces and special characters are replaced with underscores).

## Options

*   `-h, --help`: Shows the help message and exits.
*   `-i, --input <file>`: **Required**. The path to the input Excel workbook file.
*   `-o, --output <directory>`: The directory where the output TSV files will be saved. You must specify either this option or `--stdout`.
*   `-c, --stdout`: If specified, the TSV content will be printed directly to the standard output instead of being saved to files. Each worksheet's content will be preceded by a comment indicating its name.

## Examples

### Convert an Excel file to TSV files

Imagine you have an Excel file named `MyData.xlsx` with two worksheets: "Raw Data" and "Summary Sheet".

```bash
mkdir -p tsv_output
xls2tsv -i MyData.xlsx -o tsv_output
```

This command will produce the following files:
*   `tsv_output/Raw_Data.tsv`
*   `tsv_output/Summary_Sheet.tsv`

### Print worksheet content to the console

To view the TSV conversion of `MyData.xlsx` directly in your terminal:

```bash
xls2tsv -i MyData.xlsx -c
```

This will print the contents of "Raw Data" and then "Summary Sheet" to the console, separated by comments.
