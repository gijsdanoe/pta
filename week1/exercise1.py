#!/usr/bin/python3
# filename: exercise1.py
# author: Group 3

import nltk

# access the corpus we want to use
from nltk.corpus import gutenberg

def main():
	# print files that are in the names corpus
	print(gutenberg.fileids())

	# get the raw text of a file in the corpus and print the first 100 characters
	hamlet_txt = gutenberg.raw("shakespeare-hamlet.txt")
	print(hamlet_txt[:99])

	#get the words as a list and print the first 15 items
	hamlet_list = gutenberg.words("shakespeare-hamlet.txt")
	print(hamlet_list[:14])
	
	# get the sentences of as a list of lists and print the first 3 sentences
	hamlet_sents = gutenberg.sents("shakespeare-hamlet.txt")
	print(hamlet_sents[:4])

	# read a text and print some of it
	path = "../nltk_data/corpora/gutenberg/shakespeare-hamlet.txt"
	f = open(path)
	hamlet = f.read()
	f.close()
	print(hamlet[:100])

	# split the text up into sentences
	sents = nltk.sent_tokenize(hamlet)
	print(sents[20:22])

	# tokenize the sentences
	tokens = []
	for sent in sents:
		tokens += nltk.word_tokenize(sent)
	print(tokens[300:350])

	# print bigrams of a sent
	sent = ["he", "is", "ok", "is", "he", "ok", "is"]
	print(list(nltk.bigrams(sent)))

	# print bigrams with frequentie
	bigrams = nltk.bigrams(sent)
	fdist = nltk.FreqDist(bigrams)
	for b,f in fdist.items():
		print(b,f)
	
main()



