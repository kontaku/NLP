#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

if __name__== '__main__':
	for line in sys.stdin.xreadlines():
		print line.replace('\t',' '),
