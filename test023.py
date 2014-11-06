#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	for string in sys.stdin.xreadlines():
		for term in string.strip().split():
			term = term.rstrip(',').rstrip('.')
			print term
		print 
