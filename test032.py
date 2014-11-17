#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,marshal
from test031 import CreateDict

if __name__== '__main__':
	f1 = open('辞書','w')
	f2 = open('inflection.table.txt','r')
	dictA = CreateDict(f2)
	dictB = {}
	for key in dictA.keys():
		dictB[key] = str(dictA[key])
	marshal.dump(dictB,f1)
	f2.close()
	f1.close()