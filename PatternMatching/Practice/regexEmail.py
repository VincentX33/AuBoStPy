import re

emailR = re.compile(r'''(
  ([a-zA-Z0-9.%_+-]+) #seqence of chars repeated more than once
  (@) #at the rate symbol
  ([a-zA-Z0-9.-]{2,12}) #domain name
  (\.) # dot
  ([a-zA-Z]{2,5}) #group 4
)''',re.VERBOSE)
f = emailR.findall("vincen@gmail.com and vds@gmail.uk.co")
for D in f:
  print(''.join([D[i] for i in range(1,6)]))
# print(f)