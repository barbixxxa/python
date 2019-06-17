#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

import shutil
import os
import re


def selectiveCopy(rootFolder, extension, newFolderPath):
    for folderName, subfolders, filenames in os.walk(rootFolder):
        for filename in filenames:
            if filename.endswith('.' + extension):
                print('\n ### Copying ###\n * FILE: ' + filename + '\n * AT: ' +
                      folderName + '\n * TO: ' + newFolderPath + '\n##################\n')
                shutil.copy(folderName + '/' + filename, newFolderPath)


selectiveCopy('/home/theeam/Documents/learning/python/automate the boring stuff with python/Chapter 9', 'txt',
              '/home/theeam/Documents/learning/python/automate the boring stuff with python/Chapter 9/selectiveCopy')
