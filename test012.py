#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

if __name__== '__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		if line.endswith(u'なう'):
			print line
