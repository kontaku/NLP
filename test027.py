#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re
import test010 as t10

def sep_col(listA):
	listB=[]
	for line in listA:
		sep_line = line.strip().split()
		listB.append(sep_line[1])
	return listB


if __name__== '__main__':
	md_line = sys.stdin.xreadlines()
	sep_md_line = sep_col(md_line)
	freq_md_line = t10.freq_sort(sep_md_line)
	i=0
	for line in freq_md_line:
		print '%s\t%s'%(line[0].strip('\n').encode('utf8'),str(line[1]).encode('utf8'))
		i+=1
		if i >= 100:
			break
