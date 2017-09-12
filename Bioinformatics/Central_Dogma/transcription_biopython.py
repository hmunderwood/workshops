#!/usr/bin/env python
# encoding: utf-8
"""
rosalind_2.py

Created by Heather Underwood on 2014-12-18.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

#Transcribes DNA into RNA
file_name = list(sys.argv)
text_file = open(file_name[1])
DNA = text_file.read()

my_seq = Seq(DNA, IUPAC.unambiguous_dna)
print my_seq.transcribe()

