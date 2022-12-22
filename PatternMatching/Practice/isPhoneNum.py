def isPhoneNumber(text):
  if len(text) != 12:
    return False
  for i in range(0,3):
    if not text[i].isdigit():
      return False
  if text[3] != '-':
    return False
  for i in range(4,7):
    if not text[i].isdigit():
      return False
  if text[7] != '-':
    return False
  for i in range(8,12):
    if not text[i].isdigit():
      return False
  return True

if __name__ == '__main__':
  numSt : str = input("Enter number:")
  if (isPhoneNumber(numSt)):
    print(f"{numSt} is a phone number")
  else:
    print(f"{numSt} is not a phone number")
