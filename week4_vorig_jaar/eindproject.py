#!/usr/bin/python3
import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
import wikipedia
from nltk.parse import CoreNLPParser
import itertools
from collections import OrderedDict
import os

def sfNERTagger(rawText):
	'''(sf = stanford) get the raw text from a file and convert that to a list with tuples of each word with a StanFord annotated NER-tag'''
	parser = CoreNLPParser(url='http://localhost:9000', tagtype='ner')
	tupleList = list(parser.tag(rawText.split()))
	#convert list of tuple to list of lists, so we can change tags we dont need
	NERList = [list(tuple) for tuple in tupleList]

	#change tags we dont need
	for item in NERList:
		if item[1] == 'COUNTRY': item[1] = 'COU'
		elif item[1] == 'PERSON': item[1] = 'PER'
		elif item[1] == 'CITY': item[1] = 'CIT'
		elif item[1] == 'ORGANIZATION': item[1] = 'ORG'
		else: item[1] = ''

	return NERList

def ownTagger (NERList):
#take nerlist, when i[1] =='': see if this tagger can tag it, other wise leave empty. output ex: [[word, tag][word, tag]]

	synlist = []
	ll = []
	onesynlist = []
	simlist = []
	current_chunk = []

	#make list out of NERList that only contains the words that are not tagged by NERTagger
	for n in NERList:
		if n[1] == '':
	#for p in rawlist:
			onedeflist = []
			deflist = []
			klist = []
			for syns in wn.synsets(n[1]):
				deflist.append(syns.definition())
				onedeflist.append(syns)
				klist.append(syns)
			if not deflist:
				ll.append([])
			elif len(deflist) == 1:
				onesynlist.append(onedeflist[0])
				ll.append(klist)
			else:
				synlist.append(deflist)
				ll.append(klist)

			newlist = []
			for item in ll:
				itemb = []
				for i in item:
					synb = []
					for a in onesynlist:
						ps = i.path_similarity(a)
						synb.append(ps)
					itemb.append(synb)
			newlist.append(itemb)
		newlist = [[[0 if x is None else x for x in i] for i in item] for item in newlist]
		newlist = [[sum(i) for i in item] for item in newlist]

	maxlist = []
	newsynlist = []

	for item in newlist:
		if not item:
			maxlist.append([])
		else:
			maxlist.append(item.index(max(item)))


	for x,value in zip(ll, maxlist):
		if value == []:
			newsynlist.append([])
		else:
			a = x[value].definition()
			newsynlist.append(a)
	synlist = newsynlist


	#lists of all words that could appear in the definitions of the unigrams and bigrams
	city = [' city ', ' village ', ' town ', 'capital']
	country = [' nation ', ' republic ', ' monarchy ', ' province ', ' island ' , ' archipelago ']
	sport = [' sport ', 'combat', ' game ']
	natural_places = [' desert ', ' volcano ', ' sea ', ' ocean ',	' lake ', ' river ', ' jungle ', ' waterfall ', ' glacier ', ' mountain ', ' forest ' , ' crater ', ' cave ', ' canyon ', ' fjord ', ' park ', ' bay ', ' valley ', ' cliff ', ' reef ']
	entertainment = [' book ', 'magazine', 'film', 'movie', 'song', 'journal', 'newspaper']
	animal = ['mammal', 'bird', 'fish', 'amphibian', 'reptil', 'crustacean', 'insect', 'carnivore', 'herbivore', 'species', 'breed', 'cattle', 'quadruped', 'pachyderm', 'feline', 'ungulate']
	person = ['born']
	organization = ['organization']

	#if one of the words appears in the definition of the uni- or bigram, append a tuple to a list with the word and the NER tag
	for deflist in synlist:
		if any(x in deflist for x in city):
			current_chunk.append((NERList[synlist.index(deflist)][0], 'CIT'))
		elif any(x in deflist for x in country):
			current_chunk.append((NERList[synlist.index(deflist)][0], 'COU'))
		elif any(x in deflist for x in sport):
			current_chunk.append((NERList[synlist.index(deflist)][0], 'SPO'))
		elif any(x in deflist for x in natural_places):
			current_chunk.append((NERList[synlist.index(deflist)][0], 'NAT'))
		elif any(x in deflist for x in entertainment):
			current_chunk.append((NERList[synlist.index(deflist)][0], 'ENT'))
		elif any(x in deflist for x in animal):
			current_chunk.append((NERList[synlist.index(deflist)][0], 'ANI'))

	return current_chunk

def sfNERWriter(POSFile, NERList):
	'''Takes output of sfNERTagger() -->NERList, iters over the POSFile, if NERList[index][1] is meaningful: add the appropriate tag. create ENTFile and write every line'''
	with open(POSFile, "r") as f1:
		POSLines = f1.readlines()
	with open(str(POSFile + ".test"),"w") as f2:
		for lineNumber, line in enumerate(POSLines):
			line  = line.strip('\n')
			if line.split()[3] == NERList[lineNumber][0]:
				f2.write(str(line + " " + NERList[lineNumber][1] + '\n'))
			else:
				f2.write("error")
	# with open("posfile", "r") as posfile:
	#lines = posfile.readlines()
#with open("posfile", "w") as posfile:
	#for line in lines:
		#sources.write(blablabla)


def getContinuousChunks(NERList):
	'''takes NERList and lists together words that need chunking'''
	continuous_chunk = []
	current_chunk = []

	for token, tag in NERList:
		if tag != "":
			current_chunk.append((token))
		else:
			if current_chunk: # if the current chunk is not empty
				continuous_chunk.append(current_chunk)
				current_chunk = []
	# Flush the final current_chunk into the continuous_chunk, if any.
	if current_chunk:
		continuous_chunk.append(current_chunk)
	return continuous_chunk

def main():
	with open('data/p51/d0060/en.raw') as f1:
		rawText = f1.read()
		NERList = sfNERTagger(rawText)
		# x output example: [('out', 'O'),('two','Date")] etc

	#with open('data/p51/d0060/en.tok.off.pos') as f2:
		#for lineNumber, line in enumerate(f2):
			#if line.split()[3] == x[lineNumber][0]:
				#print('True', NERRaw[lineNumber], f2.name + ".ent")

	POSFile = 'data/p51/d0060/en.tok.off.pos'
	#print(NERRaw)
	sfNERWriter(POSFile, NERList)
	x = getContinuousChunks(NERList)
	y = ownTagger(NERList)
	print(y)
if __name__ == "__main__":
	main()
