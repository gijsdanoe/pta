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
    return list(parser.tag(rawText.split()))

def sfNERWriter(POSFile, NERList):
    '''Takes output of sfNERTagger() -->NERList, iters over the POSFile, if NERList[index][1] is meaningful: add the appropriate tag. create ENTFile and write every line'''
    with open(POSFile, "r") as f1:
        POSLines = f1.readlines()
    with open(str(POSFile + ".ent"),"w") as f2:
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
        if tag != "O":
            current_chunk.append((token, tag))
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
        NERRaw = sfNERTagger(rawText)
        # x output example: [('out', 'O'),('two','Date")] etc

    #with open('data/p51/d0060/en.tok.off.pos') as f2:
        #for lineNumber, line in enumerate(f2):
            #if line.split()[3] == x[lineNumber][0]:
                #print('True', NERRaw[lineNumber], f2.name + ".ent")

    POSFile = 'data/p51/d0060/en.tok.off.pos'
    #print(NERRaw)
    sfNERWriter(POSFile, NERRaw)
if __name__ == "__main__":
    main()
