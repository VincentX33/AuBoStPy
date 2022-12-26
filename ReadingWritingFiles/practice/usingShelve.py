#! usr/bin/python3

# permanent data storage using shelve module

import os
import shelve
path = os.path.abspath('./ReadingWritingFiles/practice/simulation/trial2')
friends = ['suyash','smitesh','deeptej','kasim','siddeshwar']
sF = shelve.open(os.path.join(path, 'db'))
if 'fr' not in sF.keys():
  sF['fr'] = friends
sF.close()

sF = shelve.open(os.path.join(path, 'db'))
print(sF['fr'])
sF.close()