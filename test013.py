#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

if __name__=='__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		if line.find('RT @') !=-1:
			retweet=line.split('RT @')[0]
			print retweet
			
