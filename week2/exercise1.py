#!/usr/bin/python3
# filename: exercise1.py
# this is the file for exercise 1 in week 2
# author: group 3

import nltk
from nltk import word_tokenize
from nltk.collocations import *

def pmi(text, bigram_measures):
        sents = nltk.sent_tokenize(text)
        tokens = []
        for sent in sents:
                tokens += nltk.word_tokenize(sent)
        finder = BigramCollocationFinder.from_words(tokens)
        print("the 20 most likely colloctions according to PMI are {0}".format(finder.nbest(bigram_measures.pmi, 20)))

def chi_sq(text, bigram_measures):
        sents = nltk.sent_tokenize(text)
        tokens = []
        for sent in sents:
                tokens += nltk.word_tokenize(sent)
        finder = BigramCollocationFinder.from_words(tokens)
        print("the 20 most likely collocations according to chi squared are {0}".format(finder.nbest(bigram_measures.chi_sq, 20)))

def main():
        file = open("holmes.txt")
        text = file.read()
        file.close()
        bigram_measures = nltk.collocations.BigramAssocMeasures()
        pmi(text, bigram_measures)
        bigram_measures1 = nltk.collocations.BigramAssocMeasures()
        chi_sq(text, bigram_measures1)
        print("1c: I can see no differences of ranking within the results of the two methods, they are completely equal")
        print("1.2: the original formula for chi squared can be rewritten like shown in the exercise becausei  N(O11 O22 - O12 O21) is the same as the sum of all differences between the expected value and the observed value, and for the bottom row of the equation: E (the expected frequencies) are the same as (O11+O12)(O11+O21)(O12+O22)(O21+O22)")
        
if __name__ == "__main__":
        main()
