#! python3
# unneededFiles.py - Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. Print these files with their absolute path to the screen.

import os

# input('Insert the folder path: ')
rootFolder = input('Insert the root folder path: ')
size = int(input('Insert the minimum size in bytes: '))

for folderName, subfolders, filenames in os.walk(rootFolder):
    for filename in filenames:
        absoluteFilePath = folderName + '/' + filename
        fileSize = os.path.getsize(absoluteFilePath)
        if fileSize >= size:
            print('* FILE: ' + absoluteFilePath + '\nSIZE: ' + str(fileSize))
