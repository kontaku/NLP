#!/usr/bin/python
#-*-coding:utf-8-*-

import sys


if __name__== '__main__':
	adrs_list=[]
	for line in sys.stdin.xreadlines():
		adrs_list.append(line.strip('\n').split('\t'))
		
	adrs_list.sort(key=lambda X:X[1])
	for L in adrs_list:
		print '%s\t%s'%(L[0],L[1])
