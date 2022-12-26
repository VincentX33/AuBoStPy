#! usr/bin/python3
import os
filename = "hello.txt"
path = os.path.abspath('./../simulation/trial1')
helloFile = open(os.path.join(path,filename),'a')
# write does not automatically add \n like print()
# write returns number of characters added to file
if helloFile.mode == 'a':
  helloFile.write('\n')
helloFile.writelines("I am happy being myself\n")
helloFile.writelines("And I gotta read treasure island")
helloFile.close()
helloFile = open(os.path.join(path, filename),'r')
for line in helloFile.readlines():
  print(line,end='')
print()