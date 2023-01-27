#! usr/bin/python3
import traceback,os

basedir = os.getcwd()
if os.path.basename(basedir) == "AuBoStPy":
  os.chdir("./Debugging")
try:
  raise Exception("Basic error message")
except: 
  errorFile = open("error.txt","w")
  errorFile.write(traceback.format_exc())
  traceback.print_exc()
  print("Traceback info written to error.txt")
  errorFile.close()
