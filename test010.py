#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import Counter


def freq_sort(listA):
	counter = Counter(listA)
	sorted_list = sorted(counter.most_common(),key=lambda x:x[1],reverse = True)
	return sorted_list

if __name__=='__main__':
	f1 = open('col2.txt','r')
	adrs_list = f1.xreadlines()
	adrs_list = freq_sort(adrs_list)
	for L in adrs_list:
		print '%s\t%s'%(L[0].strip('\n').encode('utf8'),str(L[1]).encode('utf8'))
	f1.close()
