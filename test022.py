#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	f1 = open('medline.txt.sent','w')
	for string in sys.stdin.xreadlines():
		string = string.strip()
		paragraph = re.sub(r'\.\s([A-Z])',r'.\n\1',string)
		print paragraph
		f1.write(paragraph)
	
	f1.close()
