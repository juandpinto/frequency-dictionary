#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import gzip
from collections import defaultdict


############################################################
# ----------------- INITIALIZE VARIABLES ----------------- #
############################################################

# Define path for topmost directory to search. Make sure this points
# to the correct location of your corpus.
corpus_path = './OpenSubtitles2018_parsed_single/parsed/he'

# Initialize dictionaries
lemma_by_file_dict = {}
lemma_totals_dict = {}
lemma_norm_dict = {}
token_count_dict = {}
lemma_DPs_dict = defaultdict(float)
lemma_UDPs_dict = defaultdict(float)

total_tokens_int = 0
total_files_int = 0
table_list = []
row = tuple()

# Set size of final list
list_size_int = 5000


############################################################
# ------------------- DEFINE FUNCTIONS ------------------- #
############################################################


# Open XML file and read it.
def open_and_read(file_loc):
    with gzip.open(file_loc, 'rt', encoding='utf-8') as f:
        read_data = f.read()
    return read_data


# Search for lemmas and add counts to "lemma_by_file_dict{}".
def find_and_count(doc):
    file = str(f)[40:-3]
    match_pattern = re.findall(r'lemma="[א-ת]+"', doc)
    for word in match_pattern:
        if word[7:-1] in lemma_by_file_dict:
            count = lemma_by_file_dict[word[7:-1]].get(file, 0)
            lemma_by_file_dict[word[7:-1]][file] = count + 1
        else:
            lemma_by_file_dict[word[7:-1]] = {}
            lemma_by_file_dict[word[7:-1]][file] = 1


############################################################
# -------------------- OPEN AND READ --------------------- #
############################################################

# Open and read all files. If only for a specific language, comment
# out this code and uncomment the large block that follows.
#
for dirName, subdirList, fileList in os.walk(corpus_path):
    if len(fileList) > 0:
        total_files_int = total_files_int + 1
        f = dirName + '/' + fileList[0]
        find_and_count(open_and_read(f))

############################################################
# ---------------- LANGUAGE-SPECIFIC BLOCK -----------------
#
# This large block of code is for creating a list using only #
# movies with a specific primary language (in this case, Hebrew). #
# Be sure to uncomment the relevant lines of code, and to comment #
# out the block above. #
#
#
# Create list of IDs for movies with Hebrew as primary language. #
# This uses a text file that must already exist with this list. #
#
# Hebrew_IDs_list = []
# with open('./Hebrew_originals.txt', 'r', encoding='utf-8') as f:
#     read_data = f.read()
#     Hebrew_IDs_list = re.findall(r'\s\stt[0-9]+\t', read_data)
# Hebrew_IDs_list = [line[4:-1] for line in Hebrew_IDs_list]
#
#
# Delete extra 0s at the beginning of Hebrew movie IDs. #
#
# for item in Hebrew_IDs_list:
#     if item[0] == '0':
#         Hebrew_IDs_list[Hebrew_IDs_list.index(item)] = item[1:]
# for item in Hebrew_IDs_list:
#     if item[0] == '0':
#         Hebrew_IDs_list[Hebrew_IDs_list.index(item)] = item[1:]
#
#
# Open and read movies files with Hebrew as the primary language. #
#
# for dirName, subdirList, fileList in os.walk(corpus_path):
#     if len(fileList) > 0:
#         f = dirName + '/' + fileList[0]
#         folders = re.split('/', dirName)
#         if folders[len(folders)-1] in Hebrew_IDs_list:
#             find_and_count(open_and_read(f))
#
# ------------- END OF LANGUAGE-SPECIFIC BLOCK -------------
############################################################


############################################################
# --------------------- CALCULATIONS --------------------- #
############################################################

# Calculate total raw frequencies per lemma
for lemma in lemma_by_file_dict:
    lemma_totals_dict[lemma] = \
        sum(lemma_by_file_dict[lemma].values())

# Calculate token count per file
for lemma in lemma_by_file_dict:
    for file in lemma_by_file_dict[lemma]:
        token_count_dict[file] = token_count_dict.get(
            file, 0) + lemma_by_file_dict[lemma][file]

# Calculate total token count
for file in token_count_dict:
    total_tokens_int = \
        total_tokens_int + token_count_dict.get(file, 0)

# Set value for normalized frequency (freq per x words)
freq_per_int = 1000000

# Calculate normalized frequencies per lemma
for lemma in lemma_totals_dict:
    lemma_norm_dict[lemma] = \
        lemma_totals_dict[lemma] / total_tokens_int * freq_per_int

# Calculate DPs
for lemma in lemma_by_file_dict.keys():
    for file in lemma_by_file_dict[lemma].keys():
        lemma_DPs_dict[lemma] = lemma_DPs_dict[lemma] + abs(
            (token_count_dict[file] /
             total_tokens_int) -
            (lemma_by_file_dict[lemma][file] /
             lemma_totals_dict[lemma]))
lemma_DPs_dict = {lemma: DP/2 for (lemma, DP) in
                  lemma_DPs_dict.items()}

# Calculate UDPs
lemma_UDPs_dict = {lemma: (1-DP)*lemma_norm_dict[lemma] for
                   (lemma, DP) in lemma_DPs_dict.items()}


############################################################
# -------------- SORT LIST AND CREATE TABLE -------------- #
############################################################

# Sort entries by UDP
UDP_sorted_list = [(k, lemma_UDPs_dict[k]) for k in sorted(
    lemma_UDPs_dict, key=lemma_UDPs_dict.__getitem__,
    reverse=True)]

# Create list of tuples with all values:
# (Lemma, Rank, UDP, Frequency, Range)
i = 0
for k, v in UDP_sorted_list[:list_size_int]:
    i = i + 1
    row = (k,
           i,
           '{0:,.2f}'.format(v),
           '{0:,.2f}'.format(lemma_norm_dict[k]),
           '{0:,.2f}'.format(sum(1 for count in
                                 lemma_by_file_dict[k].values() if
                                 count > 0) /
                             total_files_int * 100))
    table_list.append(row)

############################################################
# ---------------- SORT-BY-FREQUENCY BLOCK -----------------
#
# Sort entries by raw frequency (total lemma count). To sort the #
# final list by frequency instead of dispersion, comment out the #
# above code within the "SORT LIST AND CREATE TABLE" section, and #
# also uncomment the relevant lines of code in this block. #
#
#
# Sort entries by raw frequency #
#
# frequency_sorted_list = [(k, lemma_totals_dict[k]) for k in
#                          sorted(lemma_totals_dict,
#                          key=lemma_totals_dict.__getitem__,
#                          reverse=True)]
#
#
# Create list of tuples with all values #
#
# for k, v in frequency_sorted_list[:list_size_int]:
#     table_list.append((k, v, sum(
#         1 for count in lemma_by_file_dict[k].values() if
#         count > 0), lemma_UDPs_dict[k]))
#
# ------------- END OF SORT-BY-FREQUENCY BLOCK -------------
############################################################

# Calculate list size for 80% coverage and set that as the list
# size. Note that if the initial list_size_int (set near the
# beginning of the script) provides less than the desired coverage,
# it will default to that instead.
#
# added_freq_int = 0
# count = 0
# for k, v in UDP_sorted_list:
#     if added_freq_int / total_tokens_int < 0.8:
#         added_freq_int = added_freq_int + lemma_totals_dict[k]
#         count = count + 1
#     else:
#         break
# list_size_int = count

# Write final tallies to TSV file
result = open('./export/frequency-dictionary.tsv', 'w')
result.write('LEMMA\tRANK\tDISPERSION\tFREQUENCY\tRANGE\n')
for i in range(list_size_int):
    result.write(str(table_list[i][0]) + '\t' +
                 str(table_list[i][1]) + '\t' +
                 str(table_list[i][2]) + '\t' +
                 str(table_list[i][3]) + '\t' +
                 str(table_list[i][4]) + '\n')
result.close()

# Print final tallies. Uncomment this code to see the results
# printed instead of writing them to a file.
#
# for i in range(list_size_int):
#     print('Lemma: ' + table_list[i][0] +
#           '\tFrequency: ' + str(table_list[i][1]) +
#           '\tRange: ' + str(table_list[i][2]) +
#           '\tUDP: ' + str(table_list[i][3]))
