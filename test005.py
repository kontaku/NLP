#!/usr/bin/python
#-*-coding:utf-8-*-

#$ python test005.py
import sys

def arg2(L):
	try:
		n=raw_input('please input the number of lines:')
		int(n)
	except:
		n=arg2(L)
	if int(n)<L:
		return n
	else:
		print 'this text has %d lines.'\
			'please try again.' %(L.encode('utf8'))
		n=arg2(L)
		return n


if __name__=='__main__':
	txt=raw_input('please input text:')
	f1 = open(txt,'r')
	txt_list=f1.readlines()
	L=len(txt_list)
	N=int(arg2(L))
	for i in xrange(N):
		print txt_list[i].encode('utf8'),
	f1.close()
	
