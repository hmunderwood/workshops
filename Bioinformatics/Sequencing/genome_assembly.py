#!/usr/bin/env python
# encoding: utf-8
"""
genome_assembly.py

Heather Underwood on 2016-2-13.

This program illustrates the genome sequencing process by taking a series of "reads",
and uses the concept of parsimony to stich the reads togetherto create a candidate
chromosome of the target organism. The general algorithm used here is a single growing
superstring with ends "a" and "b". Each read has ends "c" and "d". By looking at possible
overlapping regions of "a" and "c", and overlaps between "b" and "d" we can determine
where and if the read is going to be appended to the superstring. We also check first if the
read is already contained in the superstring - then nothing is appended.

To run from command line: python genome_assembly.py genome_assembly.txt

"""

import sys
import os
import string
from collections import defaultdict

# Import DNA reads
file_name = list(sys.argv)
text_file = open(file_name[1])
reads = text_file.read()
temp = reads.split('>')

# Create a list of all the given 'reads' in the text file
read_list = defaultdict(str)
for x in range(1, len(temp)):
	read_whole = temp[x].split('\n', 1)
	read_name = read_whole[0]
	read = read_whole[1].replace('\n',"")
	read_list[read_name] = read

read_values = read_list.values()
superstring = read_values[0]
read_values.remove(read_values[0])

# Superstring: the growing superstring of concatenated reads
# Read: the new read to be concatenated to the superstring
# FB: a boolean variable, 1 if add to front, 0 if add to back
# overlap_len: by how much the read overlaps with the superstring
def superstring_concat(ss, read, fb, overlap_len):
	# Add read to end of the superstring
	if fb == 0:
		ss = ss + read[overlap_len:len(read)]	
	# Add read to the beginning of the superstring	
	else:
		ss = read[0:len(read) - overlap_len] + ss
	
	return ss


while len(read_values) > 0:
	for entry in read_values:
		match = 0
		# Entire entry is not already contained in the superstring
		if superstring.find(entry) == -1:
			half_read_length = len(entry) / 2
			index = len(entry)
	
			# Add read to end of superstring check
			while index > half_read_length and match == 0:
				# Compare forward read with end of superstring (c, b)
				temp_read_f = entry[0:index]
				ss_back = superstring[len(superstring)-index:len(superstring)]
	
				# Compare end of read with beginning of superstring (d, a)
				temp_read_b = entry[len(entry)-index:len(entry)]
				ss_front = superstring[0:index]

				if temp_read_f == ss_back:
					# Match
					superstring = superstring_concat(superstring, entry, 0, index)
					read_values.remove(entry)
					match = 1
		
				if temp_read_b == ss_front:
					superstring = superstring_concat(superstring, entry, 1, index)
					read_values.remove(entry)
					match = 1
		
				# Create a shorter substring of the read to compare
				index = index - 1
	
		# The entire read is already contained in the superstring; remove it from read_values	
		else:
			read_values.remove(entry)

print "Final superstring: " + superstring


