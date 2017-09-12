#!/usr/bin/env python
# encoding: utf-8
"""
rosalind_3.py

Created by Heather Underwood on 2014-12-18.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from collections import defaultdict

#Returns the reverse complement of a DNA string
RC = ""
file_name = list(sys.argv)
text_file = open(file_name[1])
DNA = text_file.read()
reverse_dna = DNA[::-1]
#print reverse_dna

for char in reverse_dna:
	if char == 'T':
		RC += 'A'
	elif char == 'A':
		RC += 'T'
	elif char == 'G':
		RC += 'C'
	elif char == 'C':
		RC += 'G'

rc = open("rc_file", "w+")
rc.write(RC)
rc.close()
	
		
		
		
		



