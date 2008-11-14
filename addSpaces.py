#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programa que separa les lletres d'una paraula amb espais

import sys
import codecs

# indiquem la codifiacio de stdin
sys.stdin = codecs.getreader("utf-8")(sys.stdin)

# llegim l'entrada estandar
for linea in sys.stdin:
	b=linea[0];
	# cal fer-ho fins a len(linea)-1 per a que no tinga
	# en compte el propi final de linia
	for i in range(1,len(linea)-1):
		b+=' '+linea[i];
	print b;

