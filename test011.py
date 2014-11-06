#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

if __name__== '__main__':
	for line in sys.stdin.xreadlines():
		line = line.strip().decode('utf8')
		if u'拡散希望' in line:
			print line.encode('utf8')
