import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet as wn


def main():
#open and read the file, make a list of all nouns
    path = "/home/gijs/projecttextanalyse/eindproject/testdir/p52/d0116"
    testfile = open(path + "/en.tok.off.pos.test", "w+")
    rawlist = []
    with open(path + "/en.tok.off.pos", "r") as posfile:
        f = posfile.readlines()
        for line in f:
            if line.split()[4].startswith('N'):
                rawlist.append(line.split()[3])
            else:
                pass
        rawstring = " ".join(rawlist)

#make a list of every wordnet definition of every word in the raw text list
    synlist = []
    for p in rawlist:
        deflist = []
        for syns in wn.synsets(p):
            deflist.append(syns.definition())
        if not deflist:
            synlist.append([])
        else:
            synlist.append(deflist[0])

#make a list of all bigrams with nltk, then make a list with every wordnet definition of every bigram
    bigramdeflist = []
    for bigram in list(nltk.bigrams(rawlist)):
        bigram_string = '_'.join(bigram)
        dflist = []
        for syns in wn.synsets(bigram_string):
            dflist.append(syns.definition())
        if not dflist:
            bigramdeflist.append([])
        else:
            bigramdeflist.append(dflist[0])

#lists of all words that could appear in the definitions of the unigrams and bigrams
    city = [' city ', ' village ', ' town ', 'capital']
    country = [' nation ', ' republic ', ' monarchy ']
    sport = [' sport ', 'combat', ' game ', 'fight']
    natural_places = [' desert ', ' volcano ', ' sea ', ' ocean ',  ' lake ', ' river ', ' jungle ', ' waterfall ', ' glacier ', ' mountain ', ' forest ' , ' crater ', ' cave ', ' canyon ', ' fjord ', ' park ', ' bay ', ' valley ', ' cliff ', ' reef ']
    entertainment = [' book ', 'magazine', 'film', 'movie', 'song', 'journal', 'newspaper', 'show', 'band']
    animal = ['mammal', 'bird', 'fish', 'amphibian', 'reptil', 'crustacean', 'insect', 'carnivore', 'herbivore', 'species', 'breed', 'cattle', 'quadruped', 'pachyderm', 'feline', 'ungulate']
    person = ['born']
    organization = ['company', 'organization', 'charity', 'movement', 'party', 'enterprise', 'business', 'union']
    
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

    first_item = [x[0] for x in list(nltk.bigrams(rawlist))]
    second_item = [x[1] for x in list(nltk.bigrams(rawlist))]
    for bigramdf in bigramdeflist:
        if any(x in bigramdf for x in city):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'CIT'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'CIT'))
        elif any(x in bigramdf for x in country):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'COU'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'COU'))
        elif any(x in bigramdf for x in sport):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'SPO'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'SPO'))
        elif any(x in bigramdf for x in natural_places):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'NAT'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'NAT'))
        elif any(x in bigramdf for x in entertainment):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'ENT'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'ENT'))
        elif any(x in bigramdf for x in animal):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'ANI'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'ANI'))
        elif any(x in bigramdf for x in organization):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'ORG'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'ORG'))
        elif any(x in bigramdf for x in person):
            wordlist.append((first_item[bigramdeflist.index(bigramdf)], 'PER'))
            wordlist.append((second_item[bigramdeflist.index(bigramdf)], 'PER'))

    print(list(set(wordlist)))
main()

