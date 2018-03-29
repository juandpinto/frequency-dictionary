#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

lemmas_Hebrew_list = []
lemmas_all_list = []
diff_list = []

with open('./export/HebrewWordList_HebrewOnly.csv', 'r',
          encoding='utf-8') as f:
    read_data = f.read()
    lemmas_Hebrew_list = re.findall(r'[א-ת]+', read_data)

with open('./export/HebrewWordList.csv', 'r',
          encoding='utf-8') as f:
    read_data = f.read()
    lemmas_all_list = re.findall(r'[א-ת]+', read_data)


for item in lemmas_Hebrew_list:
    if item in lemmas_all_list:
        diff_list.append(item)

for item in diff_list:
    print(item)
print('Total shared: ' + str(len(diff_list)))
