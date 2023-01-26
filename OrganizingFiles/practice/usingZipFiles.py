#! usr/bin/python
# basic usage of the zipfile module
import os, zipfile,shutil
from sys import exit as se
from os.path import join as osj
# create ZipFile object ~ to file objects using zipfile.ZipFile(zip file)
# ZipFile objects have various methods, 
# like extract, extractall,setpassword, write,writestr,getinfo, namelist, open
# also, various attributes like mode,filename,filelist etc
base = os.path.join(os.getcwd(),"OrganizingFiles/practice")
print(base)
# se()
if not os.path.exists(base):
  os.mkdir(base)
os.chdir(base)
zfilepath = osj(base,"trialZip.zip")
zF = zipfile.ZipFile(zfilepath,'w')
for filename in os.listdir():
  if os.path.isdir(filename):
    continue
  print(filename)
  if filename.endswith('.zip'):
    continue
  zF.write(
    filename, # this added entire file with base dir to zipfile
    compress_type=zipfile.ZIP_DEFLATED
  )
zF.close()

# reading zip files
zRead = zipfile.ZipFile(zfilepath)
filesInZip = []
for name in zRead.namelist():
  filesInZip.append(name)
# can also create getinfo objects for each file in the zip file
# this getinfo object has information about the file
for name in zRead.namelist():
  gIo = zRead.getinfo(name)
  print(f"Info about {name} file: ")
  print(f"File size: {gIo.file_size}")
  print(f"Compressed size:{gIo.compress_size}")
zRead.close()


# Extracting zips
zEx = zipfile.ZipFile(zfilepath)
zEx.extractall(osj(os.getcwd(),"extractedFiles"))
# extractall extracts stuff into cwd if zero parameter call
# extract method removes single file
for f in zEx.namelist():
  if not os.path.isdir(f):
    zEx.extract(f,osj(os.getcwd(),"extractedFiles2"))
  zEx.close()