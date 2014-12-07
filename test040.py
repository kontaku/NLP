#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test040.py
"""
import kyotocabinet as kc
from test039 import KyotoCabinet
import re

if __name__ == '__main__':
	db = KyotoCabinet()
	db.open("sample.kch", kc.DB.OWRITER | kc.DB.OCREATE)
	
	var = raw_input("prease input text >")
	p = re.compile('\s')
	var_list = p.split(var)
	L = len(var_list)
	occ_prob = float(1)
	for i in xrange(L-1):
		bigram = '%s\t%s'%(var_list[i],var_list[i+1])
		print bigram
		prob = db.get_str(bigram)
		if prob == None:
			prob = float(0)
		print prob
		occ_prob = occ_prob * float(prob)
	print 'occurrence probability :%f'%(occ_prob)