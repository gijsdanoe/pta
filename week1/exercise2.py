#!/usr/bin/python3
# file name: exercise2.py
# author: group 3

import nltk

def main():
	path = "holmes.txt"
	f = open(path)
	holmes_raw = f.read()
	sentences = nltk.sent_tokenize(holmes_raw)
	
	word_count = lambda sentence: len(nltk.word_tokenize(sentence))
	print(min(sentences, key=word_count)) # shortest sentence (word count)
	print(max(sentences, key=word_count)) # longest sentence (word count)
	
	nummers = []
	for sent in sentences:
		tokens = []
		tokens += nltk.word_tokenize(sent)
		lengte = len(tokens)
		nummers.append(lengte)
		sort = sorted(nummers)
		fdist = nltk.FreqDist(sort)
	for b,f in fdist.items():
		print(b,f) #c
		
	print(sum(sort)/len(sort)) # print length average sentence
		

main()
