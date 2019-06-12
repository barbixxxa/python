#! python3
# madlibs.py
# reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

import re
import os

# Prompt for file name in cwd to read and save its content to string variable
file_name = input('Enter the txt file name you wish to use: ')
textFile = open('{0}/{1}.txt'.format(os.getcwd(), file_name))
fileContent = textFile.read()
textFile.close()

print('\n\t### File loaded and text copied ###\n')

print(fileContent)

# Find the matches in the fileContent
madlibRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
matches = madlibRegex.findall(fileContent)

# Replace the matched word
for match in matches:
    word = input('Enter a ' + match.lower() + ': ')
    fileContent = fileContent.replace(match, word, 1)

print('\n\t### Text replaced ###\n')

# Write the string to a new file
fileToBeSaved_name = input(
    'Enter the name of the output file you wish to save: ')
outputFile = open('{0}/{1}.txt'.format(os.getcwd(), fileToBeSaved_name), 'w')
outputFile.write(fileContent)
outputFile.close()

print('\n\t### File saved ###\n')

# Print the string
print(fileContent)
