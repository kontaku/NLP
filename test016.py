#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	
	for line in sys.stdin.xreadlines():
		line = line.strip().decode('utf8')
		paren = re.compile(ur'([一-龠]+)(\(|（)([A-Z]+)(\)|）)').findall(line)
		if len(paren)!=0:	
			print '括弧の左の漢字:%s'%(paren[0][0].encode('utf8'))
			print '括弧内の大文字アルファベット:%'%(paren[0][2].encode('utf8'))
	
