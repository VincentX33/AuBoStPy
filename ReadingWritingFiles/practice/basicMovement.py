#! usr/bin/python
"""
Program to explain the basic usage
of many of the os and os.path methods
The os module is used for file movement, 
as well as basic directory commands
like making folders, changing permissions,
and renaming.
"""
import os,sys
print(f"Seperator for this system {os.sep}")
print(f"Current directory is {os.getcwd()}")
print(f"Listing file contents: \n{os.listdir()}")
print(f"Making absolute path from relative path:")
print(f"{os.getcwd()} : {os.path.abspath('/')}")
print(f"Making relative path to home/vincent")
print(f"{os.getcwd()} to {os.path.relpath('./','/home/vincent')}")
print("Creating trial folders")
# os.mkdir("./simulation/trial2")
# on first run works correctly, on
# second run it gives FileExistsError
# to handle this
creationPath = "./ReadingWritingFiles/practice/simulation/trial" # folder basename w/o number
if not os.path.exists(creationPath+str(1)):
  print("Error")
  sys.exit()
for i in range(1,11):
  if not os.path.isdir(creationPath+str(i)):
    os.mkdir(creationPath + str(i))
print(os.listdir("./ReadingWritingFiles/practice/simulation/"))
# removing the unnecessary programs
for i in range(3,11):
  if os.path.isdir(creationPath+str(i)):
    os.rmdir(creationPath + str(i))
    print(f"Removed folder {i}")
total = 0
x = os.path.abspath('./../..')
for filename in os.listdir(x):
  total += os.path.getsize(os.path.join(x,filename))
print(f"{x} : {total}")