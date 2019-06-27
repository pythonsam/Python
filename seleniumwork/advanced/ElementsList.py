from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementsList:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        radioButtoList = driver.find_elements(By.XPATH, "//input[contains(@name,'cars') and contains(@type,'radio')]")
        size = len(radioButtoList)
        print(size)

        for radibutton in radioButtoList:
            isselected = radibutton.is_selected()

            if not isselected:
                radibutton.click()
                time.sleep(4)


ch = ElementsList()
ch.test()
