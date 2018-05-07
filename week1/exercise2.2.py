#!/usr/bin/python3
# file name: exercise2.py
# author: group 3

import nltk

def main():
    path = "holmes.txt"
	f = open(path)
	holmes_raw = f.read()
	f.close()
