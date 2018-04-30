import nltk
from nltk.corpus import brown
from collections import Counter

def main():
    br_tw = nltk.corpus.brown.tagged_words(categories='adventure')
    br_sw = nltk.corpus.brown.tagged_words(categories='adventure', tagset='universal')
    br_ts = nltk.corpus.brown.tagged_sents(categories='adventure')
    tag_fd = nltk.FreqDist(tag for (word, tag) in br_tw)
    tag_dd = nltk.FreqDist(word for (word, tag) in br_tw)
    adv = [word for word,pos in br_sw if pos == 'ADV']
    adv_fd = Counter(adv)
    adj = [word for word,pos in br_sw if pos == 'ADJ']
    adj_fd = Counter(adj)

    print(len(br_tw)) #a
    print(len(br_ts)) 
    print(br_tw[50]) #b
    print(br_tw[75])
    print(len(tag_fd.most_common())) #c
    print(tag_dd.most_common()[:15]) #d
    print(tag_fd.most_common()[:15]) #e
    print(adv_fd.most_common(1)) #g
    print(adj_fd.most_common(1)) #h

    

main()
