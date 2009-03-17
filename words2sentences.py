#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

# Programa que separa les lletres d'una paraula amb espais

#sys.setdefaultencoding('utf-8');

import sys;
from nltk.tokenize.regexp import regexp_tokenize;

from sys import stdin;
from sys import stderr;

from codecs import getreader;
from codecs import getwriter;

stdin  = getreader('utf-8')(stdin);
sys.stdout = getwriter('utf-8')(sys.stdout);
stderr = getwriter('utf-8')(stderr);

s = stdin.read();
tokens = regexp_tokenize(s,'\w+|\$[\d\.]+');

for token in tokens:
    print " ".join(regexp_tokenize(token,'\w')) + '.';
