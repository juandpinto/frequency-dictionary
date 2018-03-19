#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

# Initialize dictionaries
lemma_by_corpus_dict = {}
lemma_totals_dict = {}
token_count_dict = {}

total_tokens = 0
table_list = []


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


# ----- MAIN CODE -----


# Define path for topmost directory to search.
p = Path('../OpenSubtitles2018_parsed/parsed/he/0')
p = list(p.glob('**/*.xml'))

# Run "open_and_read()" and "find_and_count()" functions
#   for each XML file.
for f in p:
    find_and_count(open_and_read(f))

# Add total tokens per corpus for each lemma
for lemma in lemma_by_corpus_dict:
    for corpus in lemma_by_corpus_dict[lemma]:
        token_count_dict[corpus] = token_count_dict.get(
            corpus, 0) + lemma_by_corpus_dict[lemma][corpus]

# Add total frequencies per lemma
for lemma in lemma_by_corpus_dict:
    lemma_totals_dict[lemma] = sum(lemma_by_corpus_dict[lemma].values())

# Add total token counts per corpus
for corpus in token_count_dict:
    total_tokens = total_tokens + token_count_dict.get(corpus, 0)

# Sort entries in "frequency{}" dictionary by count.
frequency_sorted_list = [(k, lemma_totals_dict[k]) for k in sorted(
    lemma_totals_dict, key=lemma_totals_dict.__getitem__,
    reverse=True)]


# Write final tallies to CSV file.
# result = open('HebrewLemmaCount.csv', 'w')
# for k, v in frequency_sorted_list:
#     result.write(str(v) + ', ' + k + ', ' + '\n')
# result.close()

# Create list of tuples with all values
# table_list = [(Lemma, Frequency, Range, DP)]
# table_list = [(k, v, sum(lemma_by_corpus_dict[k].values()))
#     for k, v in frequency_sorted_list[:20]]
for k, v in frequency_sorted_list[:20]:
    table_list.append((k, v, sum(
        1 for count in lemma_by_corpus_dict[k].values() if count > 0)))

# print(table_list)
for i in range(20):
    print('Lemma: ' + table_list[i][0] +
          '\tFrequency: ' + str(table_list[i][1]) +
          '\t\tRange: ' + str(table_list[i][2]))
