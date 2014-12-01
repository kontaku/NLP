#!/usr/bin/python
#-*- coding: utf-8 -*-

import MeCab
from optparse import OptionParser
from test041 import Mor_Ana
from test042 import verb_list
from test043 import verb_base_list
from test044 import sahen
from test045 import AnoB
from test046 import noun_compounds

"""
python test047.py -a -d
"""


def command_options():
	""" コマンドエラー時に表示する文字列 """
	usage = u'%prog [Args] [Options]\nDetailed options -h or --help'
	 
	version = 0.1
	parser = OptionParser(usage=usage, version=version)
	 
	parser.add_option(
		'-a', '--verb',
		action = 'store_true',
		help = 'extract verb'  
	)
	parser.add_option(
		'-b', '--verb_base',
		action = 'store_true',
		help = 'extract verb_base'  
	)
	parser.add_option(
		'-c', '--sahen_noun',
		action = 'store_true',
		help = 'extract sahen_noun'  
	)
	parser.add_option(
		'-d', '--AnoB',
		action = 'store_true',
		help = 'extract AnoB'  
	)
	parser.add_option(
		'-e', '--nouns',
		action = 'store_true',
		help = 'extract nouns'  
	)
	""" 各オプションのデフォルト値をセット """
	parser.set_defaults(
		default = False
	)
	""" オプションをパース """
	options, args = parser.parse_args()
	return parser,options,args



if __name__ == '__main__':
	parser,options,args = command_options()
	f1 = open('japanese.txt','r')
	map_lists = []
	texts = f1.readlines()
	for text in texts:
		if options.verb == 1 or options.verb_base == 1 or options.sahen_noun == 1:
			map_lists.append(Mor_Ana(text.strip()))
	#--------------------------------------------------
	if options.verb == 1 :
		d = verb_list(map_lists)
		for verb in d['verb']:
			print verb
	#--------------------------------------------------
	if options.verb_base == 1 :
		d = verb_base_list(map_lists)
		for verbb in d['verb_base']:
			print verbb
	#--------------------------------------------------
	if options.sahen_noun == 1 :
		d = sahen(map_lists)
		for noun in d['noun']:
			print noun	
	#--------------------------------------------------
	if options.AnoB == 1:
		for text in texts:
			AnoB(text.strip())
	#--------------------------------------------------
	if options.nouns == 1:
		for text in texts:
			noun_compounds(text.strip())	
		
	f1.close() 

	