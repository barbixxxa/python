#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Delete a keyword from the shelf.
#        py.exe mcb.pyw delete - Delete all keywords.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
# Save clipboard content.

if len(sys.argv) == 3:
    # Save
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(sys.argv[2] + ' saved successfully')

    # Delete
    if sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
        print([sys.argv[2] + ' deleted'])

elif len(sys.argv) == 2:
    # List
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('List of all keywords copied to clipboard')

    # Delete all
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print('All keywords and associated contents have been deleted')

    # Load
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv[1] + ' loaded successfully')

    else:
        print('That keyword doesn\'t exist - so nothing has been loaded to the clipboard')
else:
    print("Wrong command\n\nUsage:\n\t# py.exe mcb.pyw save < keyword > - Saves clipboard to keyword.\n\t# py.exe mcb.pyw delete < keyword > - Delete a keyword from the shelf.\n\t# py.exe mcb.pyw delete - Delete all keywords.\n\t# py.exe mcb.pyw < keyword > - Loads keyword to clipboard.\n\t# py.exe mcb.pyw list - Loads all keywords to clipboard.")

mcbShelf.close()
