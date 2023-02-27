#!python3
# program to utilize the explain the basic features of the requests module
import requests, pyperclip,validators
# res1 = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# print(type(res1)) 
# will give 'class requests.models.Response'
# print(res1.status_code)
# print(requests.codes.ok)
# print(len(res1.text))
# print(res1.text[:250])

# res2 = requests.get('http://www.gutenberg.org/cache/epub/1112/billion.txt')
# should give error as wrong url
# following line stops the program if download failed
# res2.raise_for_status()


# if download failure isn't reason for termination,
# call raise_for_status() within try catch
# try:
#   res2.raise_for_status() 
# except Exception as exc:
#   print("There was a problem:  %s " %(exc))

# saving downloaded files to drive

print("copy url of file to be downloaded to clipboard:")
url:str = pyperclip.waitForNewPaste(50) #waits 50 seconds to copy the url
fName:str = input("Enter name of file :")
if len(fName) > 30:
  fName = input("Enter valid filename: ")
try:
  if validators.url(url):
    res = requests.get(url)
    res.raise_for_status()
    svfile = open(fName,"wb")
    for chunk in res.iter_content(100000):
      # each chunk is of bytes data type
      svfile.write(chunk)
    svfile.close()
  else:
    raise 
except :
  print("Unable to download file stored at invalid url")