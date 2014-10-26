#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__=='__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		u_name = re.compile('@\w*\s').findall(line)
		if len(u_name)!=0:
			print u_name[0]
		
