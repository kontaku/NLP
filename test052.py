#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test052.py
"""
import CaboCha,re

def syntactic_analysis(sentence):
	cabocha = CaboCha.Parser()
	tree = cabocha.parse(sentence)
	return tree.toString(CaboCha.FORMAT_LATTICE)


class Morph:
	def __init__(self,surface,base,pos,pos1):
		self.surface=surface
		self.base=base
		self.pos=pos
		self.pos1=pos1
	
	def showinfo(self):
		print  '[%s, %s, %s, %s]' %(self.surface, self.base, self.pos, self.pos1)

def sep_attr(lattice):
	lattice = lattice.split('\n')
	morphs = []
	for nodes in lattice:
		if nodes.find('EOS') >= 0 or nodes.startswith('* ') == 1 or nodes == '':
			continue
		else:
			node = re.split('\t|,',nodes)
			print '%s\t%s\t%s\t%s'%(node[0],node[7],node[1],node[2])
			morph = Morph(node[0],node[7],node[1],node[2])
			morphs.append(morph)
	return morphs

if __name__ == '__main__':
	f1 = open('japanese.txt','r')
	mor_lines = []
	for sentence in f1.xreadlines():
		lattice = syntactic_analysis(sentence)
		mor_lines.append(sep_attr(lattice))

	for mor_line in mor_lines:
		for morph in mor_line:
			morph.showinfo()
		print
