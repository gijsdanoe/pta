#!/usr/bin/python3
# file name: exercise2.py
# author: group 3

import nltk

def main():
        path = "holmes.txt"
        f = open(path)
        holmes_raw = f.read()
        sentences = nltk.sent_tokenize(holmes_raw)
        
        word_count = lambda sentence: len(nltk.word_tokenize(sentence))
        print(min(sentences, key=word_count)) # shortest sentence (word count)
        print(max(sentences, key=word_count)) # longest sentence (word count)
        
        nummers = []
        #for sent in sentences:
                #tokens = []
                #tokens += nltk.word_tokenize(sent)
                #lengte = len(tokens)
                #nummers.append(lengte)
                #sort = sorted(nummers)
                #fdist = nltk.FreqDist(sort)
        #for b,f in fdist.items():
                #print(b,f) #c
                
        #print(sum(sort)/len(sort)) # print length average sentence
        #list the character types
        chartypes = sorted(set("".join(sentences)))
        #print("Number of char types: {}".format(len(chartypes)))
        #print("List of character types:")
        #print(chartypes, end="\n\n")

        ## list word types
        wordtypes = sorted(set(sentences))
        #print("Number of word types: {}".format(len(wordtypes)))
        #print("List of word types:\n")
        #print(wordtypes)

        ## print top 20 character-level n-grams
        print("20 Most common character-level unigrams:\n")
        cunigrams_fdist = nltk.FreqDist(holmes_raw)
        for b, f in cunigrams_fdist.most_common(20):
            print("{} '{}'".format(f, b))

        print("20 Most common character-level bigrams:\n")
        cbigrams = nltk.bigrams(holmes_raw)
        cbigrams_fdist = nltk.FreqDist(cbigrams)
        for b, f in cbigrams_fdist.most_common(20):
            print(f, b)

        print("20 Most common character-level trigrams:\n")
        ctrigrams = nltk.trigrams(holmes_raw)
        ctrigrams_fdist = nltk.FreqDist(ctrigrams)
        for b, f in ctrigrams_fdist.most_common(20):
            print(f, b)

         #print top 20 word-level uni-, bi- and trigrams
        print("20 Most common word-level unigrams:\n")
        wunigrams_fdist = nltk.FreqDist(sentences)
        for b, f in wunigrams_fdist.most_common(20):
            print("{} '{}'".format(f, b))

        print("20 Most common word-level bigrams:\n")
        wbigrams = nltk.bigrams(sentences)
        wbigrams_fdist = nltk.FreqDist(wbigrams)
        for b, f in wbigrams_fdist.most_common(20):
            print(f, b)

        print("20 Most common word-level trigrams:\n")
        wtrigrams = nltk.trigrams(sentences)
        wtrigrams_fdist = nltk.FreqDist(wtrigrams)
        for b, f in wtrigrams_fdist.most_common(20):
            print(f, b)
                    

main()
