#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys,re

def human_name(line,keisyou):
	kanji = ur'[一-龠]+'
	hiragana = ur'[ぁ-ん]+'
	katakana = ur'[ァ-ヴ]+'	
	human_name = re.compile(ur'(%s|%s|%s)(%s)' \
				% (kanji,hiragana,katakana,keisyou)). \
				findall(line)	
	if len(human_name)!=0 and len(human_name[0][0]) >=3 and len(human_name[0][0])<=5:
		return human_name[0][0].encode('utf8')+human_name[0][1].encode('utf8')
	

if __name__== '__main__':
	for line in sys.stdin.readlines():
		line = line.strip().decode('utf8')
		keisyou = re.compile(ur'(さん|氏|ちゃん|くん|君|先生|様|殿|たん|きゅん|嬢)').findall(line)
		if len(keisyou)!=0 and human_name(line,keisyou[0]) != None:
				print human_name(line,keisyou[0])
	
