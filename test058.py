#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test057.py
"""
from test053 import *
from collections import defaultdict


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
		if len (srcs) > 1:
			print 'chunk:%s,\tsrcs:%s'%(chunk,srcs_chunk)

if __name__ == '__main__':
	phr_lines = main()
	for phr_line in phr_lines:
		dependency_parsing(phr_line)
		
		
		