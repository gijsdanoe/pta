#!/usr/bin/python3
#filename: project.py

import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet
import wikipedia
from nltk.tag import StanfordNERTagger
import os
from operator import eq 
    
def tagger(path, st):
    st = StanfordNERTagger('/home/thomas/Downloads/stanford-ner-2017-06-09/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/thomas/Downloads/stanford-ner-2017-06-09/stanford-ner.jar')
    #open ever file in every folder of our testdir
    #for folder in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/"):
        #for folder2 in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/" + folder):

    rawlist = []
    #testing:
    with open(path + "/en.tok.off.pos", "r") as posfile:
    #with open("testdir/" + folder + "/" + folder2 + "/en.tok.off.pos", "r") as posfile:
        f = posfile.readlines()
        for line in f:
            rawlist.append(line.split()[3])

        rawstring = " ".join(rawlist)
                #stanford NER tag
        l = st.tag(rawstring.split())
    return l
        
def column(l, path):
    #testfile = open("testdir/" + folder + "/" +  folder2 + "/en.tok.off.pos.test", "w+")
    testfile = open(path + "/en.tok.off.pos.test", "w+")
        #with open("testdir/" + folder + "/" + folder2 + "/en.tok.off.pos", "r") as postfile:
    #testing:
    with open(path + "/en.tok.off.pos", "r") as posfile:
        n = 0
        Nerlist = [Tuple[1] for Tuple in l]
        print(Nerlist)
        for row in posfile:
            #if stanford has an appriopriate tag, add it

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

    #with open("testdir/" + folder + "/" + folder2 + "/en.tok.off.pos.test", "r+") as testfile:
        #for row in testfile:


def main():
    st = StanfordNERTagger('/home/thomas/Downloads/stanford-ner-2017-06-09/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/thomas/Downloads/stanford-ner-2017-06-09/stanford-ner.jar')
    path = "/home/thomas/projecttextanalyse/eindproject/testdir/p05/d0580/"
    column(tagger(path, st), path)
    
main()
