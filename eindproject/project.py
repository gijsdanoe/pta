#!/usr/bin/python3
#filename: eindproject.py

import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet
import wikipedia
from nltk.tag import StanfordNERTagger
import os


def main(): 
    wiki = wikipedia.page("emmen, netherlands")
    raw = wiki.content
    sents = nltk.sent_tokenize(raw)
    words = nltk.word_tokenize(raw)
    tagged = nltk.pos_tag(words)
    nouns = [word for word,pos in tagged if pos.startswith('N')]
    st = StanfordNERTagger('/home/lennart/Downloads/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/lennart/Downloads/stanford-ner-2018-02-27/stanford-ner.jar')
    for folder in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/"):
        for folder2 in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/" + folder):
    #path = "/home/lennart/projecttextanalyse/eindproject/testdir/p05/d0580/"
            testfile = open("testdir/" + folder + "/" +  folder2 + "/en.tok.off.pos.test", "w+")
            rawlist = []
            with open("testdir/" + folder + "/" + folder2 + "/en.tok.off.pos", "r") as posfile:
                f = posfile.readlines()
                for line in f:
                    rawlist.append(line.split()[3])

                rawstring = " ".join(rawlist)
                l = st.tag(rawstring.split())
            with open("testdir/" + folder + "/" + folder2 + "/en.tok.off.pos", "r") as postfile:
                n = 0
                for row in postfile:
                    if l[n][1] != "O": 
                        columns = row.split()
                        columns.append(l[n][1])
                        testfile.write(" ".join(columns))
                        testfile.write("\n")
                        n += 1
                    else:
                        columns = row.split()
                        testfile.write(" ".join(columns))
                        testfile.write("\n")
                        n += 1



main()
