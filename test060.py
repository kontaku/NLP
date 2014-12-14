#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test057.py
"""
from test053 import *
from collections import defaultdict
import MeCab
import pygraphviz as pgv

def dependency_parsing(phr_line):
	TOKENS = re.compile(u'[一-龠ぁ-んァ-ヴA-Za-z0-9\ー]')
	d = defaultdict(list)
	for phr in phr_line:
		morphs = phr.morphs.decode('utf8')
		n = TOKENS.findall(morphs)
		re_morphs = ''.join(n)
		d[phr.id] = re_morphs

	for phr in phr_line:
		chunk = d[int(phr.id)]
		dst = phr.dst
		srcs = phr.srcs
		if int(dst) != -1:
			dst_chunk = d[int(dst)]
		else :
			dst_chunk = ''
		srcs = [d[int(x)] for x in srcs]
		srcs_chunk = '\t'.join(srcs)
		if check_noun(chunk) == 1 and check_verb(dst_chunk) == 1:
			#print 'chunk:%s,\tdst:%s'%(chunk,dst_chunk) 
			f.write('\t"%s" -> "%s" ;\n'%(chunk.encode('utf8'),dst_chunk.encode('utf8')))

def check_noun(line):
	tagger = MeCab.Tagger()
	line = line.encode('utf8')
	node = tagger.parseToNode(line)
	check = 0
	while node:
		if node.posid >= 38 and node.posid <= 60:
			nc = node.surface
			check = 1
		node = node.next
	return check

def check_verb(line):
	tagger = MeCab.Tagger()
	line = line.encode('utf8')
	node = tagger.parseToNode(line)
	check = 0
	while node:
		if node.posid >= 31 and node.posid <= 32:
			nc = node.surface
			check = 1
		node = node.next
	return check

if __name__ == '__main__':
	phr_lines = main()
	f=open("test060.dot", "w")
	f.write('digraph "g" {\n')
	for phr_line in phr_lines:
		dependency_parsing(phr_line)
	f.write('}')
		
		
		