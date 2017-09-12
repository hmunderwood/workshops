from collections import defaultdict
import sys

# For MAC people with terminal
# file_name = list(sys.argv)
# text_file = open(file_name[1])
# reads = text_file.read()

# For everyone else
text_file = open("dict_practice.txt")
text = text_file.read()

my_list = text.split('\n')

my_dict = {}
for i in range(0, len(my_list)):
    temp_list = my_list[i].split(', ')
    if len(temp_list) > 1:
        my_dict[temp_list[0]] = temp_list[1]

print my_dict
