#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test056.py
"""
from test053 import *
from collections import defaultdict
import MeCab

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
			print 'chunk:%s,\tdst:%s'%(chunk,dst_chunk) 

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
		if node.posid >= 31 and node.posid <= 33:
			nc = node.surface
			check = 1
		node = node.next
	return check

if __name__ == '__main__':
	phr_lines = main()
	for phr_line in phr_lines:
		dependency_parsing(phr_line)
		
		
		