<img alt="seqfu logo" align="right" width="200" height="200" src="https://raw.githubusercontent.com/telatin/gan/master/docs/gan_logo.png">

# GAN: The Great Automatic Nomenclator
The Next Million Names for Archaea and Bacteria


## Principle

To generate a large number of new names, we apply a combinatorial approach starting with two or three sets of _curated roots_, that are processed to produce all their possible combinations while keeping trace of their grammatical metadata to draft a valid etymology.

![Gan flowchart](docs/gan_concept_wiki.png)

## Dependencies

The scripts in this repository require Python (at least 3.6) and these modules:
* itertools (ships with Python)
* pandas (>1.0)
* xlrd (1.2.0)

## Genera generator

A set of two (or three) Excel tables formatted as shown below is used to generate the list of combinations in JSON, HTML and LaTeX format.

![Excel input format](docs/input_table.png)

Synopsis:

```
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
                        Output basename
  -c CONNECTOR, --connector CONNECTOR
                        String connecting the explanatory strings [default: of]
  -v, --verbose         Increase output verbosity
 ```

## Etymology

"*The great automatic nomenclaturer*" is a reference to a short story ("_The Great Automatic Grammatizator_") 
written by the British author Roald Dahl [[link](https://en.wikipedia.org/wiki/The_Great_Automatic_Grammatizator)].

