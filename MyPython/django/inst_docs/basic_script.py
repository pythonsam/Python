
import os
from selenium import webdriver

import sele_refer as refer


cur_dir = os.getcwd()
# Create a new directory to store saved screenshots
screens_path = cur_dir + os.path.sep + "screens"
if not os.path.exists(screens_path):
    os.mkdir(screens_path)

try:
    driver = webdriver.Chrome()
    
    driver.maximize_window()
    driver.get("https://www.python.org/")

    about_elem = driver.find_element_by_xpath(refer.ABOUT_XP)
    about_elem.click()

    driver.save_screenshot(screens_path+os.path.sep+"about.png")
    driver.back()

    downloads_elem = driver.find_element_by_xpath(refer.DOWNLOADS_XP)
    downloads_elem.click()

    driver.save_screenshot(screens_path+os.path.sep+"downloads.png")
    driver.back()
except Exception as e:
    print("Exception while executing script. %s"%e)
finally:
    driver.quit()
