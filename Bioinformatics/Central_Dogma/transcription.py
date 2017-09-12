#!/usr/bin/env python
# encoding: utf-8
"""
rosalind_2.py

Created by Heather Underwood on 2014-12-18.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from collections import defaultdict

#Transcribes DNA into RNA
RNA = ""
file_name = list(sys.argv)
text_file = open(file_name[1])
DNA = text_file.read()
for char in DNA:
	if char == 'T':
		RNA += 'U'
	else:
		RNA += char

rna_file = open("rna_file", "w+")
rna_file.write(RNA)
rna_file.close()
	
		
		
		
		



