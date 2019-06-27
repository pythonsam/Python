from selenium import webdriver

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
import requests
from bs4 import BeautifulSoup


class Hyperlinks:
    def test(self):
        baseURL = 'http://www.learningaboutelectronics.com'
        getpage = requests.get(baseURL)
        #print(getpage)
        getpage_soup=BeautifulSoup(getpage.text, 'html.parser')
        all_links = getpage_soup.find_all('a')
        print(all_links)
        #for link in all_links:
         #    length = len(link)
          #   print(length)

ch = Hyperlinks()
ch.test()
