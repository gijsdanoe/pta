#!/usr/bin/python3
import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet as wn
import wikipedia
from nltk.tag import StanfordNERTagger
import itertools
from collections import OrderedDict
import os

def wikilinker(query, wordlist):
    try:
        return wikipedia.page(query).url
    except wikipedia.exceptions.DisambiguationError as e: 
        ll = []  
        sumlist = []        
        for option in e.options:
            dis = 1/nltk.edit_distance(query, option)
            ll.append(dis)
            try:
                a = nltk.word_tokenize(wikipedia.page(option).summary)
                match = set(a).intersection(wordlist)
                sumlist.append(len(match))
            except:
                
                sumlist.append(0)
        multilist = []
        for (ws,match) in zip(ll, sumlist):
            multilist.append(ws*match)
        maxval = multilist.index(max(multilist))
        return wikipedia.page(e.options[maxval]).url
    except wikipedia.exceptions.WikipediaException as r:
        pass

def main():
    query = 'new york'
    wordlist = ['washington', 'is', 'a', 'nice', 'city', 'capital', 'dc']
    print(wikilinker(query, wordlist))

main()
