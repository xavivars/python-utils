#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

# Programa que separa les lletres d'una paraula amb espais

#sys.setdefaultencoding('utf-8');


import sys, codecs, copy;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin);
sys.stdout = codecs.getwriter('utf-8')(sys.stdout);
sys.stderr = codecs.getwriter('utf-8')(sys.stderr);

j=0

# llegim l'entrada estandar
for linea in sys.stdin:
	j=j+1;

	b=linea[0];
	# cal fer-ho fins a len(linea)-1 per a que no tinga
	# en compte el propi final de linia
	for i in range(1,len(linea)-1):
		b+=' '+linea[i];

	# l'encode és necessari perquè python té un bug
	# http://drj11.wordpress.com/2007/05/14/python-how-is-sysstdoutencoding-chosen/#comment-3503
	# print b.encode('utf-8');
	# també es soluciona posant el getwriter del principi
	print b;


