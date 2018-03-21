#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# import re
from sys import argv
import os
import glob
import omdb

# year = '1996'
script, year = argv

dirs = []
p = []


for name in glob.glob(
        '../OpenSubtitles2018_parsed/parsed/he/' + year + '/*/'):
    p.append(name)
# p = Path('../OpenSubtitles2018_parsed/parsed/he')
# p = list(p.glob('[198-199]*/*/*.xml'))

p = [os.path.basename(os.path.dirname(str(i))) for i in p]

for i in p:
    if i not in dirs:
        dirs.append(i)

for i in dirs:
    while len(i) < 7:
        dirs[dirs.index(i)] = '0' + i
        i = '0' + i

dirs.sort()

# for i in dirs:
#     print('tt' + i)

print('# ' + year + '\n')


omdb.set_default('apikey', '906517b3')

for i in dirs:
    doc = omdb.imdbid('tt' + i)
    # if doc['language'] == 'Hebrew':
    print('ID: tt' + i)
    print('Title: ' + doc['title'] +
          '\nYear: ' + doc['year'] +
          '\tLanguage: ' + doc['language'] +
          '\n')
