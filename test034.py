#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys, marshal

if __name__ == '__main__':
	wordsDict = marshal.load(open('辞書','r'))
	for line in sys.stdin.xreadlines():
		wordset = line.strip().split('\t')
		word = wordset[1]
		try:
			attr = wordsDict[word]
		except KeyError:
			print word