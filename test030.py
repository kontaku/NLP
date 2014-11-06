#!/usr/bin/python
#-*- coding: utf-8 -*-

from stemming.porter2 import stem
import sys

if __name__== '__main__':
	f1 = open('medline.txt.sent.tok.stem','w')
	for line in sys.stdin.xreadlines():
		col3 = line.strip().split()
		print '%s\t%s'%(line.strip(),stem(col3[1]))
		f1.write('%s\t%s'%(line.strip(),stem(col3[1])))
	f1.close()
