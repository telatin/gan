# `gan-genus` Command Reference

The `gan-genus` command is a tool for generating novel bacterial genus names by combining linguistic roots from two or three separate input files.

## Synopsis

```bash
usage: gan-genus [-h] -1 FIRST -2 SECOND [-3 THIRD] -o OUTDIR [-p PREFIX] [-c CONNECTOR] [-v] [--version]
```

## Description

This script takes two or three Excel files as input, each containing word roots in the "GAN" format. It performs a combinatorial generation of new names and outputs them in multiple formats (JSON, HTML, and LaTeX) to a specified directory. This is useful for creating a large number of candidate names for new bacterial genera, complete with etymological explanations.

## Options

*   `-h, --help`: Shows the help message and exits.
*   `-1, --first <file>`: **Required**. Path to the first Excel file containing word roots.
*   `-2, --second <file>`: **Required**. Path to the second Excel file containing word roots.
*   `-3, --third <file>`: *Optional*. Path to a third Excel file for three-part name combinations.
*   `-o, --outdir <directory>`: **Required**. The directory where output files will be saved.
*   `-p, --prefix <basename>`: *Optional*. The base name for the output files (e.g., `my_run.json`, `my_run.html`). Defaults to `gan`.
*   `-c, --connector <string>`: *Optional*. The string used to connect the explanatory parts of the generated names. Defaults to `of`.
*   `-v, --verbose`: *Optional*. Increases the amount of information printed to the console during execution.
*   `--version`: Shows the program's version number and exits.

## Example

To generate names by combining `genera.xlsx` and `species.xlsx` and save them into a directory named `output_run1`:

```bash
gan-genus -1 input_real/Table1_genera.xlsx -2 input_real/Table1_species.xlsx -o output/run1
```

This will create the following files:
*   `output/run1/gan.json`
*   `output/run1/gan.html`
*   `output/run1/gan.tex`
