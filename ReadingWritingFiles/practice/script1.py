import os, sys
path = os.path.abspath('./ReadingWritingFiles/practice/simulation/trial1/')
fileName = 'capitals.txt'
filePath = os.path.join(path, fileName)
ofilePath = os.path.join(path, 'opCaps.txt')
if os.path.exists(filePath):
  print("running program")
  dataFile = open(filePath, 'r')
  opFile = open(ofilePath,'w')
else:
  sys.exit()

text = dataFile.read()
pairs = text.split(',')
for line in pairs:
  opFile.writelines(line+',\n')
dataFile.close()
opFile.close()
