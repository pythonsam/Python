from selenium import webdriver
import time
class NavigateGet:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.back()
        time.sleep(4)
        driver.forward()
        time.sleep(5)


ch =NavigateGet()
ch.test()