#!/usr/bin/env python
# encoding: utf-8
"""
genetic_code.py

Created by Heather Underwood on 2014-12-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import string
from collections import defaultdict

"""
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
"""
#Print the protein strings that can be made from a given RNA sequence

file_name = list(sys.argv)
codon_table_file = open(file_name[1])
codons = codon_table_file.read()
codon_dict = codons.split(' ')

codon_table = defaultdict(str)

rna_file = open(file_name[2])
rna_string = rna_file.read()

for entry in codon_dict:
	temp = entry.split(',')
	codon_table[temp[0]] = temp[1]


protein_string = ""
x = 0

while x < len(rna_string):
	three_bases = rna_string[x:x+3]
	if not(codon_table[three_bases] == 'Stop'):
		protein_string += codon_table[three_bases]
	x += 3

print protein_string

	
	
	
	
	
	
		
