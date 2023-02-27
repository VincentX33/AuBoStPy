# Explanation to tutorial.py
The tutorial is divided into three parts:
- working requests.get
- requests.get with invalid url
- a 5-line snippet project involving requests, pyperclip, and validators modules
The first two components are self explanatory: part 3 was interesting: made a 
file downloader. The downsides are that it doesn't have error checking or 
filesize validation yet, so if malicious url is given, system/drive might crash.
So download_size_validation is one of the steps remaining.

## File downloader
- tells the user to copy a url to clipboard
- takes a valid `filename` from user
- takes `url` from the clipboard, validates if it is proper URL(using validators.url() function)
- gets a response object `res` from the given url
- raises response object status ie, checks if file downloaded correctly (`res.raise_for_status()`)
- opens a binary file with the given `filename` 
- iterates through `100000` byte chunks of res.iter_content()
- - iter_content iterates through the file
- - writes each chunk to the file `filename`
- if invalid url or download failed, raise error, display error message
