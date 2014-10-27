#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

if __name__== '__main__':
	
	f1,f2= open('col1.txt','w'),open('col2.txt','w')
	for line in sys.stdin.xreadlines():
		dec_line = line.decode('utf8')
		sep_line = dec_line.split('\t',1)
		f1.write(sep_line[0].encode('utf8')+'\n')
		f2.write(sep_line[1].encode('utf8'))
	f1.close(),f2.close()
	
