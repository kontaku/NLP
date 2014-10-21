#!/usr/bin/python
#-*-coding;utf-8-*-

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
	for i in range(N):
		print f1.readline()
	f1.close()
	
		
