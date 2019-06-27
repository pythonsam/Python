from selenium import webdriver
from selenium.webdriver.common.by import By

class WindowSize:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(6)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Height:" + str(height))
        print("Width:" + str(width))


ch = WindowSize()
ch.test()