#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test051.py
"""
import CaboCha

def syntactic_analysis(sentence):
	cabocha = CaboCha.Parser()
	tree = cabocha.parse(sentence)
	return tree.toString(CaboCha.FORMAT_LATTICE)


if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	for sentence in f1.xreadlines():
		print syntactic_analysis(sentence)
		print