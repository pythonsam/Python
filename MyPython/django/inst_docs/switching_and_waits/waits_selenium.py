
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cwd = os.getcwd()
html_file = "file:///" + cwd + os.path.sep + "loading_page.html"

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(html_file)
    return driver

def do_wait(driver):
    wobj = WebDriverWait(driver, 10)
    print("Waiting for python link")
    wobj.until(EC.visibility_of_element_located((By.LINK_TEXT, "Visit Python site!")))
    driver.find_element_by_link_text("Visit Python site!").click()
    print("Link clicked")

def close_browser(driver):
    driver.quit()
    

driver = open_browser()
do_wait(driver)
close_browser(driver)