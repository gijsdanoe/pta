#!/usr/bin/python3

import nltk
from nltk import pos_tag, word_tokenize

def main():

	f = open("holmes.txt", "rU")
	raw = f.read()
	tokens = nltk.word_tokenize(raw)
	print(pos_tag(tokens))
main()

