#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test037.py
"""
import sys
from test036 import createBigram
from collections import Counter

def freq_sort(listA):
	counter = Counter(listA)
	sorted_list = sorted(counter.most_common(), key=lambda x:x[1], reverse = True)
	return sorted_list

def freq_bigram(terms):
	bigrams = createBigram(terms)
	s_bigrams = freq_sort(bigrams)
	return s_bigrams

if __name__ == '__main__':
	f1 = open('medline.txt.sent.tok','r')
	terms = f1.readlines()
	lines = freq_bigram(terms)
	for line in lines:
		print '%s\t%s'%(line[1],line[0])