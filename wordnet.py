import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet as wn
import wikipedia
from nltk.tag import StanfordNERTagger
import os
from operator import eq 
import re

def main():
    st = StanfordNERTagger('/home/s3494888/Desktop/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/s3494888/Desktop/stanford-ner-2018-02-27/stanford-ner.jar')
    path = "/home/s3494888/Desktop/projecttextanalyse/eindproject/testdir/p50/d0328/"
    testfile = open(path + "/en.tok.off.pos.test", "w+")
    rawlist = []
    with open(path + "/en.tok.off.pos", "r") as posfile:
        f = posfile.readlines()
        for line in f:
            if line.split()[4].startswith('N'):
                rawlist.append(line.split()[3])
            else:
                pass
        rawstring = " ".join(rawlist)

        l = st.tag(rawstring.split())

    with open(path + "/en.tok.off.pos", "r") as posfile:
        n = 0
        Nerlist = [Tuple[1] for Tuple in l]
        print(rawlist)


    #with open("testdir/" + folder + "/" + folder2 + "/en.tok.off.pos.test", "r+") as testfile:
        #for row in testfile:
    synlist = []
    for p in rawlist:
        deflist = []
        for syns in wn.synsets(p):

            deflist.append(syns.definition())
        synlist.append(deflist)
    print(synlist)

    for deflist in synlist:
        for item in deflist:
            if ' city ' in item:
                print('{0} - CIT'.format(rawlist[synlist.index(deflist)]))
            elif ' nation ' in item:
                print('{0} - COU'.format(rawlist[synlist.index(deflist)]))

main()
