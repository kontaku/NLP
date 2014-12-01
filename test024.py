#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

"""
cat medline.txt.sent | python test024.py
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
							print kakko[0][i]
							f1.write(kakko[0][i]+'\n')
					else:
						print kigou[0][i]
						f1.write(kigou[0][i]+'\n')
			else:
				print term
				f1.write(term+'\n')
		print
		f1.write('\n')
	f1.close()
