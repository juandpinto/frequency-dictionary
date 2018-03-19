#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

# Initialize dictionary
lemma_dict = {}
total_lemma_freq_dict = {}
token_count_dict = {}


# ----- FUNCTIONS -----


# Open XML file and read it.
def open_and_read(file_loc):
    with open(file_loc, 'r', encoding='utf-8') as f:
        read_data = f.read()
    return read_data


# Search for lemma and add counts to "frequency{}".
def find_and_count(doc):
    name = str(f)[38:-4]
    match_pattern = re.findall(r'lemma="[א-ת]+', doc)
    for word in match_pattern:
        if word[7:] in lemma_dict:
            count = lemma_dict[word[7:]].get(name, 0)
            lemma_dict[word[7:]][name] = count + 1
        else:
            lemma_dict[word[7:]] = {}
            lemma_dict[word[7:]][name] = 0


# Add total tokens per corpus
def add_tokens():
    for lemma in lemma_dict:
        for name in lemma_dict[lemma]:
            token_count_dict[name] = token_count_dict.get(name, 0) + \
                lemma_dict[lemma][name]


# Add total frequencies per lemma
def calculate_total_frequencies():
    for lemma in lemma_dict:
        for name in lemma_dict[lemma]:
            total_lemma_freq_dict[lemma] = total_lemma_freq_dict.get(
                lemma, 0) + lemma_dict[lemma][name]


# Sort entries in "frequency{}" dictionary by count.
def sort_frequencies():
    return [(k, lemma_dict[k]) for k in sorted(
        lemma_dict, key=lemma_dict.__getitem__, reverse=True)]


# ----- MAIN CODE -----


# Define path for topmost directory to search.
p = Path('../OpenSubtitles2018_parsed/parsed/he/0')
p = list(p.glob('**/*.xml'))

# Run "open_and_read()" and "find_and_count()" functions
#   for each XML file.
for f in p:
    find_and_count(open_and_read(f))

# Run "add_tokens()" and "calculate_total_frequencies()"
add_tokens()
calculate_total_frequencies()

for item in total_lemma_freq_dict:
    print(item + '  -  ' + str(total_lemma_freq_dict[item]))

# Run "sort_frequencies()" function.
# frequency_sorted = sort_frequencies()

# Write final tallies to CSV file.
# result = open('HebrewLemmaCount.csv', 'w')
# for k, v in frequency_sorted:
#     result.write(str(v) + ', ' + k + ', ' + str(
#         range_dict[k]) + '\n')
# result.close()
