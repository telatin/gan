# GAN 1.0

## Installation

_GAN_ is a Python script requiring Python (>3.6), IPython, itertools, 
pandas (>= 1.0), xlrd (>=1.2.0).

To install the required dependencies, an option is to use the Miniconda package manager (https://docs.conda.io/en/latest/miniconda.html), and create a new environment using the bundled `environment.yaml` file to create a new environment to be used to run the bundled scripts.

Commands:

```bash
# Create the environment (run it once)
conda env create -f environment.yml

# Activate the environment to use the scripts
conda activate gan
```

## Usage

The repository comes with two scripts:
* gan-validate.py - to perform a check of the Excel input files
* gan-genus.py - to combine two or more Excel files

### gan-genus.py

```text
usage: gan-genus.py [-h] -1 FIRST -2 SECOND [-3 THIRD] -o OUTDIR [-p PREFIX] [-c CONNECTOR] [-v]

Generate bacterial genera with Excel input

optional arguments:
  -h, --help            show this help message and exit
  -1 FIRST, --first FIRST
                        First Excel file in "GAN" format
  -2 SECOND, --second SECOND
                        Second Excel file in "GAN" format
  -3 THIRD, --third THIRD
                        Third Excel file in "GAN" format
  -o OUTDIR, --outdir OUTDIR
                        Output directory
  -p PREFIX, --prefix PREFIX
                        Output basename [default: 'gan']
  -c CONNECTOR, --connector CONNECTOR
                        String connecting the explanatory strings [default: 'of']
  -v, --verbose         Increase output verbosity
```

The program requires two or three Excel tables, to be supplied with the `-1`, `-2` and `-3` arguments, respectively.

The program requires an output directory to be specified (via `-o`), and optionally an output "basename" prefix (via `-p`).

The repository comes with small test files to check that the program is working properly. From the base directory of the repository:
```bash
mkdir test_output
./scripts/gan-genus.py -1 ./test/table1.xlsx -2 ./test/table2.xlsx -o ./test_output
```

This will produce three files in the _test\_output_ directory:
* **gan.html** (HTML formatted text)
* **gan.json** (computer friendly output, in JSON format)
* **gan.tex** (LaTeX list, requiring an additional _config.tex_ from the _docs_ directory)

## Input

Each input file is an Excel file with at least one workbook (any other workbook is discarded). An empty template is provided in [input_test/template.xlsx](https://github.com/telatin/gan/blob/master/input_test/template.xlsx).


It should contain these columns (in any order):
* Language (L. for Latin, Gr. for Greek ...)
* Gender (masc., fem., neut. or masc./fem. or blank)
* Part (n. for noun, etc.)
* Word (the original word)
* Root (the root extracted from the word. This will be combined and must be unique in the file)
* Definition (definition of the word used to produce the etymology)
* Explanation (this is concatenated with a connector, for example _of_)

Small example:

| Language  | Gender | Part | Word | Root | Definition | Explanation  |
|:-----|:-------|:-----|-------------|-----------|-------------------------------|--------|
| L.   | masc.  | n.   | admissarius | admissari | a stallion used for breeding  | horses |
| Gr.  | masc.  | n.   | Balios      | Balio     | a mythical horse              | horses |
| L.   | masc.  | n.   | caballus    | caballi   | a horse                       | horses |


## Output

### JSON format

The JSON object is an array of elements, each element is a dictionary having as key the compound name (e.g. _ Admissaristercoradaptatus_) and as value an array of tuples in the form of (_type_, _value_), where type specifies how to render the value. Some examples:
 * `[ "glossary", "L." ]`
 * `[ "separator", " " ]`
 * `[ "italic", admissarius ]`

### HTML format

An HTML formatted list of compound words and their etymology.

Each item is provided as:

> **Admissaristercoricola** -- 
> Etymology: `L. masc. n.` _admissarius_, a stallion used for breeding; `L. neut. n.` _stercus_, excrement; `N.L. masc./fem. n.` _cola_, an inhabitant; _Admissaristercoricola_: a microbe of the faeces of horses.

* An example is available at [https://telatin.github.io/gan/example.html](https://telatin.github.io/gan/example.html)

### LaTeX format

A LaTeX source that can be compiled to produce a PDF document. It requires a `config.tex` file (supplied in the `docs/` directory) and can be used to produce the PDF with this command:

```bash
pdflatex gan.tex
```

To install a LaTeX package, on Ubuntu (requires ~5 Gb of space):
```bash
sudo apt install texlive-full
```

* An example is available at [https://telatin.github.io/gan/example.pdf](https://telatin.github.io/gan/example.pdf)