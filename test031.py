#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from collections import defaultdict

def CreateList(line):
	spt_line = line.split('|')
	tapleA = (spt_line[1],spt_line[3],spt_line[6])
	return spt_line[0],tapleA

def CreateDict(f1):
	alt = defaultdict(list)
	for line in f1.xreadlines():
		keyA,valueA = CreateList(line.strip())
		alt[keyA].append(valueA)
	return alt

if __name__== '__main__':
	f1 = open('inflection.table.txt','r')
	dictA = CreateDict(f1)
	query=raw_input('please input word:')
	try:
		attr = dictA[query]
		L = len(attr)
		for i in xrange(L):
			print 'POS:%s,infected form:%s,basic form:%s'% (attr[i][0],attr[i][1],attr[i][2])	
	except KeyError:
		print "The text don't have the word"
	f1.close()