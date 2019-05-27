#!/usr/bin/python3

from collections import Counter
from nltk.metrics import ConfusionMatrix
import os

def main():
    set1  = []
    set2 = []
    set3 = []
    list1 = []
    list2 = []
    list3 = []

    for folder in os.listdir("/home/lennart/school/projectta/projecttextanalyse/week4_vorig_jaar/data/"):
        for folder2 in os.listdir("/home/lennart/school/projectta/projecttextanalyse/week4_vorig_jaar/data/" + folder):
            myfile = open("/home/lennart/school/projectta/projecttextanalyse/week4_vorig_jaar/data/" + folder + "/" + folder2 + "/en.tok.off.pos.len", "r")
            myfile2 = open("/home/lennart/school/projectta/projecttextanalyse/week4_vorig_jaar/data/" + folder + "/" + folder2 + "/en.tok.off.pos.gijs", "r")
            myfile3 = open("/home/lennart/school/projectta/projecttextanalyse/week4_vorig_jaar/data/" + folder + "/" + folder2 + "/en.tok.off.pos.tho", "r")
            for line in myfile:
                columns = line.split()
                if len(columns) < 6:
                    set1.append("NON")
                    list1.append("NO")
                else:
                    set1.append(columns[5])
                    list1.append("YES")
            for line in myfile2:
                columns = line.split()
                if len(columns) < 6:
                    set2.append("NON")
                    list2.append("NO")
                else:
                    set2.append(columns[5])
                    list2.append("YES")
            for line in myfile3:
                columns = line.split()
                if len(columns) < 6:
                    set3.append("NON")
                    list3.append("NO")
                else:
                    set3.append(columns[5])
                    list3.append("YES")

    total = 0
    finds = 0
    agr_find = 0
    #test function for out of range error 
    setlength = len(set1)
    for i in range(len(set1)):
        if set1[i] != "NON" and set2[i] !="NON" and set3[i] != "NON":
            agr_find += 1
            finds += 1
            total += 1
        elif set1[i] != "NON" and set2[i] == "NON" and set3[i] == "NON":
            finds += 1
            total += 1
        elif set1[i] == "NON" and set2[i] != "NON" and set3[i] == "NON":
            finds += 1
            total += 1
        elif set1[i] == "NON" and set2[i] == "NON" and set3[i] != "NON":
            finds += 1
            total += 1
        elif set1[i] != "NON" and set2[i] != "NON" and set3[i] == "NON":
            finds += 1
            total += 1
        elif set1[i] == "NON" and set2[i] != "NON" and set3[i] != "NON":
            finds += 1
            total += 1
        elif set1[i] != "NON" and set2[i] == "NON" and set3[i] != "NON":
            finds += 1
            total += 1
        else:
            total += 1

    print("Total agreed finds: {0}\nTotal finds: {1}\nTotal tokens: {2}\n".format(str(agr_find),str(finds),str(total)))
    print("Lennart vs Gijs")
    two_int(list1, list2)
    print("Lennart vs Thomas")
    two_int(list1, list3)
    print("Gijs vs Thomas")
    two_int(list2, list3)
    print("\n\n")
    print("Lennart vs Gijs")
    two_cla(set1, set2)
    print("Lennart vs Thomas")
    two_cla(set1, set3)
    print("Gijs vs Thomas")
    two_cla(set2, set3)

def two_int(list1, list2):
    matrix = ConfusionMatrix(list1, list2)
    print(matrix)

    labelSet = set(list1 + list2)

    true_positives = Counter()
    false_negatives = Counter()
    false_positives = Counter()

    for i in labelSet:
        for j in labelSet:
            if i == j:
                true_positives[i] += matrix[i,j]
            else:
                false_negatives[i] += matrix[i,j]
                false_positives[j] += matrix[i,j]

    print("TP:", sum(true_positives.values()), true_positives)
    print("FN:", sum(false_negatives.values()), false_negatives)
    print("FP:", sum(false_positives.values()), false_positives)
    print()

    for i in sorted(labelSet):
        if true_positives[i] == 0:
            fscore = 0
        else:
            precision = true_positives[i] / float(true_positives[i]+false_positives[i])
            recall = true_positives[i] / float(true_positives[i]+false_negatives[i])
            fscore = 2 * (precision * recall) / float(precision + recall)
        print("fscore")
        print(i, fscore)


def two_cla(set1, set2):
    matrix = ConfusionMatrix(set1, set2)
    print(matrix)

    labelSet = set(set1 + set2)

    true_positives = Counter()
    false_negatives = Counter()
    false_positives = Counter()

    for i in labelSet:
        for j in labelSet:
            if i == j:
                true_positives[i] += matrix[i,j]
            else:
                false_negatives[i] += matrix[i,j]
                false_positives[j] += matrix[i,j]

    print("TP:", sum(true_positives.values()), true_positives)
    print("FN:", sum(false_negatives.values()), false_negatives)
    print("FP:", sum(false_positives.values()), false_positives)
    print()

    for i in sorted(labelSet):
        if true_positives[i] == 0:
            fscore = 0
        else:
            precision = true_positives[i] / float(true_positives[i]+false_positives[i])
            recall = true_positives[i] / float(true_positives[i]+false_negatives[i])
            fscore = 2 * (precision * recall) / float(precision + recall)
        print(i, fscore)



if __name__ == "__main__":
    main()
