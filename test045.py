#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab

"""
python test045.py
"""

def AnoB(line):
	tagger = MeCab.Tagger()
	node = tagger.parseToNode(line).next
	while node:
		if node.posid >= 38 and node.posid <= 60:
			try:
				n_node = node.next
				if n_node.surface == 'の':
					nn_node = n_node.next
					if nn_node.posid >= 38 and nn_node.posid <= 60:
						print node.surface,n_node.surface,nn_node.surface
			except:
				continue
		node = node.next

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	map_lists = []
	for line in f1.readlines():
		AnoB(line.strip())
	f1.close() 

	