#!/usr/bin/python3
#exercise1

import nltk
from nltk.corpus import wordnet as wn

def ex1_1():
	relative = wn.synset('relative.n.01')
	illness = wn.synset('illness.n.01')
	science = wn.synset('science.n.01')
	print(relative.hyponyms())
	print(illness.hyponyms())
	print(science.hyponyms())

def ex1_3():
	car = wn.synset('car.n.01')
	automobile = wn.synset('automobile.n.01')
	coast = wn.synset('coast.n.01')
	shore = wn.synset('shore.n.01')
	food = wn.synset('food.n.01')
	fruit = wn.synset('fruit.n.01')
	journey = wn.synset('journey.n.01')
	monk = wn.synset('monk.n.01')
	slave = wn.synset('slave.n.01')
	moon = wn.synset('moon.n.01')
	string = wn.synset('string.n.01')
	print(car.path_similarity(automobile))
	print(coast.path_similarity(shore))
	print(food.path_similarity(fruit))
	print(journey.path_similarity(car))
	print(monk.path_similarity(slave))
	print(moon.path_similarity(string))

def main():
	ex1_1()
	ex1_3()

if __name__ == "__main__":
	main()


