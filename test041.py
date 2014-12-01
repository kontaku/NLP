#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab

"""
python test041.py
"""

def Mor_Ana(line):
	tagger = MeCab.Tagger()
	nodes = tagger.parse(line)
	nodes = nodes.split('\n')
	listA = []
	for node in nodes:
		if node == 'EOS' or node == '':
			continue
		else:
			node_surface,node_attrs = node.split('\t')
			node_attr = node_attrs.split(',')
			base,pos,pos1 = node_attr[6],node_attr[0],node_attr[1]
			#print node_surface,base,pos,pos1
			dicA = {'surface':node_surface,\
					'base':base,\
					'pos':pos,\
					'pos1':pos1}
			listA.append(dicA)
	return listA

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	map_lists = []
	for line in f1.readlines():
		map_lists.append(Mor_Ana(line.strip())) 
	f1.close()
	