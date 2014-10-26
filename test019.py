#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

if __name__=='__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		yubin = re.compile(ur'[0-9]{3}-[0-9]{4}').findall(line)
		ken = re.compile(ur'.{2,3}[都|道|府|県]').findall(line)
		si = re.compile(ur'(.{2,3}[都|道|府|県])(.{1,}[市|町|村])').findall(line)
		if len(ken)!=0 and yubin!=0 and len(si)!=0:
			print yubin[0]+'\t'+ken[0]+'\t'+si[0][1]
			
			
	
