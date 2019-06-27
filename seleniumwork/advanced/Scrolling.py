from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Scrolling:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        # Scroll Down
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(5)
        # Scroll Up
        driver.execute_script("window.scrollBy(0,-600);")


ch = Scrolling()
ch.test()


