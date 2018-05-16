#!/usr/bin/env python3

import os
from nltk import pos_tag, word_tokenize


def main():
    for folder in os.listdir("/home/thomas/projectta/week4/data/"):
        for folder2 in os.listdir("/home/thomas/projectta/week4/data/" + folder):
            path = "/home/thomas/projectta/week4/data/" + folder + "/" + folder2 + "/"
            posfile = open(path + "en.tok.off.pos", "w+")
            with open(path + "en.tok.off", "r") as myfile:
                for line in myfile:
                    columns = line.split()
                    if len(columns) > 1:
                                                columns.append(pos_tag(word_tokenize(columns[3]))[0][1])
                        posfile.write(" ".join(columns))
                        posfile.write("\n")

if __name__ == "__main__":
    main()
