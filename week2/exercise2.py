#!/usr/bin/python3

import nltk
from nltk import pos_tag, word_tokenize

def exercise23():
	f = open("holmes.txt", "rU")
	raw = f.read()
	f.close()
	tokens = nltk.word_tokenize(raw)
	print(pos_tag(tokens))

def exercise24()
	f = open("holmes.txt", "rU")
	raw = f.read()
	tokens = nltk.word_tokenize(raw)
	pos_tags = pos_tag(tokens)
	tags = []
	for x in pos_tags:
		tags += x[1:]		
	finder = BigramCollocationFinder.from_words(tags)
	print(finder.nbest(nltk.collocations.BigramAssocMeasures().pmi, 20))

def main():
	exercise23()
	exercise24()
main()

