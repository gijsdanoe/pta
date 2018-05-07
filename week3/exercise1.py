#!/usr/bin/python3
#exercise1

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from nltk.tag import UnigramTagger
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter

def ex1_1():
        relative = wn.synset('relative.n.01')
        illness = wn.synset('illness.n.01')
        science = wn.synset('science.n.01')
        print(relative.hyponyms())
        print(illness.hyponyms())
        print(science.hyponyms())

def ex1_3():
        car = wn.synset('car.n.01')
        automobile = wn.synset('automobile.n.01')
        coast = wn.synset('coast.n.01')
        shore = wn.synset('shore.n.01')
        food = wn.synset('food.n.01')
        fruit = wn.synset('fruit.n.01')
        journey = wn.synset('journey.n.01')
        monk = wn.synset('monk.n.01')
        slave = wn.synset('slave.n.01')
        moon = wn.synset('moon.n.01')
        string = wn.synset('string.n.01')
        print(car.path_similarity(automobile))
        print(coast.path_similarity(shore))
        print(food.path_similarity(fruit))
        print(journey.path_similarity(car))
        print(monk.path_similarity(slave))
        print(moon.path_similarity(string))

def hypernymOf(synset1, synset2):
        """ Returns True if synset2 is a hypernym of
        synset1, or if they are the same synset.
        Returns False otherwise. """
        if synset1 == synset2:
                return True
        for hypernym in synset1.hypernyms():
                if synset2 == hypernym:
                        return True
                if hypernymOf(hypernym, synset2):
                        return True
        return False

def getMaxSim(synsets1, synsets2):
        maxSim = None
        for s1 in synsets1:
                for s2 in synsets2:
                        sim = s1.lch_similarity(s2)
                        if maxSim == None or maxSim < sim:
                                maxSim = sim
        return maxSim

def main():
        print("\nExercise 1.1")
        ex1_1()
        print("\nExercise 1.2")
        f = open("ada_lovelace.txt")
        raw = f.read()
        tokens = nltk.word_tokenize(raw)
        tagged = nltk.pos_tag(tokens)
        nouns = [token for token,pos in tagged if pos.startswith('N')]
        lemmatizer = WordNetLemmatizer()
        noun_lemmas = []
        for noun in nouns:
                lemma = lemmatizer.lemmatize(noun, wn.NOUN)
                noun_lemmas.append(lemma)
        relative_ss = wn.synsets("relative", pos="n")
        illness_ss = wn.synsets("illness", pos="n")
        science_ss = wn.synsets("science", pos="n")
        relative_lemmas = []
        illness_lemmas = []
        science_lemmas = []
        for lemma in noun_lemmas:
                synsets = wn.synsets(lemma, pos="n")
                for synset in synsets:
                        if hypernymOf(synset, relative_ss[0]) is True or hypernymOf(synset, relative_ss[1]) is True:
                                relative_lemmas.append(lemma)
                                break
                        elif hypernymOf(synset, illness_ss[0]) is True:
                                illness_lemmas.append(lemma)
                                break
                        elif hypernymOf(synset, science_ss[0]) is True or hypernymOf(synset, science_ss[1]) is True:
                                science_lemmas.append(lemma)
                                break

        hypernyms = []
        for lemma in noun_lemmas:
                synsets = wn.synsets(lemma, pos="n")
                for synset in synsets:
                        for hypernym in synset.hypernyms():
                                hypernyms.append(hypernym)
        print("The top 25 noun hypernyms are:\n", Counter(hypernyms).most_common(25))
        hypernym_num = []
        one_hypernyms = []
        more_hypernyms = []
        for lemma in noun_lemmas:
                synsets = wn.synsets(lemma, pos="n")
                hypernym_num.append(len(synsets))
                if len(synsets) == 1:
                        lemma_t = lemma, synsets[0]
                        one_hypernyms.append(lemma_t)
                elif len(synsets) > 1:
                        lemma_t = lemma, synsets
                        more_hypernyms.append(lemma_t)
                
        print("\nThere are {0} lemmas with only one hypernym.\nSome examples are:\n{1}".format(len(one_hypernyms), one_hypernyms[:4]))
        print("\nThere are {0} lemmas with more than one hypernym.\nSome examples are:\n{1}".format(len(more_hypernyms), more_hypernyms[:4]))
        print("\nThe average amount of hypernyms for one lemma is:", sum(hypernym_num)/len(hypernym_num)) 
        print("\nExercise 1.3")
        ex1_3()
                        
if __name__ == "__main__":
        main()


