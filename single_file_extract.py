#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import os
from pathlib import Path

file_dirs = []

# source = os.listdir("../OpenSubtitles2018_parsed/parsed/he/0")
# destination = ("../OpenSubtitles2018_parsed_selected")

# p = Path('../OpenSubtitles2018_parsed/parsed/he/0')
# p = list(p.glob('**/*.xml.gz'))
#
# print(p)

# shutil.copytree(source, destination)

source = '../OpenSubtitles2018_parsed/parsed/he/0'

for dirName, subdirList, fileList in os.walk(source):
    print('Directory: %s' % dirName)
    print(fileList)
    # for fname in fileList:
    #     print('\t%s' % fname)

# for folder in source:
#     f = 0
#     # print(folder)
#     for file in folder:
#         if file.endswith('.xml.gz'):
#             print(file)
#             if f == 0:
#                 file_dirs.append(file)
#             f = 1
    # shutil.copy(files, destination)

# print(type(file_dirs))
# print(file_dirs)
