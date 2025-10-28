# `gan-init` Command Reference

The `gan-init` command is a utility to create template Excel workbook files that are compatible with the `gan-genus` command.

## Synopsis

```bash
usage: gan-init [-h] [-o OUTDIR] [--example]
```

## Description

This script generates two Excel files, `gan_roots_primary.xlsx` and `gan_roots_secondary.xlsx`, which serve as starting points for creating lists of linguistic roots for name generation.

The generated files will contain the necessary headers for the `gan-genus` tool to correctly parse them. You can optionally populate these files with example rows to see the expected format.

The columns in the generated Excel files are:
- `Language`
- `Gender`
- `Part`
- `Word`
- `Root`
- `Definition`
- `Explanation`

## Options

*   `-h, --help`: Shows the help message and exits.
*   `-o, --outdir <directory>`: *Optional*. The directory where the template files will be saved. If not specified, they will be created in the current directory.
*   `--example`: *Optional*. If included, the generated Excel files will be populated with a few example rows of data.

## Examples

### Create empty templates

To create empty templates in a directory named `my_gan_inputs`:

```bash
mkdir -p my_gan_inputs
gan-init -o my_gan_inputs
```

This will create the following files with only a header row:
*   `my_gan_inputs/gan_roots_primary.xlsx`
*   `my_gan_inputs/gan_roots_secondary.xlsx`

### Create templates with example data

To create templates in the current directory and fill them with example data:

```bash
gan-init --example
```

This will create `gan_roots_primary.xlsx` and `gan_roots_secondary.xlsx` in the current folder, each containing sample data to guide you.
