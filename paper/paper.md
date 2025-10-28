---
title: 'nomenclator: a Python package for the automated generation of Latin binomials for Bacterial and Archaeal genera'
tags:
  - Python
  - microbiology
  - taxonomy
  - nomenclature
  - bioinformatics
authors:
  - name: Andrea Telatin
    orcid: 0000-0001-7619-281X
    affiliation: 1
affiliations:
  - name: Quadram Institute Bioscience, Norwich, UK
    index: 1
date: 28 October 2025
bibliography: paper.bib
---

# Summary

`nomenclator` is a Python package that automates the creation of linguistically valid Latin binomials for bacterial and archaeal taxa, based on the "Great Automated Nomenclator" script [@Pallen2021].
Bacterial nomenclature requires Latin or Latinized names that conform to the rules of the International Code of Nomenclature of Prokaryotes (ICNP) and Latin grammar [@Parker2019, @Oren2019].
The tool generates taxonomic names by combinatorially concatenating roots from
Latin and Greek starting from two Excel files containing curated lists of 
roots to be combinatorially assembled into genus and species names.
`nomenclator` encapsulates the original script, and adds new features, such as an integration with LLMs
to draft an initial roots table staring from a text file used as context (e.g. a draft of a paper describing the biome where the new taxa were isolated).

# Statement of need

The increased rate of discovery of new microbial taxa driven by high-throughput sequencing technologies has created a bottleneck in the formal naming of new taxa, which requires the creation of valid Latin names that conform to the ICNP rules and Latin grammar.
The manual creation of such names is time-consuming and requires expertise in Latin, which is not commonly available among microbiologists.
`nomenclator` addresses this need by providing an automated tool that generates valid Latin names, thus facilitating the formal naming process and accelerating the description of new microbial taxa.

# Implementation and Features

## Installation

The package can be installed via `pip`:

```bash
pip install nomenclator
```

## Tools

`GAN` is implemented in pure Python (3.8+) with minimal dependencies.
The package exports these CLI tools:

- `gan-genus`: Generates genus names based on user-defined parameters (number of names, roots to use, etc.)
- `gan-init`: Initializes a project directory with necessary files and templates
- `gan-validate`: Validates the input Excel files for correct format and content
- `gan-aidraft`: Using OpenRouter API, generates draft etymologies given a text file used as context (e.g. draft of a paper describing the biome where the new taxa were isolated)
- `xls2tsv`: Converts Excel files with taxonomic data into TSV format for further processing


## Example input and output

An example of the input Excel file structure is shown below:

| Language | Gender | Part | Word        | Root      | Definition                           | Explanation |
|----------|--------|------|-------------|-----------|--------------------------------------|-------------|
| L.       | masc.  | n.   | admissarius | admissari | a stallion used for breeding         | horses      |
| Gr.      | masc.  | n.   | Arion       | ariono    | a mythical horse that could speak    | horses      |
| Gr.      | masc.  | n.   | Balios      | Balio     | a mythical horse                     | horses      |
| L.       | masc.  | n.   | caballus    | caballi   | a horse                              | horses      |

The programme's output can be saved as HTML or PDF files. An example is:

* **Admissaristercoricola** - Etymology: *L. masc. n. admissarius*, a stallion used for breeding; *L. neut. n. stercus*, excrement; *N.L. masc./fem. n. cola*, an inhabitant; `Admissaristercoricola`: a microbe of the faeces of horses.
* **Admissaristercoradaptatus** - Etymology: *L. masc. n. admissarius*, a stallion used for breeding; *L. neut. n. stercus*, excrement; *L. masc. n. adaptatus*, something adapted; `Admissaristercoradaptatus`: a microbe of the faeces of horses.
* **Admissaristercorihabitans** - Etymology: *L. masc. n. admissarius*, a stallion used for breeding; *L. neut. n. stercus*, excrement; *L. masc. n. habitans*, an inhabitant; `Admissaristercorihabitans`: a microbe of the faeces of horses.

# Acknowledgments

This software originated from research conducted with Mark J. Pallen and Aharon Oren, published in *Trends in Microbiology* [@Pallen2021] as *Great Automatic Nomenclator*, where it demonstrated the concept of large scale nomenclature generation for prokaryotic taxonomy. This paper describe the `nomenclator` package, which implements and extends the original script providing a Python package with CLI and additional features.

# Funding

The author gratefully acknowledge the support of the Biotechnology and Biological Sciences Research Council (BBSRC); this research was funded
by the BBSRC Core Capability Grant BB/CCG2260/1
and by the BBSRC Institute Strategic Programme Microbes and Food Safety 
BB/X011011/1 and its constituent project 
BBS/E/QU/230002C.

# References
