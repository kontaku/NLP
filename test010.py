#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import Counter

if __name__=='__main__':
	f1 = open('col2.txt','r')
	counter = Counter(f1.readlines())
	list = sorted(counter.most_common(),key=lambda x:x[1],reverse = True)
	for L in list:
		print L[0].strip('\n')+'\t'+str(L[1])
	f1.close()
