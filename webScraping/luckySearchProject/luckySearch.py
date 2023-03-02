#!python3
# a simple program that 
# - takes a search term as input
# - searches for the term on google
# - visits the first n links
# idea: if possible, store default no of result tabs in a persistent config binary file
# idea: can take the first argument as the search term string, second as number of searches (default 5)
import sys, pyperclip, requests, bs4, webbrowser,validators
from selenium import webdriver

# webbrowser.open_new()
base : str = "https://google"
countryCode : str = "com"
searchString: str = "search?q="
"""
try soup.find('div', id_=)

"""

def search_for_term(query:str):
    print("googling...")
    url: str = '/'.join([('.'.join([base,countryCode])),''.join([searchString,'+'.join(query.split(' '))])])
    if validators.url(url):
        # res = requests.get(url)
        # res.raise_for_status()
        driver = webdriver.Firefox() #change with your browser
        driver.get(url)
        # print(res.text) # prints out the raw response: unreadable
        soup = bs4.BeautifulSoup(driver.page_source,features='lxml')
        driver.quit()
        # print(soup.text)
        searchDiv = soup.select('#rso a')
        # print(type(searchDiv[0]))
        i = 0
        for link in searchDiv:
            extLink = link.get('href')
            if extLink == None:
                continue
            if extLink.startswith('/search?q'):
                # print('https://google.com'+extLink)  
                generatedUrl = 'https://google.co.in'+extLink
            else:
                # print(extLink)
                generatedUrl = extLink
            if i < 5:
                i += 1
                webbrowser.open(generatedUrl)
            
    else:
        print("invalid url")
        print(url)

# take the sys.argv:
#print(len(sys.argv))
if len(sys.argv) == 1:
    # get something off clipboard and search for it
    searchTerm = pyperclip.paste()
    if len(searchTerm) >= 20:
        print("copy valid search term to clipboard")
        searchTerm = pyperclip.paste()

    if not validators.url(searchTerm):
        print("copy valid search term to clipboard")
        searchTerm = pyperclip.paste()
        
    print("calling the search_for_term function")
    search_for_term(searchTerm) #temporarily off


elif len(sys.argv) == 2:
    # url as second argument
    #print(sys.argv[1])
    #print(type(sys.argv[1]))
    print("calling the search_for_term function")
    search_for_term(sys.argv[1]) #temporarily off
    # search_for_term('virat kohli')
elif len(sys.argv)==3:
    # number of searches as third argument
    print(' -- '.join(sys.argv))
    print(type(int(sys.argv[2]))) 
    print(int(sys.argv[2]))