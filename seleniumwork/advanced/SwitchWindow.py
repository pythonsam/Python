from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchWindow:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(6)

        # Find the Parent Window Handle - Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle :" + parentHandle)

        # Find Open window button / Link  and Click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(3)

        # Find all the handles , thee should be two handles after clicking the Open window button / Link
        handles = driver.window_handles

        # Switch to window and Search Course
        for handle in handles:
            print("Hnadle: " + handle)

        # searchbox = driver.find_element(By.ID, "search-courses")
        # searchbox.send_keys("Python")


ch = SwitchWindow()
ch.test()

