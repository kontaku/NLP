#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

def arg():
	try:
		n=raw_input('please input row number:')
		int(n)
	except:
		n=arg()
	return n 


if __name__=='__main__':
	N=int(arg())
	f1 = open('address.txt','r')
	L=f1.readlines()
	i=0
	for line in L:
		if len(L)-N>i:
			i+=1
			continue
		else:
			print line
	f1.close()
	
