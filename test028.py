#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re
import test010 as t10

def sep_col(listA):
	listB = []
	for line in listA:
		sep_line = line.strip().split()
		listB.append(sep_line[1])
	return listB

def sep_bi(listA):
	listB = []
	for line in listA:
		L = len(line)
		uline = line.decode('utf8')
		for i in xrange(L-1):
			try:
				bigram = uline[i] + uline[i+1]
				listB.append(bigram)
			except:
				continue
	return listB		 

if __name__== '__main__':
	md_line = sys.stdin.xreadlines()
	sep_md_line = sep_col(md_line)
	sep_bi_md_line = sep_bi(sep_md_line)
	freq_md_line = t10.freq_sort(sep_bi_md_line)
	i=0
	for line in freq_md_line:
		print '%s\t%s'%(line[0].strip('\n').encode('utf8'),str(line[1]).encode('utf8'))
		i+=1
		if i >= 100:
			break
