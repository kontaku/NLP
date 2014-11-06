#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__=='__main__':
	for line in sys.stdin.xreadlines():
		line = line.strip().decode('utf8')
		comment = re.compile(': ([\S]{1,})RT @').findall(line)
		if len(comment) !=0:
			print comment[0].encode('utf8')
