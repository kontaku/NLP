#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__=='__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		ku = re.compile(ur'(仙台市)(.{1,3}区)').findall(line)
		if len(ku)!=0:
			print line
		
	
