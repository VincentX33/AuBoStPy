#! usr/bin/python3
# navigating folders for creation, deletion, renaming
# using the os.walk() method
import os
for folder, subfolders, files in os.walk(os.getcwd()):
  if '.git' in folder:
    continue
  print("\nCurrent folder is "+ folder)
  for sf in subfolders:
    print("Subfolder of ", folder, " : "+sf)
  for fl in files:
    print("Files in ", folder , ": ", fl)
