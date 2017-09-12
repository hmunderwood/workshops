#!/usr/bin/env python
# encoding: utf-8
"""
rosalind_1.py

Created by Heather Underwood on 2014-12-18.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from collections import defaultdict

groups = defaultdict(int)
file_name = list(sys.argv)
text_file = open(file_name[1])
inp = text_file.read()
for char in inp:
	print groups[char]
	groups[char] += 1

x = str(groups['A']) + ' ' + str(groups['C']) + ' ' + str(groups['G']) + ' ' + str(groups['T'])
print x
	
		
		
		
		



