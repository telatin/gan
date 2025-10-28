#!/usr/bin/env python3

import os

programdir = os.path.dirname(os.path.realpath(__file__))
version = "0.1.0"
columns = ["Language", "Gender", "Part", "Word", "Definition", "Explanation"]

validate = {
    "Language": ["L.", "Gr.", "N.L.", "M.E.", "M.L."],
    "Gender": ["masc.", "fem.", "neut.", "masc./fem."],  # ,
    # "Part": ["n.", "adj.", "adv.", "gen.", "nom."]   #?
}


def slurp(filename):
    with open(programdir + "/" + filename, "r") as file:
        return file.read()


# abl.
# ablative
# adj.
# adjective
# adv.
# adverb
# Chem.
# Chemical term
# comp.
# comparative
# dim.
# diminutive
# fem.
# feminine gender
# gen.
# genitive case
# Gr.
# latinized Greek (the original Greek spelling is not given and the word is transliterated into the Latin alphabet)
# L.
# Latin (indicates that the word is classic Latin and found in an unabridged Latin dictionary)
# masc.
# masculine gender
# M.E.
# Middle English
# M.L.
# Medieval (sometimes pharmaceutical) Latin
# n.
# noun
# neut.
# neuter gender
# N.Gr.
# Neo-Greek (modern Greek)
# N.L.
# Neo-Latin (a word treated and used as a Latin word)
# nom.
# nominative case
# num.
# numerus
# part. adj.
# participle adjective
# part.
# participle
# pass.
# passive
# perf.
# perfect
# pl.
# plural
# pref.
# prefix
# prep.
# preposition
# pres. part.
# present participle
# pron.
# pronoun
# sing.
# singular
# suff.
# suffix
# sup.
# superlative
# sync.
# syncope
# v.
# verb
