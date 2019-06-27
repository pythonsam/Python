from selenium import webdriver
from selenium.webdriver.common.by import By


class FindIdByName:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)
        elementById = driver.find_element(By.ID, "name")
        if elementById is not None:
            print('We Found an element by Id')
        elementByName = driver.find_element(By.NAME, "show-hide")
        if elementByName is not None:
            print('We Found an element by Name')
        driver.close()


ch = FindIdByName()
ch.test()
