import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet as wn
import wikipedia
from nltk.tag import StanfordNERTagger


def main():
#open and read the file, make a list of all nouns
    st = StanfordNERTagger('/home/s3494888/Desktop/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/s3494888/Desktop/stanford-ner-2018-02-27/stanford-ner.jar')
    path = "/home/s3494888/Desktop/projecttextanalyse/eindproject/testdir/p12/d0535"
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
    for syn in synlist:
        if not syn:
            try:
                wikipedia.summary(rawlist[synlist.index(syn)], sentences=1)
            except:
                pass
        else:
            pass

    print(synlist)


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





    print(groupedwords)   

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


    print(list(set(wordlist)))
    for line in testfile:
        line = line.split()
        for word in wordlist:
            if line[3] == word[0]:
                line.append(word[0])
    print(testfile)

main()

