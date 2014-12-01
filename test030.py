#!/usr/bin/python
#-*- coding: utf-8 -*-

from stemming.porter2 import stem
import sys

"""
cat medline.txt.sent.tok | python test030.py
"""

if __name__== '__main__':
	f1 = open('medline.txt.sent.tok.stem','w')
	for line in sys.stdin.xreadlines():
		col3 = line.strip().split('\t')
		try:
			print '%s\t%s'%(line.strip(),stem(col3[1]))
			f1.write('%s\t%s\n'%(line.strip(),stem(col3[1])))
		except IndexError:
			print 
			f1.write('\n')
	f1.close()
