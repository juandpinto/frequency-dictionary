#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import gzip
from collections import defaultdict

# Initialize dictionaries
lemma_by_corpus_dict = {}
lemma_totals_dict = {}
token_count_dict = {}
lemma_DPs_dict = defaultdict(float)
lemma_UDPs_dict = defaultdict(float)

total_tokens_int = 0
table_list = []

# Identify size of list
list_size_int = 3000


# ------------ FUNCTIONS ------------


# Open XML file and read it.
def open_and_read(file_loc):
    with gzip.open(file_loc, 'rt', encoding='utf-8') as f:
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


# ------------ OPEN AND READ ------------


# Define path for topmost directory to search. (0/374995)
p = './OpenSubtitles2018_parsed_single/parsed/he/0'

# Create list of IDs for movies with Hebrew as primary language
# Hebrew_IDs_list = []
# with open('./Hebrew_originals.txt', 'r', encoding='utf-8') as f:
#     read_data = f.read()
#     Hebrew_IDs_list = re.findall(r'\s\stt[0-9]+\t', read_data)
# Hebrew_IDs_list = [line[4:-1] for line in Hebrew_IDs_list]
#
# # Delete extra 0s at the beginning of Hebrew movie IDs
# for item in Hebrew_IDs_list:
#     if item[0] == '0':
#         Hebrew_IDs_list[Hebrew_IDs_list.index(item)] = item[1:]
# for item in Hebrew_IDs_list:
#     if item[0] == '0':
#         Hebrew_IDs_list[Hebrew_IDs_list.index(item)] = item[1:]

# Count lemmas for movies with Hebrew as primary language
# for dirName, subdirList, fileList in os.walk(p):
#     if len(fileList) > 0:
#         f = dirName + '/' + fileList[0]
#         folders = re.split('/', dirName)
#         if folders[len(folders)-1] in Hebrew_IDs_list:
#             find_and_count(open_and_read(f))

# Count lemmas for all movies
for dirName, subdirList, fileList in os.walk(p):
    if len(fileList) > 0:
        f = dirName + '/' + fileList[0]
        find_and_count(open_and_read(f))

# ------------ CALCULATIONS ------------


# Calculate token count per corpus
for lemma in lemma_by_corpus_dict:
    for corpus in lemma_by_corpus_dict[lemma]:
        token_count_dict[corpus] = token_count_dict.get(
            corpus, 0) + lemma_by_corpus_dict[lemma][corpus]

# Calculate total frequencies per lemma
for lemma in lemma_by_corpus_dict:
    lemma_totals_dict[lemma] = sum(lemma_by_corpus_dict[lemma].values())

# Calculate total token count
for corpus in token_count_dict:
    total_tokens_int = total_tokens_int + token_count_dict.get(corpus, 0)

# Sort entries in "frequency{}" dictionary by count.
frequency_sorted_list = [(k, lemma_totals_dict[k]) for k in sorted(
    lemma_totals_dict, key=lemma_totals_dict.__getitem__,
    reverse=True)]

# Calculate DPs
for lemma in lemma_by_corpus_dict.keys():
    for corpus in lemma_by_corpus_dict[lemma].keys():
        lemma_DPs_dict[lemma] = lemma_DPs_dict[lemma] + abs(
            (token_count_dict[corpus] /
             total_tokens_int) -
            (lemma_by_corpus_dict[lemma][corpus] /
             lemma_totals_dict[lemma]))
lemma_DPs_dict = {lemma: DP/2 for (lemma, DP) in lemma_DPs_dict.items()}

# Calculate UDPs
lemma_UDPs_dict = {lemma: 1-DP for (lemma, DP) in lemma_DPs_dict.items()}


# Calculate list size for 70% coverage
added_freq_int = 0
count = 0
for k, v in frequency_sorted_list:
    print(v, added_freq_int, count)
    if added_freq_int / total_tokens_int < 0.7:
        added_freq_int = added_freq_int + v
        count = count + 1
    else:
        break
print(count)
print(added_freq_int)
print(total_tokens_int)
print(added_freq_int / total_tokens_int)

# ------------ CREATE TABLE ------------

#
# # Create list of tuples with all values
# # Lemma, Frequency, Range, DP
# # table_list = [(k, v, sum(lemma_by_corpus_dict[k].values()))
# #     for k, v in frequency_sorted_list[:20]]
# for k, v in frequency_sorted_list[:list_size_int]:
#     table_list.append((k, v, sum(
#         1 for count in lemma_by_corpus_dict[k].values() if count > 0),
#         lemma_UDPs_dict[k]))
#
#
# # print(table_list)
# # for i in range(list_size_int):
# #     print('Lemma: ' + table_list[i][0] +
# #           '\tFrequency: ' + str(table_list[i][1]) +
# #           '\tRange: ' + str(table_list[i][2]) +
# #           '\tUDP: ' + str(table_list[i][3]))
#
#
# # Write final tallies to CSV file
# result = open('./export/HebrewWordList.csv', 'w')
# # for k, v in frequency_sorted_list:
# #     result.write(str(v) + ', ' + k + ', ' + '\n')
# # result.close()
# result.write('LEMMA, FREQUENCY, RANGE, UDP\n')
# for i in range(list_size_int):
#     result.write(str(table_list[i][0]) + ', ' +
#                  str(table_list[i][1]) + ', ' +
#                  str(table_list[i][2]) + ', ' +
#                  str(table_list[i][3]) + '\n')
# result.close()
