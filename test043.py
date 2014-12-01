#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab
from test041 import Mor_Ana 
from collections import defaultdict

"""
python test043.py
"""
def verb_base_list(lists):
	d = defaultdict(set)
	for listA in lists:
		for dictA in listA:
			if dictA['pos'] == '動詞':
				#print dictA['base']
				d['verb_base'].add(dictA['base'])
	return d

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	map_lists = []
	for line in f1.readlines():
		map_lists.append(Mor_Ana(line.strip())) 		
	d = verb_base_list(map_lists)
	for verbb in d['verb_base']:
		print verbb
	f1.close()