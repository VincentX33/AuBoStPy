#!python3
# simple program that takes an address either from the
# command line argument, or from the clipboard,
# and opens the google map page for the given address
# in the default browser
import webbrowser, pyperclip, sys

# check if address given as command line argument
if len(sys.argv) > 1:
  address: str = ' '.join(sys.argv[1:])
else:
  address:str = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)