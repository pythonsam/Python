from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByClassTag:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        elementByClass = driver.find_element(By.CLASS_NAME, "displayed-class")
        elementByClass.send_keys('Test Class Name')
        if elementByClass is not None:
            print('We found an Element by Class')

        elementByTag = driver.find_element_by_tag_name("h1")
        text = elementByTag.text
        if elementByTag is not None:
            print("we found an Element by Tag:" + text)


ch = FindByClassTag()
ch.test()