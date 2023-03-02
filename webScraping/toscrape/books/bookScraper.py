#! python3
import bs4, requests, validators, pyperclip,os,
from selenium import webdriver
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
# program with functions that scrape the books.toscrape.com 

res = requests.get(url)
try:
    print(os.getcwd())
    # needs to be called from books directory to work properly
    driver = webdriver.Firefox()
    driver.get(url)
    # res.raise_for_status()
    file = open("obtainedFile.html",'w')
    soup = bs4.BeautifulSoup(driver.page_source, features='lxml')
    # for chunk in res.iter_content():
    #   file.write(chunk)
    
    file.close()
    # print(soup.prettify())
except:
    print("Not able to get response object")
