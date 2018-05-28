#!/usr/bin/python3
#filename: exercise1.py
#exercise 1 of week 5

import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet
import wikipedia

def main():
	wiki = wikipedia.page("forum_for_the_future")
	raw = wiki.content
	sents = nltk.sent_tokenize(raw)
	words = nltk.word_tokenize(raw)
	tagged = nltk.pos_tag(words)
	nouns = [word for word,pos in tagged if pos.startswith('N')]
	polysemous = []
	average_synsets = []
	for noun in nouns:
		synsets = wordnet.synsets(noun, pos="n")
		average_synsets.append(len(synsets))
		if len(synsets) > 1:
			polysemous.append(noun)
			syn = lesk(raw, noun, "n")
			print("{0}\t{1}".format(noun, syn))
	print("1. Porportionof polyseous words: ", len(polysemous))
	print("2. ") #check more than 1 page
	print("3. Average number of senses for the polysemous words: ", sum(average_synsets)/len(average_synsets))
	print("4.")
	nul_synsets = []
	one_synsets = []
	two_synsets = []
	three_synsets = []
	four_synsets = []
	five_synsets = []
	six_synsets = []
	seven_synsets = []
	eigth_synsets = []
	nine_synsets = []
	ten_synsets = []
	tenplus_synsets = []
	for noun in nouns:
		synsets = wordnet.synsets(noun, pos="n")
		if len(synsets) == 0:
			nul_synsets.append(synsets)
		elif len(synsets) == 1:
			one_synsets.append(synsets)
		elif len(synsets) == 2:
			two_synsets.append(synsets)
		elif len(synsets) == 3:
			three_synsets.append(synsets)
		elif len(synsets) == 4:
			four_synsets.append(synsets)
		elif len(synsets) == 5:
			five_synsets.append(synsets)
		elif len(synsets) == 6:
			six_synsets.append(synsets)
		elif len(synsets) == 7:
			seven_synsets.append(synsets)
		elif len(synsets) == 8:
			eigth_synsets.append(synsets)
		elif len(synsets) == 9:
			nine_synsets.append(synsets)
		elif len(synsets) == 10:
			ten_synsets.append(synsets)
		elif len(synsets) > 10:
			tenplus_synsets.append(synsets)
	print("4.\n{0} words showed 0 senses\n{1} words showed 1 senses\n{2} words showed 2 senses\n{3} words showed 3 senses\n{4} words showed 4 senses\n{5} words showed 5 senses\n{6} words showed 6 senses\n{7} words showed 7 senses\n{8} words showed 8 senses\n{9} words showed 9 senses\n{10} words showed 10 senses\n{11} words showed more than 10 senses".format(len(nul_synsets),len(one_synsets),len(two_synsets),len(three_synsets),len(four_synsets),len(five_synsets),len(six_synsets),len(seven_synsets),len(eigth_synsets),len(nine_synsets),len(ten_synsets),len(tenplus_synsets)))







main()
