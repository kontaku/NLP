#!/usr/bin/python
#-*-coding;utf-8-*-

import sys


if __name__=='__main__':
	f1 = open('address.txt','r')
	list=[]
	for line in f1:
		list.append(line.strip('\n').split('\t'))
		
	list.sort(key=lambda X:X[1])
	for L in list:
		print L[0]+'\t'+L[1]
	f1.close()
