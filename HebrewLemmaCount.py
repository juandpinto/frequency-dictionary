#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

# Initialize dictionary
lemma_by_corpus_dict = {}
lemma_totals_dict = {}
token_count_dict = {}


# ----- FUNCTIONS -----


# Open XML file and read it.
def open_and_read(file_loc):
    with open(file_loc, 'r', encoding='utf-8') as f:
        read_data = f.read()
    return read_data


# Search for lemma and add counts to "frequency{}".
def find_and_count(doc):
    corpus = str(f)[38:-4]
    match_pattern = re.findall(r'lemma="[א-ת]+"', doc)
    for word in match_pattern:
        if word[7:-1] in lemma_by_corpus_dict:
            count = lemma_by_corpus_dict[word[7:-1]].get(corpus, 0)
            lemma_by_corpus_dict[word[7:-1]][corpus] = count + 1
        else:
            lemma_by_corpus_dict[word[7:-1]] = {}
            lemma_by_corpus_dict[word[7:-1]][corpus] = 1


# Add total tokens per corpus
def add_tokens():
    for lemma in lemma_by_corpus_dict:
        for corpus in lemma_by_corpus_dict[lemma]:
            token_count_dict[corpus] = token_count_dict.get(
                corpus, 0) + lemma_by_corpus_dict[lemma][corpus]


# Add total frequencies per lemma
def calculate_total_frequencies():
    for lemma in lemma_by_corpus_dict:
        for corpus in lemma_by_corpus_dict[lemma]:
            lemma_totals_dict[lemma] = lemma_totals_dict.get(
                lemma, 0) + lemma_by_corpus_dict[lemma][corpus]


# Sort entries in "frequency{}" dictionary by count.
def sort_frequencies():
    return [(k, lemma_totals_dict[k]) for k in sorted(
        lemma_totals_dict, key=lemma_totals_dict.__getitem__,
            reverse=True)]


# ----- MAIN CODE -----


# Define path for topmost directory to search.
p = Path('../OpenSubtitles2018_parsed/parsed/he/0/374995')
p = list(p.glob('**/*.xml'))

# Run "open_and_read()" and "find_and_count()" functions
#   for each XML file.
for f in p:
    find_and_count(open_and_read(f))

# Run "add_tokens()" and "calculate_total_frequencies()"
add_tokens()
calculate_total_frequencies()

# Debugger:
# for item in lemma_totals_dict:
#     print(item + '  -  ' + str(lemma_totals_dict[item]))

# Debugger:
# for lemma in lemma_by_corpus_dict:
#     for corpus in lemma_by_corpus_dict[lemma]:
#         print(lemma + '  -  ' + corpus + '  -  ' + str(
#             lemma_by_corpus_dict[lemma][corpus]))

# Run "sort_frequencies()" function.
frequency_sorted = sort_frequencies()

# Write final tallies to CSV file.
result = open('HebrewLemmaCount.csv', 'w')
for k, v in frequency_sorted:
    result.write(str(v) + ', ' + k + ', ' + '\n')
result.close()
