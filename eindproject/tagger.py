#!/usr/bin/python3
import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet as wn
import wikipedia
from nltk.tag import StanfordNERTagger
import itertools
from collections import OrderedDict

def wikilinker(query):
    try:
        return wikipedia.page(query).url
    except wikipedia.DisambiguationError as e:
        return wikipedia.page(e.options[0]).url
    except wikipedia.exceptions.WikipediaException as r:
        pass
def main():
#open and read the file, make a list of all nouns
    st = StanfordNERTagger('/home/lennart/Downloads/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/lennart/Downloads/stanford-ner-2018-02-27/stanford-ner.jar')
    path = "/home/lennart/projecttextanalyse/eindproject/testdir/p05/d0692"
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
        

#make a list of every wordnet definition of every word in the raw text list, in case of ambiguity the program calculates the path similarity of every option with every word in the text; he picks the option with the highest cumulative path similarity
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
    print(groupedwords)
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
    country = [' nation ', ' republic ', ' monarchy ', ' province ', ' island ' , ' archipelago ']
    sport = [' sport ', 'combat', ' game ']
    natural_places = [' desert ', ' volcano ', ' sea ', ' ocean ',  ' lake ', ' river ', ' jungle ', ' waterfall ', ' glacier ', ' mountain ', ' forest ' , ' crater ', ' cave ', ' canyon ', ' fjord ', ' park ', ' bay ', ' valley ', ' cliff ', ' reef ']
    entertainment = [' book ', 'magazine', 'film', 'movie', 'song', 'journal', 'newspaper']
    animal = ['mammal', 'bird', 'fish', 'amphibian', 'reptil', 'crustacean', 'insect', 'carnivore', 'herbivore', 'species', 'breed', 'cattle', 'quadruped', 'pachyderm', 'feline', 'ungulate']
    person = ['born']
    organization = ['organization']
    
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



    groupedwordslist = []
    for item in groupedwords:
        item = item.split()
        groupedwordslist.append(item)   


    firstitem = [item[0] for item in groupedwordslist]
    seconditem = [item[1] for item in groupedwordslist]

    for bigramdf in bigramdeflist:
        if any(x in bigramdf for x in city):
            wordlist.append((firstitem[bigramdeflist.index(bigramdf)], 'CIT'))
            wordlist.append((seconditem[bigramdeflist.index(bigramdf)], 'CIT'))

        elif any(x in bigramdf for x in country):
            wordlist.append((firstitem[bigramdeflist.index(bigramdf)], 'COU'))
            wordlist.append((seconditem[bigramdeflist.index(bigramdf)], 'COU'))

        elif any(x in bigramdf for x in sport):
            wordlist.append((firstitem[bigramdeflist.index(bigramdf)], 'SPO'))
            wordlist.append((seconditem[bigramdeflist.index(bigramdf)], 'SPO'))

        elif any(x in bigramdf for x in natural_places):
            wordlist.append((firstitem[bigramdeflist.index(bigramdf)], 'NAT'))
            wordlist.append((seconditem[bigramdeflist.index(bigramdf)], 'NAT'))

        elif any(x in bigramdf for x in entertainment):
            wordlist.append((firstitem[bigramdeflist.index(bigramdf)], 'ENT'))
            wordlist.append((seconditem[bigramdeflist.index(bigramdf)], 'ENT'))

        elif any(x in bigramdf for x in animal):
            wordlist.append((firstitem[bigramdeflist.index(bigramdf)], 'ANI'))
            wordlist.append((seconditem[bigramdeflist.index(bigramdf)], 'ANI'))


    ll = list(set(wordlist))
    l = [list(tpl) for tpl in l]
    for item in l:
        if item[1] == 'MISC':
            item[1] = ''
        elif item[1] == 'ORGANIZATION':
            item [1] = 'ORG'
        elif item[1] == 'PERSON':
            item[1] = 'PER'
        elif item[1] =='LOCATION':
            item[1] = ''.join([i[1] for i in ll if item[0] == i[0]])
        elif item [1] == 'O':
            item[1] = ''.join([i[1] for i in ll if item[0] == i[0]])
    l = [tuple(ls) for ls in l]
           
    print(l)
    with open(path + "/" + "en.tok.off.pos", "r") as posfile:
        n = 0
        Nerlist = [Tuple[1] for Tuple in l]
        #print(l)
        #print(Nerlist)
        wg = l
        #tagged = [tuple for tuple in wg if tuple[1] != '']
        for row in posfile:
            #if stanford has an appriopriate tag, add it
            x = [s for s in wg if row.split()[3] in s]
            #making a list of queries for each individual word
            query = ""
            #if row.split()[5] == 'ORG' or row.split()[5] == 'NAT' or row.split()[5] == 'CIT' or row.split()[5] == 'ENT' or row.split()[5] ==  'COU' or row.split()[5] == 'SPO' or row.split()[5] == 'ANI':   
            if len(row.split()) > 4:
                for j in groupedwords:
                    if row.split()[3] in j:
                        query = j
                    else:
                        query = row.split()[3]
              

                    
            if l[n][1] != "": 
                columns = row.split()
                columns.append(l[n][1])
            #if collumn needs wiki link add it, otherwise write as is.
                if x:
                    try:
                        columns.append(wikilinker(query))
                        testfile.write(" ".join(columns))
                        testfile.write("\n")
                        n += 1
                    except TypeError as t:
                        pass
                else:
                    testfile.write(" ".join(columns))
                    testfile.write("\n")
                    n += 1

            else:
                columns = row.split()
                testfile.write(" ".join(columns))
                testfile.write("\n")
                n += 1
            
main()
