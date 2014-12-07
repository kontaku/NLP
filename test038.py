#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
python test038.py
"""
import sys
from test037 import freq_bigram


def cnt_1st_terms(listA):
	dictA = {}
	for line in listA:
		first_term = line[0].strip().split('\t')[0]
		if first_term in dictA:
			dictA[first_term] = line[1] + dictA[first_term] 
		else:
			dictA[first_term] = line[1]
	return dictA

if __name__ == '__main__':
	f1 = open('medline.txt.sent.tok','r')
	terms = f1.readlines()
	lines = freq_bigram(terms)
	dictA = cnt_1st_terms(lines)
	for line in lines:
		first_term = line[0].strip().split('\t')[0]
		print '%f\t%s'%(float(line[1])/dictA[first_term],line[0])