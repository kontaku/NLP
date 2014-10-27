#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

def replacehref(usr):
	user=usr.strip('@')
	HTML='<a href = "https://twitter.com/#!/%s">%s</a>' \
	% (user,usr)
	return HTML.encode('utf8')

if __name__== '__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		u_name = re.compile('@\w*\s').findall(line)
		if len(u_name)!=0:	
			print replacehref(u_name[0].strip())
		
