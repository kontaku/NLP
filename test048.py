#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab
from collections import Counter,defaultdict
from test041 import Mor_Ana
from test042 import verb_list
from test043 import verb_base_list
from test044 import sahen
from test047 import command_options
"""
python test048.py -a
"""

def tf(texts):
	tagger = MeCab.Tagger()
	counter = Counter()
	for text in texts:
		node = tagger.parseToNode(text.strip())
		while node:
			word = node.surface
			counter[word] += 1
			node = node.next
	return counter


if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	texts = f1.readlines()
	f1.close() 
	tf = tf(texts)
	parser,options,args = command_options()
	map_lists = []
	default_d = defaultdict(int)
	for text in texts:
		if options.verb == 1 or options.verb_base == 1 or options.sahen_noun == 1:
			map_lists.append(Mor_Ana(text.strip()))
	#--------------------------------------------------
	if options.verb == 1 :
		d = verb_list(map_lists)
		for verb in d['verb']:
			print verb,tf[verb]
			default_d[verb] = tf[verb]
	#--------------------------------------------------
	if options.verb_base == 1 :
		d = verb_base_list(map_lists)
		for verbb in d['verb_base']:
			print verbb,tf[verbb]
	#--------------------------------------------------
	if options.sahen_noun == 1 :
		d = sahen(map_lists)
		for noun in d['noun']:
			print noun,tf[noun]
	#--------------------------------------------------
	print 'sorted'
	for w, c in sorted(default_d.iteritems(), key=lambda x: x[1], reverse=True):
		print w, c	
	

	