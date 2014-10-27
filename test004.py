#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

if __name__== '__main__':
	f1,f2= open('col1.txt','r'),open('col2.txt','r')
	for i in xrange(len(sys.stdin.readlines())):
		line='%s\t%s' %(f1.readline().rstrip('\n'),f2.readline().rstrip('\n'))
		print line
	f1.close(),f2.close()
		
