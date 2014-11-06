#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__== '__main__':
	for line in sys.stdin.xreadlines():
		line = line.strip().decode('utf8')
		yubin = re.compile(ur'[0-9]{3}-[0-9]{4}').findall(line)
		ken = re.compile(ur'[一-龠]{2,3}[都|道|府|県]').findall(line)
		si = re.compile(ur'([一-龠]{2,3}[都|道|府|県])(.{1,}[市|町|村])').findall(line)
		if len(ken)!=0 and len(yubin)!=0 and len(si)!=0:
			print '%s\t%s\t%s'%(yubin[0].encode('utf8'),ken[0].encode('utf8'),si[0][1].encode('utf8'))
			
			
	
