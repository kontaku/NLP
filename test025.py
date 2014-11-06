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
					print '%s\t%s' %(kigou[0][i],kigou[0][i].lower())
					f1.write('%s\t%s\n' %(kigou[0][i],kigou[0][i].lower())) 
			else:
				print '%s\t%s' %(term,term.lower())
				f1.write('%s\t%s\n' %(term,term.lower()))
		print 
	f1.close()
