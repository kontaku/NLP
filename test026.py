#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	for line in sys.stdin.xreadlines():
		sp_line = line.strip().split()
		ness_ly = re.compile(r'.+(ly$|ness$)').match(sp_line[1])
		if ness_ly != None:
			print line,
