#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

# Initialize frequency and range dictionaries
frequency_dict = {}
range_dict = {}
range_bool = {}


# --- FUNCTIONS ---


# Open XML file and read it.
def open_and_read(file_loc):
    with open(file_loc, 'r', encoding='utf-8') as f:
        read_data = f.read()
    return read_data


# Search for lemma and add counts to "frequency{}".
def find_and_count(doc):
    match_pattern = re.findall(r'lemma="[א-ת]+', doc)
    for word in match_pattern:
        count = frequency_dict.get(word[7:], 0)
        frequency_dict[word[7:]] = count + 1
        # print(word[7:])
        range_bool[word[7:]] = True
    for k in range_bool:
        if range_bool[k]:
            count = range_dict.get(k, 0)
            range_dict[k] = count + 1
            range_bool[k] = False


# Sort entries in "frequency{}" dictionary by count.
def sort_frequencies():
    return [(k, frequency_dict[k]) for k in sorted(
        frequency_dict, key=frequency_dict.__getitem__, reverse=True)]


# -- MAIN CODE ---

# Define path for topmost directory to search.
p = Path('../OpenSubtitles2018_parsed/parsed/he')
p = list(p.glob('**/*.xml'))

# Run "open_and_read()" and "find_and_count()" functions
#   for each XML file.
for f in p:
    find_and_count(open_and_read(f))

# Run "sort_frequencies()" function.
frequency_sorted = sort_frequencies()

# Write final tallies to CSV file.
result = open('HebrewLemmaCount.csv', 'w')
for k, v in frequency_sorted:
    result.write(str(v) + ', ' + k + ', ' + str(
        range_dict[k]) + '\n')
result.close()
