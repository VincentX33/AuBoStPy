#! usr/bin/python3
# Practice program to learn the basics of the folder traversal modules
# Will use the shutil module, send2trash module, 

import shutil,os, sys
# usage: shutil.copy(source, destination)
#   if destination is file, file gets renamed, else stored in a directory
#   returns the path of the newly copied file
# use shutil.copytree(sourceFolder, destinationFolder)
#   copies everything from source, including subdirectories
# use shutil.move(source,destination)
# use shutil.movetree(source, destination)
# Python throws a FileNotFoundError if intermediate folders do not exist
# use os to delete single files, use shutil to delete multiple
# 
# 
# USE: os.unlink(path) to delete file at path
# USE: os.rmdir(path) to delete empty folder at path
# USE: shutil.rmtree(path) to delete entire folder at path
# example
base = os.getcwd()
deletePath = os.path.join(base, "ReadingWritingFiles/RandomQuizProject/QuizFiles")
for i in range(20):
  dPath = os.path.join(deletePath,"Quiz%s" %i)
  if os.path.exists(dPath):
    os.chdir(dPath)
    for filename in os.listdir():
      os.unlink(filename)
      print(filename)
    print(os.getcwd())
    os.chdir(deletePath)
    os.rmdir(dPath)
# the above code emptied the files generated by the previous project

# Use send2trash module for safe delete
# to delete file : send2trash.send2trash(path)