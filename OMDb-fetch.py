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

print('# ' + year + '\n' +
      'IMDb ID\tTitle\tYear\tLanguage(s)')


omdb.set_default('apikey', '')

for i in dirs:
    if i > '0681189':
        doc = omdb.imdbid('tt' + i)
        # if doc['language'] == 'Hebrew':
        print('tt' + i + '\t' +
              doc['title'] + '\t' +
              doc['year'] + '\t' +
              doc['language'])
