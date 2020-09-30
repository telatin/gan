#!/usr/bin/env python3
import pandas as pd
import argparse
import itertools
import sys

def eprint(*args, **kwargs):
	"""print to STDERR"""
	print(*args, file=sys.stderr, **kwargs)	

def readListFromExcelWorkbook(filename, workbook_index):
	table =  pd.read_excel (filename, sheet_name=workbook_index, header=0)
	return table["Root"].tolist()

def readListsFromExcel(filename):
	lists = []
	for index in [0,1,2]:
		lists.append(readListFromExcelWorkbook(filename, index) )
	return lists[0], lists[1], lists[2]

def listsPermutations(list1,list2,list3):
	"""
	will receive a list of lists, and return all the possible combinations e.g.
	('seleni', 'entero', 'plasma')
	"""
	combinations = []
	iterables = [ list1 ,list2 ,list3 ]

	for triplet in itertools.product(*iterables):
		combinations.append(triplet)
	return combinations
	
def joinTwoRoots(m, n):
	"""
	Function to join two words
	"""
	return m + n

def combineRoots(rootsList):
	"""
	will receive a list of roots eg ('seleni', 'entero', 'plasma')
	and combine them as single string. This allows to implement rules
	"""
	word = joinTwoRoots(rootsList[0], rootsList[1])

	return joinTwoRoots(word, rootsList[2])




opt_parser = argparse.ArgumentParser(description='Generate bacterial genera with Excel input')

opt_parser.add_argument('-i', '--input',
                        help='Excel file in "autotaxonomer" format',
                        required=True)

                                        
opt_parser.add_argument('-v', '--verbose',
                        help='Increase output verbosity',
                        action='store_true')

opt = opt_parser.parse_args()

counter = 0
prefixes, mids, suffixes = readListsFromExcel(opt.input)
permutations = listsPermutations(prefixes, mids, suffixes)
for triplet in permutations:
	counter += 1
	eprint("#", counter, triplet)
	print(combineRoots(triplet))

