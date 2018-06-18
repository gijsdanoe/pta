#!/usr/bin/python3
#filename: project.py

import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet
import wikipedia
from nltk.tag import StanfordNERTagger
import os

def wordgrouper(list1):
    #compound words are grouped 
    
    taglist = [Tuple[1] for Tuple in list1]
    #grouped(tags =  [list(j) for i,j in groupby(taglist)]
    groupedwords = []
    for i in range(len(list(enumerate(taglist)))):
        if list(enumerate(taglist))[i][1] != 'O':
            x = str(list1[i][0])
            j = i
            while list(enumerate(taglist))[j+1][1] != 'O':
                x = x + " " + str(list1[j+1][0])
                j += 1
                if list(enumerate(taglist))[j+1][1] == 'O':
                    groupedwords.append(x)
            
    return groupedwords
    

def wikilinker(query):
    try:
        return wikipedia.page(query).url
    except wikipedia.DisambiguationError as e:
        return wikipedia.page(e.options[0]).url



    
def tagger(path, st):
    #open ever file in every folder of our testdir
    #for folder in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/"):
        #for folder2 in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/" + folder):

    rawlist = []
    #testing:
    #with open(path + "/en.tok.off.pos", "r") as posfile:
    with open(path + "/" + "en.tok.off.pos", "r") as posfile:
        f = posfile.readlines()
        for line in f:
            rawlist.append(line.split()[3])

        rawstring = " ".join(rawlist)
                #stanford NER tag
        l = st.tag(rawstring.split())
    return l
        
def column(l, path):
    testfile = open(path + "/" + "en.tok.off.pos.test", "w+")
    #testfile = open(path + "/en.tok.off.pos.test", "w+")
        #with open("testdir/" + folder + "/" + folder2 + "/en.tok.off.pos", "r") as postfile:
    #testing:
    with open(path + "/" + "en.tok.off.pos", "r") as posfile:
        n = 0
        Nerlist = [Tuple[1] for Tuple in l]
        #print(l)
        #print(Nerlist)
        wg = wordgrouper(l)
        for row in posfile:
            #if stanford has an appriopriate tag, add it
            x = [s for s in wg if row.split()[3] in s]

            if l[n][1] != "O": 
                columns = row.split()
                columns.append(l[n][1])

                if x:
                    columns.append(wikilinker(x[0]))
                    testfile.write(" ".join(columns))
                    testfile.write("\n")
                    n += 1
                else:
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
#def linkadder(l, path):
    #with open(path + "/en.tok.off.pos.test", "w+") as testfile:
            #wg = wordgrouper(l)
            #for row in testfile:
                #print(row)
                #x = [s for s in wg if row.split()[3] in s]
                #columns = row.split()
                #if x:
                    #columns.append(wikipedia.page(x[0]).url)
                    #testfile.write(" ".join(columns))
                    #testfile.write("\n")




def main():
    st = StanfordNERTagger('/home/lennart/Downloads/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/lennart/Downloads/stanford-ner-2018-02-27/stanford-ner.jar')
    #path = "/home/lennart/projecttextanalyse/eindproject/testdir/p05/d0580/"
    for folder in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/"):
        for folder2 in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/" + folder):
            path = "/home/lennart/projecttextanalyse/eindproject/testdir/" + folder + "/" + folder2
            column(tagger(path,st),folder2)
            #print(path)
main()
