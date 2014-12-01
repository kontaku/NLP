#!/usr/bin/python
#-*- coding: utf-8 -*-

import kyotocabinet as kc
from test039 import KyotoCabinet
import re

"""
python test040.py
"""

if __name__ == '__main__':
	db = KyotoCabinet()
	db.open("sample.kch", kc.DB.OWRITER | kc.DB.OCREATE)
	
	var = raw_input("prease input text >")
	p = re.compile('\s')
	var_list = p.split(var)
	L = len(var_list)
	occ_prob = 1
	for i in xrange(L-1):
		bigram = '%s\t%s'%(var_list[i],var_list[i+1])
		print bigram
		try:
			prob = db.get_str(bigram)
			if prob == None:
				prob = 0
			print prob
			occ_prob *= prob

		except Exception as e:
			print 'type:' + str(type(e))
	print 'occurrence probability :%f'%(occ_prob)