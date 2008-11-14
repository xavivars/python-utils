#!/usr/bin/python

import sys

# comprovem el parametre
if len(sys.argv)<2:
	print >> sys.stderr, "ERROR: Cal utilitzar un fitxer."

# carreguem el diccionari correcte en memoria
dicc = {}
f = open(sys.argv[1], 'r')

for line in f.readlines():	
	dicc[line]=1


# llegim i comprovem l'entrada estandar
for linea in sys.stdin:
	if not dicc.has_key(linea):
		print linea;

	
