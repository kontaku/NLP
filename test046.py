#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab

"""
python test046.py
"""

def noun_compounds(line):
	tagger = MeCab.Tagger()
	node = tagger.parseToNode(line).next
	print line
	while node:
		if node.posid >= 38 and node.posid <= 60:
			nc = node.surface
			while node.next.posid >= 38 and node.next.posid <= 60:
				nc += node.next.surface
				node = node.next
			print nc
		node = node.next

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	map_lists = []
	for line in f1.readlines():
		noun_compounds(line.strip())
	f1.close() 

	