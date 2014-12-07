#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test036.py
"""
import sys

def sep_col(line):
	line = line.strip().split('\t')[0]
	return line

def createBigram(terms):
	ListA = []
	for i in xrange(len(terms)-1):
		j=i+1
		ListA.append('%s\t%s' %(sep_col(terms[i]),sep_col(terms[j])))
	return ListA

if __name__ == '__main__':
	f1 = open('medline.txt.sent.tok','r')
	terms = f1.readlines()
	bigrams = createBigram(terms)
	for bigram in bigrams:
		print bigram