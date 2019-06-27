from selenium import webdriver
import time


def scrolldown():
    baseURL = "https://learn.letskodeit.com/p/practice"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(baseURL)
    driver.minimize_window()
    time.sleep(5)
    # scroll down
    driver.execute_script("window.scrollBy(0,100);")
    time.sleep(5)

    # Scroll Up
    driver.execute_script("window.scrollBy(0,-100);")
    time.sleep(5)


scrolldown()


