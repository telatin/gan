#!/usr/bin/env python3

import pandas as pd
import argparse
import itertools
import sys
from IPython import embed;

program = "GAN (Great Automatic Nomenclaturer)"
version = "0.2.1"

"""
 Input File

  - An excel file with three workbooks, each with columns:
     - Root [key: unique]			REQUIRED
     - Language [G,L,NL]			REQUIRED
     - Gender [M,F,MF,N]			REQUIRED
     - Definition (free text)		Optional
     - Basic_definition (free text)	Optional

 Release notes

 0.2.0 	Initial print of etymology concatenating "Basic_definition"s
 0.1.0  Initial release parsing an Excel file with three workbooks
 			- Validating each workbook for column names and valid values
 			- Create all combinations (triplet of Keys)
 			- Convert each triplet to string (allows to inject rules
 			)
"""


def eprint(*args, **kwargs):
    """print to STDERR"""
    print(*args, file=sys.stderr, **kwargs)


def read_list_from_xlsx_workbook(filename, workbook_index):
    """
	Extract a single workbook from an Excel file and validate it
	"""
    try:
        table = pd.read_excel(filename, sheet_name=workbook_index, header=0, index_col="Root")

    except Exception as e:
        eprint(
            f"FATAL ERROR:\nUnable to read file \"{filename}\":[page={workbook_index}] (expecting column \"Root\").\n({e})")
        quit(1)

    try:
        with open(f"{opt.outdir}/tables.html", "a") as f:
            sheet = workbook_index + 1
            f.write(html_header + f"<h3>Workbook {sheet}</h3>\n")
            f.write(table.to_html())
    except Exception as e:
        eprint(f"WARNING: HTML not saved for workbook {workbook_index} of {filename}.\n{e}")

    # Check needed columns
    required_cols = ["Language", "Gender"]
    optional_cols = ["Part", "Definition", "Basic_definition"]

    for column in required_cols:
        if column not in table:
            eprint(f"INPUT FORMAT ERROR:\nRequired column \"{column}\" not found in the workbook #{workbook_index} in "
                   f"the Excel file \"{filename}\".")
            exit()
    for column in optional_cols:
        if column not in table:
            eprint(
                f"WARNING: Suggested column \"{column}\" not found in the workbook #{workbook_index} in the Excel file \"{filename}\".")

    # Check values: Gender M/F/MF/N
    if ((table["Gender"] != "M") & (table["Gender"] != "F") & (table["Gender"] != "MF") & (
            table["Gender"] != "N")).sum():
        eprint(f"ERROR: Workbook {workbook_index} contains invalid values for Gender (expected M, F, MF, N).")
        quit(1)

    # Check values: Language is L/G/NL
    if ((table["Language"] != "L") & (table["Language"] != "G") & (table["Language"] != "NL")).sum():
        eprint(f"ERROR: Workbook {workbook_index} contains invalid values for Language (expected L, G, NL).")
        quit(1)

    return table


def read_all_lists_from_excel(filename):
    """
	Read from the Excel file the first three workbooks and return them
	"""
    lists = []
    for index in [0, 1, 2]:
        lists.append(read_list_from_xlsx_workbook(filename, index))
    return lists[0], lists[1], lists[2]


def lists_permutations(list1, list2, list3):
    """
	will receive a list of lists, and return all the possible combinations e.g.
	('seleni', 'entero', 'plasma')
	"""
    combinations = []
    iterables = [list1.index.tolist(), list2.index.tolist(), list3.index.tolist()]

    for triplet in itertools.product(*iterables):
        combinations.append(triplet)

    # TODO: To return full rows and not only indexes?
    return combinations


def is_vowel(letter):
    if len(letter) > 1:
        eprint(f"ERROR: Expecting a letter but received '{letter}'.")
        quit(2)

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    if letter in vowels:
        return True

    return False


def join_two_roots(m, n):
    """
    Function to join two words
    """
    protected_suffixes = ('bio', 'geo', 'neo', 'mega', 'micro')

    # If the first word ends with one of the suffixes tuple, join without changes
    if m is None:
        print(f"<{m}> <{n}>")
        pdb.set_trace()
    if m.endswith(protected_suffixes):
        return m + n

    # If the last letter of the first and first letter of the second word are vowels, remove last char of first word
    if is_vowel(m[-1]) and is_vowel(n[0]):
        return m[:-1] + n

    return m + n


def combine_roots(rootsList):
    """
    will receive a list of roots eg ('seleni', 'entero', 'plasma')
    and combine them as single string. This allows to implement rules
    """

    word = join_two_roots(rootsList[0], rootsList[1])
    if word is None:
        print(f"What {rootsList}: {word}")

    return join_two_roots(word, rootsList[2]).capitalize()

def partofspeechToString(string):
    """
    TODO
    """
    return string

def genderToString(string):
    """
    Return etymology friendly gender from M to "masc."
    """
    gender = {'M': "masc.", 'F': "fem.", 'N': "neutr.", "MF": "fem."}

    if string in gender:
        return gender[string]
    else:
        eprint(f"Error: gender {string} is not valid.")
        raise Exception("ganWrongGender")

def combine_etymology(triplet, parts):
    """
    Example:
        Admissaristercoricola;
        Etymology L.  masc  n. admissarius a stallion used for breeding; L.  neut.  n. stercus excrement; N.L. fem.  n. cola an inhabitant;
    prepare the etymology combining each root's info
    """

    etymology_html =""
    hint = ""
    for index in (0, 1, 2): # TODO - range using len?
        w = parts[index]
        key = triplet[index]
        for part in ("Language", "Gender", "Part", "Word", 0, "Definition"):

            if part == 0:
                etymology_html += triplet[index]
            else:
                etymology_html += w[part][key] + " "
        etymology_html += "; "

    for index in (2, 1, 0):

        hint += parts[index]["Basic_definition"][triplet[index]]
        if index > 0:
            hint += " of "
#    hint = parts[2]["Basic_definition"][triplet[2]] + " of " + parts[1]["Basic_definition"][triplet[1]] + " of " + \
#           parts[0]["Basic_definition"][triplet[0]]


    return (hint, etymology_html)


if __name__ == "__main__":
    opt_parser = argparse.ArgumentParser(description='Generate bacterial genera with Excel input')

    opt_parser.add_argument('-i', '--input',
                            help='Excel file in "autotaxonomer" format',
                            required=True)

    opt_parser.add_argument('-o', '--outdir',
                            help="Output directory")

    opt_parser.add_argument('-v', '--verbose',
                            help='Increase output verbosity',
                            action='store_true')

    opt = opt_parser.parse_args()

    html_header = (f"\n"
               f"    <head>\n"
               f"	 <style><!--\n"
               f"       * {{ font-family: Helvetica; }}\n"
               f"     --></style>\n"
               f"    </head>\n"
               f"	")

    counter = 0
    prefixes, mids, suffixes = read_all_lists_from_excel(opt.input)
    permutations = lists_permutations(prefixes, mids, suffixes)

    for triplet in permutations:
        counter += 1
        eprint("#", counter, triplet)
        combinedWord = combine_roots(triplet)
        combinedEtym, fullEtym = combine_etymology(triplet, [prefixes, mids, suffixes])
        print(f"{combinedWord}\n{fullEtym} {combinedEtym}\n")
