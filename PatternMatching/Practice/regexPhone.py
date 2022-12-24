import re,sys
phoneNum  = re.compile(r"\d{3}-\d{3}-\d{4}")
matchObj = phoneNum.search("434-234-2352 vincent@google")
print(matchObj.group())
# sys.exit() # while debugging

indianPhoneNum = re.compile(r'''(
  (\+91)?
  ((\d{10,11}))
  )''',re.VERBOSE)
indianPhoneNum2 = re.compile(r'''(
  (\+91)?
  ((\d){4}(\s|-)((\d){7}))
  )''',re.VERBOSE)
matches = indianPhoneNum2.findall("+919146158746 and 8320322213, are numbers along with 0832-2914153")
for i in matches:
  print(i)

'''
Learnings:
in re, special chars need to be escaped
'''

