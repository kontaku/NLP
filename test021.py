#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	for string in sys.stdin.xreadlines():
		sep_lines = string.split('.')
		for line in sep_lines:
			print line.decode('utf8') + '.'
		
