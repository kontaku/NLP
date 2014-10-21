# -*- coding: utf-8 -*-
import sys
import csv

if __name__=='__main__':
	D = set()
	for row in csv.reader(sys.stdin):
		s1 = ''.join((row[6].decode('sjis'), row[7].decode('sjis')))
		s2 = row[8].decode('sjis')
		if s2 == u'以下に掲載がない場合':
			continue
		s2s = s2.split(u'、')
		for s in s2s:
			p = s.find(u'（')
			if p != -1:
				s = s[:p]
			D.add((s1, s))
	f = open('address.txt','w')
	for s1, s2 in D:
		print '\t'.join((s1, s2))
		en_s1=s1.encode('utf8')
		en_s2=s2.encode('utf8')
		
		f.write('\t'.join((en_s1,en_s2))+'\n')
	
	f.close

	

