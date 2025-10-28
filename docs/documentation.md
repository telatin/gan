# GAN 1.0

## Installation

_GAN_ is a Python script requiring Python (>3.6), IPython, itertools, 
pandas (>= 1.0), xlrd (>=1.2.0).

To install the required dependencies, an option is to use the Miniconda package manager (https://docs.conda.io/en/latest/miniconda.html), and create a new environment using the bundled `environment.yaml` file to create a new environment to be used to run the bundled scripts.

Commands:

```bash
pip install nomenclator
```

## Usage

The repository comes with two scripts:

* [gan-genus](gan-genus.md): generates bacterial genera from two or three Excel files in "GAN" format.
* [gan-init](gan-init.md): initializes a project directory with necessary files and templates.
* [xls2tsv](xls2tsv.md): converts Excel files with taxonomic data into TSV format for further processing.
* [gan-aidraft](gan-aidraft.md): Using OpenRouter API, generates draft etymologies given a text file used as context (e.g. draft of a paper describing the biome where the new taxa were isolated).


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