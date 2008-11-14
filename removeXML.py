#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

a = sys.stdin.read();

# etiquetes normals
#a = re.sub("< */? *\w+ */?\ *>", "", a);

# etiquetes amb namespaces
#a = re.sub("< */? *\w+[:|\w]* */?\ *>", "", a);

# etiquetes amb namespaces i atributs normals
a = re.sub("< */? *\w+[:|\w]* *[\w+=\"\w+\" *]* */?\ *>", "", a);

# etiquetes amb namespaces i atributs amb namespace (no funciona bé)
#a = re.sub("< */? *\w+[:|\w]* *[\w+[:|\w]*=\"\w+\" *]* */?\ *>", "", a);

print a
