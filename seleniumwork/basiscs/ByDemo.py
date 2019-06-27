from selenium import webdriver
from selenium.webdriver.common.by import By


class Bydemo:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        elementByClass = driver.find_element(By.CLASS_NAME, "displayed-class")
        elementByClass.send_keys('Test Class Name')
        if elementByClass is not None:
            print('We found an Element by Class')

        elementByLink = driver.find_element(By.LINK_TEXT, "Login")
        if elementByLink is not None:
            print('We found an Element by Link Text')

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCSS is not None:
            print('We found an Element by Css Selector')


ch = Bydemo()
ch.test()