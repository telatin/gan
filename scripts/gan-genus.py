#!/usr/bin/env python3


import argparse
import itertools
import os, sys, json
from IPython import embed;

program = "GAN (Great Automatic Nomenclaturer)"
version = "0.2.1"


# Input File
#
#  - An excel file with three workbooks, each with columns:
#     - Root [key: unique]			REQUIRED
#     - Language           			REQUIRED
#     - Gender            			REQUIRED
#     - Definition (free text)		Optional
#     - Explanation (free text)	    Optional
#
# Release notes
#
# 0.2.0 	Initial print of etymology concatenating "Explanation"s
# 0.1.0  Initial release parsing an Excel file with three workbooks
# 			- Validating each workbook for column names and valid values
# 			- Create all combinations (triplet of Keys)
# 			- Convert each triplet to string (allows to inject rules
#

def eprint(*args, **kwargs):
    """print to STDERR"""
    print(*args, file=sys.stderr, **kwargs)


def read_list_from_xlsx_workbook(filename):
    """
	Extract a single workbook from an Excel file and validate it
	"""
    try:
        table = pd.read_excel(filename, sheet_name=0, header=0, index_col="Root")

    except Exception as e:
        eprint(
            f"FATAL ERROR:\nUnable to read file \"{filename}\":[page=0] (expecting column \"Root\").\n({e})")
        quit(1)

    try:
        with open(f"{opt.outdir}/tables.html", "a") as f:
            sheet = 1
            f.write(html_header + f"<h3>Workbook {sheet}</h3>\n")
            f.write(table.to_html())
    except Exception as e:
        eprint(f"WARNING: HTML not saved for workbook 1 of {filename}.\n{e}")

    # Check needed columns
    required_cols = ["Language", "Gender"]
    optional_cols = ["Part", "Definition", "Explanation"]

    for column in required_cols:
        if column not in table:
            eprint(f"INPUT FORMAT ERROR:\nRequired column \"{column}\" not found in the Excel file \"{filename}\".")
            exit()
    for column in optional_cols:
        if column not in table:
            eprint(
                f"WARNING: Suggested column \"{column}\" not found in the Excel file \"{filename}\".")

    # # Check values: Gender M/F/MF/N
    # if ((table["Gender"] != "M") & (table["Gender"] != "F") & (table["Gender"] != "MF") & (
    #         table["Gender"] != "N")).sum():
    #     eprint(f"ERROR: Workbook {workbook_index} contains invalid values for Gender (expected M, F, MF, N).")
    #     quit(1)
    #
    # # Check values: Language is L/G/NL
    # if ((table["Language"] != "L") & (table["Language"] != "G") & (table["Language"] != "NL")).sum():
    #     eprint(f"ERROR: Workbook {workbook_index} contains invalid values for Language (expected L, G, NL).")
    #     quit(1)

    return table


def lists_permutations(list_of_lists):
    """
    will receive a list of lists, and return all the possible combinations e.g.
    ('seleni', 'entero', 'plasma')
    """

    combinations = []
    iterables    = []
    for l in list_of_lists:
        iterables.append(l.index.tolist())
    #iterables = [list1.index.tolist(), list2.index.tolist(), list3.index.tolist()]

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

    if len(rootsList) == 3:
        return join_two_roots(word, rootsList[2]).capitalize()
    elif len(rootsList) == 2:
        return word.capitalize()


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

    etymology_html = ""
    hint = ""
    for index in range(len(triplet)):  # TODO - range using len?
        w = parts[index]
        key = triplet[index]
        for part in ("Language", "Gender", "Part", "Word",  "Definition"):

            if part == "Root":
                etymology_html += triplet[index]
            else:
                if part in ("Language", "Gender", "Part"):
                    etymology_html += "<span class=\"glossary\">" + w[part][key] + "</span>"
                elif part in ("Word"):
                    etymology_html += "<em>" + w[part][key] + "</em>,"
                else:
                    etymology_html += w[part][key]
                # add trailing space if not last part
                if part != "Definition":
                    etymology_html += "&nbsp;"
        etymology_html += "; "

    for index in reversed(range(len(triplet))):
        if "Explanation" in parts[index]:
            hint += parts[index]["Explanation"][triplet[index]]
        else:
            hint += parts[index]["Definition"][triplet[index]]
        if index > 0:
            hint += opt.connector
    #    hint = parts[2]["Explanation"][triplet[2]] + " of " + parts[1]["Explanation"][triplet[1]] + " of " + \
    #           parts[0]["Explanation"][triplet[0]]

    return (hint, etymology_html)


if __name__ == "__main__":
    opt_parser = argparse.ArgumentParser(description='Generate bacterial genera with Excel input')

    opt_parser.add_argument('-1', '--first',
                            help='First Excel file in "GAN" format',
                            required=True)

    opt_parser.add_argument('-2', '--second',
                            help='Second Excel file in "GAN" format',
                            required=True)

    opt_parser.add_argument('-3', '--third',
                            help='Third Excel file in "GAN" format')

    opt_parser.add_argument('-o', '--outdir',
                            help="Output directory",
                            required=True)
    opt_parser.add_argument('-c', '--connector',
                            help="String connecting the explanatory strings [default: of]",
                            default="of")
    opt_parser.add_argument('-v', '--verbose',
                            help='Increase output verbosity',
                            action='store_true')

    opt = opt_parser.parse_args()
    import pandas as pd
    html_header = (f"<html>\n"
                   f"    <head>\n"
                   f"    <meta charset=\"utf-8\" />\n"
                   f"	 <style><!--\n"
                   f"       * {{ font-family: Georgia, \"Times New Roman\", Times, serif;; }}\n"
                   f"       h3 {{ color:brown; font-style: italic; padding: 0px; margin: 0px; margin-bottom: 0.5em; margin-top: 1.6em;}}"
                   f"       .glossary {{ border-bottom: 1px dotted; }}"
                   f"       .def  {{ font-size: 1.1em; line-height: 220%; }}"
                   f"       #page {{ width: 80%; margin: 0 auto 0 auto; }}"
                   f"     --></style>\n"
                   f"    </head>\n"
                   f"	<body><div id=\"page\"><h1>GAN Genera</h1>")

    counter = 0
    html = ""
    suffixes = []
    prefixes = read_list_from_xlsx_workbook(opt.first)
    mids = read_list_from_xlsx_workbook(opt.second)

    if opt.third is not None:
        suffixes = read_list_from_xlsx_workbook(opt.third)
        permutations = lists_permutations([prefixes, mids, suffixes])
        for triplet in permutations:
            counter += 1
            eprint("#", counter, triplet)
            combinedWord = combine_roots(triplet)
            combinedEtym, fullEtym = combine_etymology(triplet, [prefixes, mids, suffixes])
            html += f"<p><h3>{combinedWord}</h3>\n<strong>Etymology:</strong> {fullEtym}<em>{combinedWord}</em>: {combinedEtym}.</p>\n\n"

        print(html_header + f"{counter} genera produced from:"
              f"<ul>"
              f"<li><em>First table</em>: {os.path.basename(opt.first)} ({len(prefixes.index)})</li>"
              f"<li><em>Second table</em>: {os.path.basename(opt.second)} ({len(mids.index)})</li>"
              f"<li><em>Third table</em>: {os.path.basename(opt.third)} ({len(suffixes.index)})</li>"
              f"</ul>.<hr>\n", html, "</body></html>")
    else:
        permutations = lists_permutations([prefixes, mids])
        for triplet in permutations:
            counter += 1
            eprint("#", counter, triplet)
            combinedWord = combine_roots(triplet)
            combinedEtym, fullEtym = combine_etymology(triplet, [prefixes, mids])
            html += f"<div><p><h3>{combinedWord}</h3>\n<strong>Etymology:</strong> {fullEtym}<em>{combinedWord}</em>: {combinedEtym}.</p></div>\n\n"

        print(html_header + f"{counter} genera produced from:"
                            f"<ul>"
                            f"<li><em>First table</em>: {os.path.basename(opt.first)} ({len(prefixes.index)})</li>"
                            f"<li><em>Second table</em>: {os.path.basename(opt.second)} ({len(mids.index)})</li>"
                            f"</ul>.<hr>\n", html, "</body></html>")
