#! python3
# mcb.pyw : saves and loads clipboard contents
# usage: py.exe mcb.pyw save [keyword] : 
#   saves clipboard contents to keyword
# usage: py.exe mcb.pyw keyword
#   loads saves keyword contents to clipboard
# usage: py.exe mcb.pyw list
#   loads list of keywords to clipboard
# usage: py.exe mcb.pyw delete keyword
# usage: py.exe mcb.pyw delete

import pyperclip, sys, os, shelve
base = os.getcwd()
print(base)
storeFile = os.path.join(base,"ReadingWritingFiles/Multiclipboard/Store")
if not os.path.exists(storeFile):
  os.mkdir(storeFile)
mcbShelf = shelve.open(os.path.join(storeFile,'mcbFile'))
if len(sys.argv) == 3 
  if sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
  elif sys.argv[1].lower() == 'delete':
    pass # delete sys.argv[2]
elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
  elif sys.argv[1].lower() == 'delete':
    pass # handle later
  elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

