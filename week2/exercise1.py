#!/usr/bin/python3
# filename: exercise1.py
# this is the file for exercise 1 in week 2
# author: group 3

import nltk
from nltk import word_tokenize
from nltk.collocations import *

def pmi(text, bigram_measures):
	sents = nltk.sent_tokenize(text)
	tokens = []
	for sent in sents:
		tokens += nltk.word_tokenize(sent)
	finder = BigramCollocationFinder.from_words(tokens)
	print("the 20 most likely colloctions according to PMI are {0}".format(finder.nbest(bigram_measures.pmi, 20)))

def chi_sq(text, bigram_measures):
	sents = nltk.sent_tokenize(text)
	tokens = []
	for sent in sents:
		tokens += nltk.word_tokenize(sent)
	finder = BigramCollocationFinder.from_words(tokens)
	print("the 20 most likely collocations according to chi squared are {0}".format(finder.nbest(bigram_measures.chi_sq, 20)))

def main():
	file = open("holmes.txt")
	text = file.read()
	file.close()
	bigram_measures = nltk.collocations.BigramAssocMeasures()
	pmi(text, bigram_measures)
	bigram_measures1 = nltk.collocations.BigramAssocMeasures()
	chi_sq(text, bigram_measures1)

if __name__ == "__main__":
	main()
