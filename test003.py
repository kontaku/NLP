#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

if __name__== '__main__':
	
	f1,f2= open('col1.txt','w'),open('col2.txt','w')
	for line in sys.stdin.xreadlines():
		sep_line = line.split('\t',1)
		f1.write(sep_line[0]+'\n')
		f2.write(sep_line[1])
	f1.close(),f2.close()
	
