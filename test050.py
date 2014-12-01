#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab
from collections import Counter,defaultdict
from test041 import Mor_Ana
from test042 import verb_list
from test047 import command_options
import matplotlib.pyplot as plt

"""
python test050.py -a
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
		map_lists.append(Mor_Ana(text.strip()))
	#--------------------------------------------------
	d = verb_list(map_lists)
	for verb in d['verb']:
		print verb,tf[verb]
		default_d[verb] = tf[verb]
	print 'sorted'
	i = 1
	fig = plt.figure()
	ax = fig.add_subplot(111)
	for w, c in sorted(default_d.iteritems(), key=lambda x: x[1], reverse=True):
		print w, c ,i
		plt.plot(i,c,'o')
		i += 1	
	plt.title('title')
	plt.ylabel('hindo')
	plt.xlabel('jyuni')
	ax.set_xlim(0, 500)
	ax.set_ylim(0, 150)
	plt.show()

	