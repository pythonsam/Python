from selenium import webdriver
import requests
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://google.co.in/')
# links = browser.find_elements_by_css_selector("a")
links = browser.find_elements_by_tag_name("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(r)
    print(link.get_attribute('href'), r.status_code)
