#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__=='__main__':
	
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		paren = re.compile(ur'([一-龠]+)(\(|（)([A-Z]+)(\)|）)').findall(line)
		if len(paren)!=0:	
			print paren[0][0]
			print paren[0][2]
	
