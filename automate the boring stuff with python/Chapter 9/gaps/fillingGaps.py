#! python3
# fillingGaps.py - Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.

import os

rootFolder = os.getcwd()
prefix = 'prefix'

files = []

for folderName, subfolders, filenames in os.walk(rootFolder):
    for filename in filenames:
        if filename.startswith(prefix):
            files.append(folderName + '/' + filename)

files.sort()

print(files)
