#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

"""
cat medline.txt.sent | python test025.py
"""

if __name__== '__main__':
	f1 = open('medline.txt.sent.tok','w')
	for string in sys.stdin.xreadlines():
		for term in string.strip().split():
			kigou = re.compile('(.+[\w])+(\W)').findall(term)
			if len(kigou) != 0:
				for i in xrange(len(kigou[0])):
					kakko = re.compile('(\()(.+[\w])').findall(kigou[0][i])
					if len (kakko) != 0:
						for i in xrange(len(kakko[0])):
							print kakko[0][i],kakko[0][i].lower()
							f1.write('%s\t%s\n'%(kakko[0][i],kakko[0][i].lower()))
					else:
						print kigou[0][i],kigou[0][i].lower()
						f1.write('%s\t%s\n'%(kigou[0][i],kigou[0][i].lower()))
			else:
				print term,term.lower()
				f1.write('%s\t%s\n'%(term,term.lower()))
		print
		f1.write('\n')
	f1.close()
