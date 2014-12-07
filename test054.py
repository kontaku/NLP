#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test054.py
"""
from test053 import *

if __name__ == '__main__':
	phr_lines = main()
	for phr_line in phr_lines:
		for phr in phr_line:
			phr.show_phr()
			phr.showinfo()
		print  
