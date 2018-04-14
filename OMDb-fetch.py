#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
import os
import glob
import omdb

script, year = argv

# Initialize IDs list
IDs = []

# Create list of all movie directory paths for desired year
for name in glob.glob(
        './OpenSubtitles2018_parsed_single/parsed/he/' + year + '/*/'):
    IDs.append(name)

# Trim list of directories to only the movie IDs
IDs = [os.path.basename(os.path.dirname(str(i))) for i in IDs]

# Add additional zeros to beginning of IDs to match with database
for i in IDs:
    while len(i) < 7:
        IDs[IDs.index(i)] = '0' + i
        i = '0' + i

# Sort IDs numerically (easier to use results)
IDs.sort()

# Replace the API key here (906517b3) with your own (omdbapi.com)
omdb.set_default('apikey', '906517b3')

# Print table header
print('# ' + year + '\n' +
      'IMDb ID\tTitle\tYear\tLanguage(s)')

# Fetch and print movie ID, title, year, and language(s)
for i in IDs:
    doc = omdb.imdbid('tt' + i)
    print('tt' + i + '\t' +
          doc['title'] + '\t' +
          doc['year'] + '\t' +
          doc['language'])
