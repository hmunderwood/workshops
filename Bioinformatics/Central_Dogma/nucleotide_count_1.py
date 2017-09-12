#!/usr/bin/env python
# encoding: utf-8
"""
Created by Heather Underwood on 2016-11-30.
Copyright (c) 2016 __MyCompanyName__. All rights reserved.
"""

import sys
import os

dna = "agggtcctctctctgagagatctcgatc"

a_count = 0
g_count = 0
c_count = 0
t_count = 0

for bp in dna:
    if bp == 'a':
        a_count += 1
    elif bp == 'g':
        g_count += 1
    elif bp == 't':
        t_count += 1
    elif bp == 'c':
        c_count += 1


print "a:" + str(a_count)
print "g:" + str(g_count)
print "t:" + str(t_count)
print "c:" + str(c_count)
