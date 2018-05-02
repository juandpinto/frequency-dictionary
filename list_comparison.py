#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

lemmas_original_list = []
lemmas_all_list = []
shared_list = []

# Import all lemmas in original-language list
with open('./export/frequency-dictionary-original-only.tsv', 'r',
          encoding='utf-8') as f:
    read_data = f.read()
    lemmas_original_list = re.findall(r'[א-ת]+', read_data)

# Import all lemmas in list from all subtitles
with open('./export/frequency-dictionary.tsv', 'r',
          encoding='utf-8') as f:
    read_data = f.read()
    lemmas_all_list = re.findall(r'[א-ת]+', read_data)

# Find shared lemmas
for item in lemmas_original_list:
    if item in lemmas_all_list:
        shared_list.append(item)

# Print shared lemmas and total count
for item in shared_list:
    print(item)
print('Total shared: ' + str(len(shared_list)))
