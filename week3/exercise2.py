#!/usr/bin/python3
from nltk.tag import StanfordNERTagger
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import os
from operator import itemgetter

def main():
	f = open("ada_lovelace.txt")
	raw = f.read()
	tokens = nltk.word_tokenize(raw)
	tagged = nltk.pos_tag(tokens)
	nouns = [token for token,pos in tagged if pos.startswith('N')]
	lemmatizer = WordNetLemmatizer()
	noun_lemmas = []

	st = StanfordNERTagger('/home/thomas/Downloads/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/thomas/Downloads/stanford-ner-2018-02-27/stanford-ner.jar')


	l = st.tag(raw.split())
	sorted_l = sorted(l, key=lambda x: x[1])
	print(sorted_l)

	#exercise2.3
	print("Exercise 2.3, nouns: ")
	n = st.tag(nouns)
	new = [tuple(s if s != "0" else "MISC" for s in tup) for tup in n] 
	print(new)
if __name__ == "__main__":
	main()
