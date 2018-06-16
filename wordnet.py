import nltk
from nltk.wsd import lesk 
from nltk.corpus import wordnet as wn


def main():
    #st = StanfordNERTagger('/home/s3494888/Desktop/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz', '/home/s3494888/Desktop/stanford-ner-2018-02-27/stanford-ner.jar')
    path = "/home/gijs/projecttextanalyse/eindproject/testdir/p15/d0092"
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

    bigramdeflist = []
    bigramstringlist = []
    for bigram in list(nltk.bigrams(rawlist)):
        bigram_string = '_'.join(bigram)
        bigramstring = ' '.join(bigram)
        bigramstringlist.append(bigramstring)
        dflist = []
        
        #print(bigramstring)
        for syns in wn.synsets(bigram_string):
            dflist.append(syns.definition())
        if not dflist:
            bigramdeflist.append([])
        else:
            bigramdeflist.append(dflist[0])

    synlist = []
    for p in rawlist:
        deflist = []
        emptydef = []
        for syns in wn.synsets(p):
            deflist.append(syns.definition())
        if not deflist:
            synlist.append([])
        else:
            synlist.append(deflist[0])
    emptydef = []


    city = [' city ', ' village ', ' town ']
    country = [' nation ', ' republic ', ' monarchy ']
    sport = [' sport ']
    natural_places = [' desert ', ' volcano ', ' sea ', ' ocean ',  ' lake ', ' river ', ' jungle ', ' waterfall ', ' glacier ', ' mountain ', ' forest ' , ' crater ', ' cave ', ' canyon ', ' fjord ', ' park ', ' bay ', ' valley ', ' cliff ', ' reef ']
    entertainment = [' book ', 'magazine', 'film', 'movie', 'song', 'journal', 'newspaper', 'show', 'band']

    for deflist in synlist:
        if any(x in deflist for x in city):
            print('{0} - CIT'.format(rawlist[synlist.index(deflist)]))
        elif any(x in deflist for x in country):
            print('{0} - COU'.format(rawlist[synlist.index(deflist)]))
        elif any(x in deflist for x in sport):
            print('{0} - SPO'.format(rawlist[synlist.index(deflist)]))
        elif any(x in deflist for x in natural_places):
            print('{0} - NAT'.format(rawlist[synlist.index(deflist)]))
        elif any(x in deflist for x in entertainment):
            print('{0} - ENT'.format(rawlist[synlist.index(deflist)]))

    for bigramdf in bigramdeflist:
        if any(x in bigramdf for x in city):
            print('{0} - CIT'.format(bigramstringlist[bigramdeflist.index(bigramdf)]))
        elif any(x in bigramdf for x in country):
            print('{0} - COU'.format(bigramstringlist[bigramdeflist.index(bigramdf)]))
        elif any(x in bigramdf for x in sport):
            print('{0} - SPO'.format(bigramstringlist[bigramdeflist.index(bigramdf)]))
        elif any(x in bigramdf for x in natural_places):
            print('{0} - NAT'.format(bigramstringlist[bigramdeflist.index(bigramdf)]))
        elif any(x in bigramdf for x in entertainment):
            print('{0} - ENT'.format(bigramstringlist[bigramdeflist.index(bigramdf)]))

main()

