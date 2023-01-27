#! usr/bin/python3
# backupToZip.py : backs up a folder and its contents to 
# zip file

import zipfile, os, sys
def backuptozip(folder: str):
  #backup entire folder to zip file
  folder = os.path.abspath(folder)
  # os.chdir(folder)
  if not os.path.exists(folder):
    print("given folder does not exist") 
    return
  
  number = 1
  while True:
    zipFileName = os.path.basename(folder)+str(number)+'.zip'
    if not os.path.exists(zipFileName):
      break
    number = number+1
  #Todo: create the zip file
  print(f"Creating {zipFileName}...")
  backupZip = zipfile.ZipFile(zipFileName,'w')
  os.chdir(folder)  

  #Todo: walk the folder and add all files and folders to zip file
  for foldername, subfolders, files in os.walk(folder):
    print(f"Adding files in {foldername}")
    backupZip.write(foldername,compress_type=zipfile.ZIP_DEFLATED) #create current folder
    for fn in files:
      newBase = os.path.basename(folder)+'_'
      if fn.startswith(newBase) and fn.endswith('.zip'):
        continue
      backupZip.write(
        os.path.join(foldername,fn),
        compress_type=zipfile.ZIP_DEFLATED)
      print(f"writing file {foldername}/{fn}")
  backupZip.close()

# print(os.path.basename(os.getcwd()))
# backuptozip("/home/vincent/Downloads")
# backuptozip("./PatternMatching")
backuptozip("./")