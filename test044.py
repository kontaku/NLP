#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab
from test041 import Mor_Ana 
from collections import defaultdict

"""
python test044.py
"""

def sahen(lists):
	d = defaultdict(set)
	for listA in lists:
		for dictA in listA:
			if dictA['pos'] == '名詞' and dictA['pos1'] == 'サ変接続':
				#print dictA['surface']
				d['noun'].add(dictA['surface'])
	return d

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	map_lists = []
	for line in f1.readlines():
		map_lists.append(Mor_Ana(line.strip())) 		
	d = sahen(map_lists)
	for noun in d['noun']:
		print noun	
	f1.close()