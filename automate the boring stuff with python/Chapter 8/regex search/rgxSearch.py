#! python3
# rgxSearch.py
# opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression

import os
import re

# Enter the desired folder
path = ''
while os.path.isdir(path) != True:
    #path = input('Insert the path to the file: ')
    # just for example, remove this line and insert the line above to receive user input
    path = '/home/theeam/Documents/learning/python/automate the boring stuff with python/Chapter 8/regex search'

os.chdir(path)
print('\n\t### You are at: ' + os.getcwd() + '\n')

files = os.listdir(path)
print('\n\t### Files found: ')
print(files)

#regExpr = input('Insert the regex: ')
# just for example, remove this line and insert the line above to receive user input
regExpr = '(ADJECTIVE|NOUN|ADVERB|VERB)'
regexSearch = re.compile(regExpr)

matches = []
for fileName in files:
    if '.txt' in fileName:
        textFile = open(fileName)
        fileContent = textFile.read()
        match = regexSearch.findall(fileContent)
        if match:
            for i in match:
                matches.append(i)
        textFile.close()

print('\n\t### Matches found: ')
print(matches)
