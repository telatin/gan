#!/usr/bin/env python3


import argparse
import itertools
import os, sys, json, re
from ganlib import *
from IPython import embed;

from string import Template


program = "GAN (Great Automatic Nomenclator)"
version = "0.6.1"


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
# 0.6.0  External templates
# 0.5.0  LaTeX support
# 0.4.0  HTML output
# 0.3.0  Etymology
# 0.2.0  Initial print of etymology concatenating "Explanation"s
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

    # Check needed columns
    required_cols = ["Language", "Gender"]
    optional_cols = ["Part", "Definition", "Explanation"]

    for column in required_cols:
        if column not in table:
            #table[column] = table["column"].str.replace(" ", "")
            eprint(f"INPUT FORMAT ERROR:\nRequired column \"{column}\" not found in the Excel file \"{filename}\".")
            eprint("Got:", table.columns)
            exit()
        else:
            table[column] = table[column].str.strip()
    for column in optional_cols:
        if column not in table:
            eprint(
                f"WARNING: Suggested column \"{column}\" not found in the Excel file \"{filename}\".")

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

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if letter.lower() in vowels:
        return True

    return False


def join_two_roots(m, n):
    """
    Function to join two words
    """

    m = ''.join([i for i in m if not i.isdigit()])
    n = ''.join([i for i in n if not i.isdigit()])

    protected_suffixes = ('bio', 'geo', 'neo', 'mega', 'micro', 'allo', 'amphi', 'extra', 'hetero', 'iso', 'iuxta', 'meso', 'neo', 'peri', 'quasi', 'ultra')
    #protected_suffixes = ('bio', 'geo', 'mega', ‘micro’, ‘allo’, ‘amphi’, ‘extra’, ‘hetero’, ‘iso’, ‘iuxta’, ‘meso’, ‘neo’, ‘peri’, ‘quasi’, ‘ultra’)

    # If the first word ends with one of the suffixes tuple, join without changes
    if m is None:
        print(f"Uncaught expection: <{m}> <{n}>")
        pdb.set_trace()
    if m.endswith(protected_suffixes):
        return m + n

    # If the last letter of the first and first letter of the second word are vowels, remove last char of first word
    if is_vowel(m[-1]) and is_vowel(n[0]):
        return m[:-1]  + n


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
        #raise Exception("ganWrongGender")
        return ""


def combine_etymology(triplet, parts):
    """
    Example:
        Admissaristercoricola;
        Etymology L.  masc  n. admissarius a stallion used for breeding; L.  neut.  n. stercus excrement; N.L. fem.  n. cola an inhabitant;
    prepare the etymology combining each root's info
    """

    etymology_html = ""
    etymology_raw = []
    hint = ""


    for index in range(len(triplet)):  # TODO - range using len?
        w = parts[index]
        key = triplet[index]
        for part in ("Language", "Gender", "Part", "Word",  "Definition"):

            if part == "Root":
                etymology_html += triplet[index]
                etymology_raw.append( ['root', triplet[index]] )
            else:
                if part in ("Language", "Gender", "Part"):
                    if not pd.isna(w[part][key]):
                        etymology_html += "<span class=\"glossary\">" + str(w[part][key]) + "</span>"
                        etymology_raw.append(['glossary',w[part][key] ])
                elif part in ("Word"):
                    etymology_html += "<em>" + w[part][key] + "</em>,"
                    etymology_raw.append(['italic', w[part][key]] )
                    etymology_raw.append( ['separator', ','])
                else:
                    etymology_html += w[part][key]
                    etymology_raw.append(['plain', w[part][key]])
                # add trailing space if not last part
                if part != "Definition":
                    etymology_html += "&nbsp;"
                    etymology_raw.append(['separator',' '])
        etymology_html += "; "
        etymology_raw.append(['separator', '; '])

    for index in reversed(range(len(triplet))):
        try:
            if "Explanation" in parts[index] and (not pd.isna(parts[index]["Explanation"][triplet[index]]) ):
                try:
                    hint += parts[index]["Explanation"][triplet[index]]
                except Exception as e:
                    eprint("WARNING: Error in column Explanation:\n" + parts[index]["Explanation"][triplet[index]], "\t", e)
                    quit(1)
        except Exception as e:
            eprint(f"ERROR:\n Exception {e}\n on index={index}, for word={triplet[index]}. Exit gracefully, for now...")
            quit(0)

            if index > 0:
                hint += " " + opt.connector + " "

    hint = re.sub(strip_ending, '', hint)

    etymology_raw.append( ['combined', hint] )
    return (hint, etymology_html, etymology_raw)


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

    opt_parser.add_argument('-p', '--prefix',
                            help="Output basename [default: 'gan']",
                            default="gan")
    opt_parser.add_argument('-c', '--connector',
                            help="String connecting the explanatory strings [default: 'of']",
                            default="of")
    opt_parser.add_argument('-v', '--verbose',
                            help='Increase output verbosity',
                            action='store_true')



    opt = opt_parser.parse_args()

    strip_ending = re.compile(rf"\s*{re.escape(opt.connector)}\s*$")

    eprint("          ----- G A N  -----        ")
    eprint("   the great automatic nomenclator  ")
    eprint("")

    import pandas as pd

    latex_template = slurp('latex.template')
    html_template  = slurp('html.template')
    latex = Template(latex_template)
    html = Template(html_template)
    html_list = ""
    latex_list = ""
    counter = 0

    suffixes = []
    prefixes = read_list_from_xlsx_workbook(opt.first)
    mids = read_list_from_xlsx_workbook(opt.second)
    eprint("Input files loaded")
    words_list = []
    third_if = "(not provided)"
    third_c  = 0


    if opt.third is not None:
        third_if = opt.third

        suffixes = read_list_from_xlsx_workbook(opt.third)
        third_c = str(len(suffixes.index))
        permutations = lists_permutations([prefixes, mids, suffixes])
        for triplet in permutations:
            counter += 1
            if  counter % int(len(permutations)/10) == 0:
                frac = int(10 * counter / int(len(permutations) / 10))
                eprint(f" - {frac}% combinations generated...")
            combinedWord = combine_roots(triplet)
            combinedEtym, fullEtym, rawEtym = combine_etymology(triplet, [prefixes, mids, suffixes])
            words_list.append({ combinedWord : rawEtym })
            if opt.verbose:
                eprint("#", counter, triplet)
            html_list += f"<p><h3>{combinedWord}</h3>\n<strong>Etymology:</strong> {fullEtym}<em>{combinedWord}</em>: {combinedEtym}.</p>\n\n"



    else:
        permutations = lists_permutations([prefixes, mids])
        for triplet in permutations:
            counter += 1
            if  counter % int(len(permutations)/10) == 0:
                frac = int(10 * counter / int(len(permutations)/10))
                eprint(f" - {frac}% combinations generated...")
            combinedWord = combine_roots(triplet)
            combinedEtym, fullEtym, rawEtym = combine_etymology(triplet, [prefixes, mids])
            words_list.append({ combinedWord : rawEtym })
            if opt.verbose:
                eprint("#", counter, triplet)
            html_list += f"<div><p><h3>{combinedWord}</h3>\n<strong>Etymology:</strong> {fullEtym}<em>{combinedWord}</em>: {combinedEtym}.</p></div>\n\n"



    eprint("\nSaving JSON: " + opt.outdir + "/" + opt.prefix + ".json")
    with open(opt.outdir + "/" + opt.prefix + ".json", "w")  as file:
        file.write(json.dumps(words_list, sort_keys=True, indent=4))



    eprint("Saving HTML:" + opt.outdir + "/" + opt.prefix + ".html")
    with open(opt.outdir + "/" + opt.prefix + ".html", "w", encoding="utf-8")  as file:
        file.write(html.safe_substitute(total=counter,
                        filename1=os.path.basename(opt.first),
                        filename2=os.path.basename(opt.second),
                        filename3=third_if,
                        count1=len(prefixes.index),
                        count2=len(mids.index),
                        count3=third_c,
                        list=html_list
                        )
        )


    for w in words_list:
        for key in w:
            #latex_list += "\subsection*{\\textit{" + key + "}}\n"
            latex_list  += "\\textbf{" + key + "} --- "
            for type, item in w[key]:
                if type == 'italic':
                    latex_list += "\\textit{" + item + "}"
                elif type == 'glossary':
                    latex_list += "\\dashuline{" + item + "}"
                    #latex_list += str(item)
                elif type == 'combined':
                    latex_list += "\\textit{" + key + "}" + ": " + item + ". "
                else:
                    latex_list += item

            latex_list += "\n\n"

    latex_out = opt.outdir + "/" + opt.prefix + ".tex"
    eprint("Saving LaTeX:" + latex_out)
    latex_list = re.sub(r'existing\s+genus\s+(\w+)', r'existing genus \\textit{\1}', latex_list.replace("_", r"\_"))
    latex_list = re.sub(r'existing\s+species\s+(\w+\s+\w+)', r'existing genus \\textit{\1}', latex_list.replace("_", r"\_"))

    with open(latex_out, "w", encoding="utf-8")  as file:
        file.write(latex.safe_substitute(
                        filename1=os.path.basename(opt.first).replace("_", r"{\_}"),
                         filename2=os.path.basename(opt.second).replace("_", r"{\_}"),
                         filename3=third_if.replace("_", r"{\_}"),
                         count1=len(prefixes.index),
                         count2=len(mids.index),
                         count3=third_c,
                         list=latex_list,
                         roots=r"\textit{Not implemented in the current version.}")
        )

