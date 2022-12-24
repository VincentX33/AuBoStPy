#! python3
'''
Solution to the project in pattern matching in AuBoStPy
'''
#import section
import pyperclip, re, sys
"""
Trial phone text:
+913443234532, 5323925331, 08322914153
434-234-2352  and 124-424-1424 vincent@google.com
lmd@heart.com ud@fs.fd.com
"""

#phone Num regex
indianPhoneNum = re.compile(r'''(
  (\+91)?
  (((\d){10})| ((\d){4}(\s|-)?((\d){7})))
  )''',re.VERBOSE)

amerPhoneNum  = re.compile(r"(\d{3})?-(\d{3})-(\d{4})")

#email regex
emailR = re.compile(r'''(
  ([a-zA-Z0-9.%_+-]+) #seqence of chars repeated more than once
  (@) #at the rate symbol
  ([a-zA-Z0-9.-]{2,12}) #domain name
  (\.) # dot
  ([a-zA-Z]{2,5}) #group 4
)''',re.VERBOSE)

#taking text off clipboard
clipBoardContents : str = ""
# if pyperclip.is_available():
#   clipBoardContents = pyperclip.waitForNewPaste()
# else:
#   print("Won't be able to run program automatically\n")
#   clipBoardContents = input("Enter manually (or ctrl^v): ")
# find emails, phNos
clipBoardContents = pyperclip.paste()
matches = []
# print(clipBoardContents)
ph1 = amerPhoneNum.findall(clipBoardContents)
# print(ph1)
for p in ph1:
  matches.append('-'.join(p))
  # print(p)
# onto clipboard
ph2 = indianPhoneNum.findall(clipBoardContents)
# print(ph1)
for p in ph2:
  matches.append(p[0])
  # print(p)
e1 = emailR.findall(clipBoardContents)
# print(ph1)
for e in e1:
  matches.append(e[0])
  # print(p)
print(matches)
final = '\n'.join(matches)
pyperclip.copy(final)
print(final)