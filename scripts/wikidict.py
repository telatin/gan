#!/usr/bin/env python3
from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()
word = parser.fetch("domus")
another_word = parser.fetch("domus", "latin")
parser.set_default_language("french")
parser.exclude_part_of_speech("noun")
parser.include_relation("alternative forms")
