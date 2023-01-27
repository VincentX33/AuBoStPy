#! usr/bin/python3
# project: european style dates
# to convert mm-dd-yyyy in dates to dd-mm-yyyy
# to iterate over a folder and perform this renaming 
# in a particular folder and all its subdirectories
"""
module overview:
  identify the pattern of american style dates
  call os.listdir() to get listing of all files in directory
  loop over obtained filenames to check whether it has american dates
  rename with shutil.move() if it is american date
"""

import shutil, os, re, sys,random
# american date (mm)-(dd)-(yyyy)
amerDate = re.compile(r"""^(.*?) # all text before date
  ((0|1)?\d)(-|/)# group 2 for whole date, group 3 for maybe prefix (june is 6 or 06)
  ((0|1|2|3)?\d)(-|/) # for the date, can be 01,11,21,31 and not others
  ((18|19|20)\d\d) # group 6 for the year
  (.*?)$
  """,re.VERBOSE
)
"""
  group listings for above re.search(): findall list indices one less
  previous: 1
  month is : 2
  day: 5
  year: 8
  after: 10
"""
x = amerDate.findall("Amer dates like 12-31-2032 and 11/10/2032")
print(x)
#TODO: loop over files in directory
runFrom = os.getcwd() #following code assumes run from AuBoStPy/
os.chdir(os.path.join(runFrom,"OrganizingFiles/EuroDates"))
print(os.getcwd())
#TODO: ignore files that don't match
if not os.path.exists("./TrialFiles"):
  os.mkdir("TrialFiles")
os.chdir("TrialFiles")

for i in range(8):
  m = random.randint(1,12)
  d = random.randint(1,30)
  y = random.randint(1800,2029)
  date = str(m)+'-'+str(d)+'-'+str(y)
  fp = open("name"+date+"suf.txt", 'w')
  fp.close()


#TODO: get different parts of filename
#currently in trialFiles folder
# get a listing of all the files in this folder
# filenames = []
for fl in os.listdir('.'):
  if os.path.isfile(fl):
    print(fl)
    mo = amerDate.search(fl)
    if mo == None:
      continue
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(5)
    year = mo.group(8)
    after = mo.group(10)
    
    #TODO: form european-filename
    eurofname = f"{before}{day}-{month}-{year}{after}"
    #print(f"new filename:{eurofname}")
    
    #TODO: get abspath of files to be renamed
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,fl)
    euroFilename = os.path.join(absWorkingDir,eurofname)
    print(f"Renaming {amerFilename} to {euroFilename}")
    shutil.move(amerFilename,euroFilename)

# use os.walk for getting all files, even in subdirs
# make this change later


#TODO: rename the files
