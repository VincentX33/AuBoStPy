#! usr/bin/python3
import os,sys
filename = "hello.txt"
print(os.getcwd())
"""
Was getting errors for a long time, because my
cwd was root of the git repo, in Aubostpy, but 
I was assuming that it was in ReadingWritingFiles
"""
path = os.path.abspath('./ReadingWritingFiles/practice/simulation/trial1/')
# path = os.path.abspath('simulation/trial1')
print(path)
try :
  filePath = os.path.join(path, filename)
  print(filePath)
  if os.path.exists(filePath):
    print("Path exists")
    helloFile = open(filePath,'a')
  else:
    helloFile = open(filePath,'w')
except FileNotFoundError:
  print("Error locating file")
# write does not automatically add \n like print()
# write returns number of characters added to file
# sys.exit()
if helloFile.mode == 'a' and os.path.getsize(filePath)!=0:
  helloFile.write('\n')
helloFile.writelines("I am happy being myself\n")
helloFile.writelines("And I gotta read treasure island\n")
helloFile.writelines("This line is added after semester exams")
helloFile.close()
helloFile = open(os.path.join(path, filename),'r')
for line in helloFile.readlines():
  print(line,end='')
print()