#!/usr/bin/python3
#filename: project.py

import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet as wn
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

    except:
        pass


    
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
        

def lgijs(l,wordlist):
    out = []
    for i in l:
        if i[0] in wordlist:
            j = wordlist.index(i[0])
            i = wordlist[j]
        else:
            out.append(i)
    return out



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
            x = [s for s in wg if row.split()[3] in s.split(" ")]
            #x = []
            #for s in wg:
                #if row.split()[3] in s.split(" "):
                    #x.append(s)


            if l[n][1] != "O": 
                columns = row.split()
                columns.append(l[n][1])

                if l[n][1] == "LOCATION":
                    columns[5] = ""
                    testfile.write(" ".join(columns))
                    testfile.write("\n")
                    n += 1

                elif l[n][1] == "MISC":
                    columns[5] = ""
                    testfile.write(" ".join(columns))
                    testfile.write("\n")
                    n += 1
                elif l[n][1] == "PERSON":
                    columns[5] ="PER"
                    testfile.write(" ".join(columns))
                    testfile.write("\n")
                    n += 1
                elif l[n][1] == "ORGANIZATION":
                    columns[5] = "ORG"
                    testfile.write(" ".join(columns))
                    testfile.write("\n")
                    n += 1

                #if x:
                    #try:

                        #columns.append(wikilinker(x[0]))
                        #testfile.write(" ".join(columns))
                        #testfile.write("\n")
                        #n += 1
                    #except TypeError:
                        #pass

                else:
                    testfile.write(" ".join(columns))
                    testfile.write("\n")
                    n += 1

            else:
                columns = row.split()
                testfile.write(" ".join(columns))
                testfile.write("\n")
                n += 1

def gijs(st,path):
    
#open and read the file, make a list of all nouns
    testfile = open(path + "/en.tok.off.pos.test", "w+")
    rawlist = []
    rawlist2 = []
    with open(path + "/en.tok.off.pos", "r") as posfile:
        f = posfile.readlines()
        for line in f:
            rawlist2.append(line.split()[3])
            if line.split()[4].startswith('N'):
                rawlist.append(line.split()[3])               
            else:
                pass
        rawstring = " ".join(rawlist2)
        l = st.tag(rawstring.split())
        

#make a list of every wn definition of every word in the raw text list, in case of ambiguity the program calculates the path similarity of every option with every word in the text; he picks the option with the highest cumulative path similarity
    synlist = []
    ll = []
    onesynlist = []
    simlist = []
    
    for p in rawlist:
        onedeflist = []
        deflist = []   
        klist = []
        for syns in wn.synsets(p):
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



    #open ever file in every folder of our testdir
    #for folder in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/"):
        #for folder2 in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/" + folder):




    taglist = [Tuple[1] for Tuple in l]
    #grouped(tags =  [list(j) for i,j in groupby(taglist)]
    groupedwords = []
    for i in range(len(list(enumerate(taglist)))):
        if list(enumerate(taglist))[i][1] != 'O':
            x = str(l[i][0])
            j = i
            while list(enumerate(taglist))[j+1][1] != 'O':
                x = x + " " + str(l[j+1][0])
                j += 1
                if list(enumerate(taglist))[j+1][1] == 'O':
                    groupedwords.append(x)
    bigramdeflist = []
    bigramlist = []
    for bigram in groupedwords:
        bilist = []
        bigraml = bigram.split()
        bi_gram = '_'.join(bigraml)
        for syns in wn.synsets(bi_gram):
            bilist.append(syns.definition())
        if not bilist:
            try:
                bigramdeflist.append(wikipedia.summary(bigram, sentences=1))
            except:
                bigramdeflist.append([])
        else:
            bigramdeflist.append(bilist[0])
 
 
    

#lists of all words that could appear in the definitions of the unigrams and bigrams
    city = [' city ', ' village ', ' town ', 'capital']
    country = [' nation ', ' republic ', ' monarchy ', ' province ']
    sport = [' sport ', 'combat', ' game ']
    natural_places = [' desert ', ' volcano ', ' sea ', ' ocean ',  ' lake ', ' river ', ' jungle ', ' waterfall ', ' glacier ', ' mountain ', ' forest ' , ' crater ', ' cave ', ' canyon ', ' fjord ', ' park ', ' bay ', ' valley ', ' cliff ', ' reef ']
    entertainment = [' book ', 'magazine', 'film', 'movie', 'song', 'journal', 'newspaper', 'show', 'band']
    animal = ['mammal', 'bird', 'fish', 'amphibian', 'reptil', 'crustacean', 'insect', 'carnivore', 'herbivore', 'species', 'breed', 'cattle', 'quadruped', 'pachyderm', 'feline', 'ungulate']
    
    person = ['born' ]
    organization = ['organization', 'multinational', 'company']
#if one of the words appears in the definition of the uni- or bigram, append a tuple to a list with the word and the NER tag
    wordlist = []  
    for deflist in synlist:
        if any(x in deflist for x in city):
            wordlist.append((rawlist[synlist.index(deflist)], 'CIT'))
        elif any(x in deflist for x in country):
            wordlist.append((rawlist[synlist.index(deflist)], 'COU'))
        elif any(x in deflist for x in sport):
            wordlist.append((rawlist[synlist.index(deflist)], 'SPO'))
        elif any(x in deflist for x in natural_places):
            wordlist.append((rawlist[synlist.index(deflist)], 'NAT'))
        elif any(x in deflist for x in entertainment):
            wordlist.append((rawlist[synlist.index(deflist)], 'ENT'))
        elif any(x in deflist for x in animal):
            wordlist.append((rawlist[synlist.index(deflist)], 'ANI'))
        elif any(x in deflist for x in organization):
            wordlist.append((rawlist[synlist.index(deflist)], 'ORG'))
        elif any(x in deflist for x in person):
            wordlist.append((rawlist[synlist.index(deflist)], 'PER'))


    for bigramdf in bigramdeflist:
        if any(x in bigramdf for x in city):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'CIT'))

        elif any(x in bigramdf for x in country):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'COU'))

        elif any(x in bigramdf for x in sport):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'SPO'))

        elif any(x in bigramdf for x in natural_places):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'NAT'))

        elif any(x in bigramdf for x in entertainment):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'ENT'))

        elif any(x in bigramdf for x in animal):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'ANI'))
        elif any(x in bigramdf for x in organization):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'ORG'))
        elif any(x in bigramdf for x in person):
            wordlist.append((groupedwords[bigramdeflist.index(bigramdf)], 'PER'))


    return wordlist




           


def main():
    st = StanfordNERTagger('/home/thomas/Downloads/stanford-ner-2017-06-09/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/thomas/Downloads/stanford-ner-2017-06-09/stanford-ner.jar')
    #path = "/home/lennart/projecttextanalyse/eindproject/testdir/p05/d0580/"
    #for folder in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/"):
        #for folder2 in os.listdir("/home/lennart/projecttextanalyse/eindproject/testdir/" + folder):
            #path = "/home/lennart/projecttextanalyse/eindproject/testdir/" + folder + "/" + folder2
    path = "/home/thomas/projecttextanalyse/eindproject/testdir/p52/d0352"

    #column(tagger(path,st),path)
    l = tagger(path,st)
    wordlist = gijs(st,path)
    print(wordlist)
    
    


main()
