# Dev notes

## Dependencies

With Miniconda create an environment using the provided yaml file:
`conda env create -f environment.yaml`

Notable dependencies:
* Python 3.6+ (f-strings...)
* Pandas
* xlrd (from pip to read Excel files)

## Input format
Each set of roots is stored in an Excel file with these columns:
* Root [index column, must be unique]
* Word [original word]
* Language: ["L.", "Gr.", "N.L.", "M.E.", "M.L."]
* Gender: ["masc.", "fem.", "neut.", "masc./fem."]
* Part: ["n.", "adj.", "adv.", "gen.", "nom."]  

Language and Gender are strictly validated.

## Programs

### gan-validate.py

Will check an input Excel files for inconsistencies:
```
gan-validate.py [-t] -i input_file.xlsx
```

### gan-genus.py

Generate combinations of roots to produce genera.
Can be used to combine two or three (valid) Excel spreadsheets:
```
gan-genus.py -1 first_roots.xlsx -2 second.xlsx \
  [-3 third.xlsx] -o output_dir/
```

The output is an HTML file with a list of genera and their
etymology, as found in the individual entries in the Excel files.

## Further notes

### External resources
 - Open dictionary, Latin: [ArchimedesDigital/open_words](https://github.com/ArchimedesDigital/open_words)


### Alpha release 
#### Input file

All fields are case sensitive.

An excel file with three worksheets (names are not used, their order is):
 - Part1
 - Part2
 - Part3

Each of the tree has the following columns:
 - Language (can be: G, L or NL)	
 - Gender (can be: M, F, MF, N)
 - Word	
 - Root (index, unique)
 - Definition_full	
 - Definition_basic

We will consider column 4 [Word] to be the part of word to be composed. The provisional syntax supported is

 - singleword
 - wordvariant,secondvariant
 - wordprefix[optionalsuffix]		# this can be misleading and can be changed or removed
 - wordprefix[suffix1,suffix2]

#### Usage

```
python scripts/gan.py -i input/test_input.xlsx [ -o outdir/ ] > list.txt
```
