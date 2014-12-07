#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab
from collections import Counter,defaultdict
from test041 import Mor_Ana
from test042 import verb_list
from test043 import verb_base_list
from test047 import command_options
from test048 import tf
import matplotlib.pyplot as plt
"""
python test049.py -a
"""

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	texts = f1.readlines()
	f1.close() 
	tf = tf(texts)
	parser,options,args = command_options()
	map_lists = []
	default_d = defaultdict(int)
	tagger = MeCab.Tagger()
	dicA = {}
	dicB = {}
	for text in texts:
		map_lists.append(Mor_Ana(text.strip()))
	#--------------------------------------------------
	d = verb_list(map_lists)
	for verb in d['verb']:
		print verb,tf[verb]
		default_d[verb] = tf[verb]
	#--------------------------------------------------	
	print 'sorted'
	for w, c in sorted(default_d.iteritems(), key=lambda x: x[1], reverse=True):
		print w, c
		node = tagger.parse(w).split('\t')[1].split(',')[6]
		try:
			dicA[node] += c 	
			dicB[node] += 1
		except KeyError:
			dicA[node] = c 	
			dicB[node] = 1
	fig = plt.figure()
	ax = fig.add_subplot(111)
	for key in dicA.keys():
		print key
		print dicA[key]
		print dicB[key]
		plt.bar(dicA[key],dicB[key])
	plt.title('title')
	plt.ylabel('kotonari')
	plt.xlabel('hindo')
	ax.set_xlim(0, 150)
	ax.set_ylim(0, 10)
	plt.savefig("plt_result49.eps")
	plt.show()