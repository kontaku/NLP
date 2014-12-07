#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
python test039.py
"""
import kyotocabinet as kc
from test037 import freq_bigram
from test038 import cnt_1st_terms


class KyotoCabinet(kc.DB):
		def __del__(self):
				self.close()

		def open(self, *args, **kwds):
				if not super(KyotoCabinet, self).open(*args, **kwds):
						raise IOError("Open error: {0}".format(super(KyotoCabinet, self).error()))

		def set(self, *args, **kwds):
				if not super(KyotoCabinet, self).set(*args, **kwds):
						raise IOError("Set error: {0}".format(super(KyotoCabinet, self).error()))

		def close(self, *args, **kwds):
				if not super(KyotoCabinet, self).close(*args, **kwds):
						raise IOError("Close error: {0}".format(super(KyotoCabinet, self).error()))

		def cursor(self, *args, **kwds):
				cur = super(KyotoCabinet, self).cursor(*args, **kwds)
				cur.jump()
				while 1:
						rec = cur.get_str(True)
						if not rec: break
						yield rec
				cur.disable()

if __name__ == '__main__':
	db = KyotoCabinet()
	db.open("sample.kch", kc.DB.OWRITER | kc.DB.OCREATE)
	f1 = open('medline.txt.sent.tok','r')
	terms = f1.readlines()
	lines = freq_bigram(terms)
	dictA = cnt_1st_terms(lines)
	for line in lines:
		first_term = line[0].strip().split('\t')[0]
		cp = float(line[1])/dictA[first_term]
		print '%f\t%s'%(cp,line[0])
		db.set(line[0],cp)
	
	for rec in db.cursor():
		print rec[0],rec[1]
	