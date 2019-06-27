from selenium import webdriver


def sizeofWindow():

    driver =webdriver.Chrome()
    height = driver.execute_script("return window.innerHeight")
    width = driver.execute_script("return window.innerWidth")

    print("Height:" + str(height))
    print("width:" + str(width))

sizeofWindow()

