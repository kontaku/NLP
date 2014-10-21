#!/usr/bin/python
#-*-coding;utf-8-*-

import sys


if __name__=='__main__':
	f1 = open('col1.txt','r')
	L=f1.readlines()
	print len(set(L))
	f1.close
