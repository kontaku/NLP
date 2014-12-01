#!/usr/bin/python
#-*- coding: utf-8 -*-


import re,sys, marshal

def str2dict(attr):
	listA = []
	taples = re.compile(ur'(\()(.+?)(\))').findall(attr)
	for taple in taples:
		terms = re.compile(ur'(\')(.+?)(\')').findall(taple[1])
		try:
			new_taple = (terms[0][1],terms[1][1],terms[2][1])
			listA.append(new_taple)
		except IndexError:
			pass
		
	return listA

if __name__ == '__main__':
	wordsDict = marshal.load(open('辞書','r'))
	for line in sys.stdin.xreadlines():
		wordset = line.strip().split('\t')
		word = wordset[1]
		try:
			attr = wordsDict[word]
			#attr = str2dict(attr)
			L = len(attr)
			if L < 3:
				continue
			for i in xrange(L):
				print '%s\t%s\t%s\t%s' %(line.strip(),attr[i][0],attr[i][1],attr[i][2])
		except KeyError:
			pass