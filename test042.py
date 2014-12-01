#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab
from test041 import Mor_Ana 
from collections import defaultdict
"""
python test042.py
"""
def verb_list(lists):
	d = defaultdict(set)
	for listA in lists:
		for dictA in listA:
			if dictA['pos'] == '動詞':
				#print dictA['surface']
				d['verb'].add(dictA['surface'])
	return d

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	map_lists = []
	for line in f1.readlines():
		map_lists.append(Mor_Ana(line.strip())) 		
	d = verb_list(map_lists)
	for verb in d['verb']:
		print verb
	f1.close()