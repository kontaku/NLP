#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test053.py
"""
import CaboCha,re

def syntactic_analysis(sentence):
	cabocha = CaboCha.Parser()
	tree = cabocha.parse(sentence)
	return tree.toString(CaboCha.FORMAT_LATTICE)


class Chunk:
	def __init__(self, id, morphs, dst, srcs):
		self.id = id
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs
	
	def showinfo(self):
		print  '[dst, srcs] = [%s, %s]' %( self.dst, self.srcs)
	
	def show_phr(self):
		print '[id, chunk] = [%d, %s]' %(self.id,self.morphs,)

def sep_phr(lattice):
	phrs = lattice.split('* ')
	dictA = {}
	dictB = {}
	L = len (phrs)
	for i in xrange(1,L):
		lines = phrs[i].split('\n')
		l = len(lines)
		phr_attr = lines[0].split(' ',2)
		phr_id = int(phr_attr[0])

		dictA[phr_id] = phr_attr[1].replace('D','')
		nodes = ''
		for i in xrange(1,l):
			if lines[i].find('EOS') >= 0 or lines[i] == '':
				continue
			else:
				node = lines[i].split('\t')[0]
				nodes += node
		dictB[phr_id] = nodes
	chunks = []
	for i in xrange(L-1):
		keys = []
		for key in dictA.keys():
			if int(dictA[key]) == i:
				keys.append(key)
		chunk = Chunk(i,dictB[i],dictA[i],keys)
		chunks.append(chunk)
	return chunks

def main():
	f1 = open('japanese.txt','r')
	phr_lines = []
	for sentence in f1.xreadlines():
		lattice = syntactic_analysis(sentence)
		phr_lines.append(sep_phr(lattice))
	return phr_lines
	
			
if __name__ == '__main__':
	phr_lines = main()
	for phr_line in phr_lines:
		for phr in phr_line:
			phr.show_phr()
			phr.showinfo()
		print 
