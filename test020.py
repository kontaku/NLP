#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		paren = re.compile(ur'([\(|（])(.+?)([\)|）])').findall(line)
		if len(paren)!=0:		
			kao_attr = re.compile(ur'[*゜∇∀\^ω][^一-龠^ぁ-ん^ァ-ヴ^0-9^A-Z^a-z\s^?^!^！^？^、^。^〜^\'^;]+').findall(paren[0][1])
			if len(kao_attr) !=0:
				kao=paren[0][0]+paren[0][1]+paren[0][2] 
				if kao.find('http')==-1:
					print kao
				
			
