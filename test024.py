#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	f1 = open('medline.txt.sent.tok','w')
	for string in sys.stdin.xreadlines():
		for term in string.strip().split():
			kigou = re.compile('(.+[\w])+(\W)').findall(term)
			if len(kigou) != 0:
				for i in xrange(len(kigou[0])):
					print kigou[0][i] 
			else:
				print term
			#f1.write(term)
		print 
	f1.close()
