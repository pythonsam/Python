"""
This is UNIT TEST Example USING POM
"""

from selenium import webdriver
import time
import unittest
import HtmlTestRunner

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))

# Getting Current Working Folder
dir_path = os.path.dirname(os.path.realpath(__file__))
# Getting Parent of Current Working Folder
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))


#from pom.pages.login_page import LoginPage
#from pom.pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.home_page import HomePage



class OrangeHRM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        baseURL = "https://opensource-demo.orangehrmlive.com"
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(baseURL)
        cls.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver = self.driver
        # self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
        time.sleep(3)

        homepage = HomePage(driver)
        homepage.click_on_welcome()
        homepage.click_on_logout()

        # usrname = self .driver.find_element(By.ID, "txtUsername")
        # usrname.send_keys("Admin")
        #
        # passwd = self.driver.find_element(By.ID, "txtPassword")
        # passwd.send_keys("admin123")
        #
        # loginbtn = self.driver.find_element(By.ID, "btnLogin")
        # loginbtn.click()
        #
        # welcomelink = self.driver.find_element(By.ID, "welcome")
        # welcomelink.click()
        #
        # logoutbtn = self.driver.find_element(By.LINK_TEXT, "Logout")
        # logoutbtn.click()
        # time.sleep(2)
    def test_login_Invalid_username(self):
        driver = self.driver
        # self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username('Admin1')
        login.enter_password('admin123')
        login.click_login()
        message = driver.find_element_by_xpath("").text
        self.assertEqual(message, "Invalid credentials")

        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


"""
To Run from command prompt as python login.py add below one
Without adding below command to script u can run the scrip by using python -m unittest login.py
"""
if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='D:/sdet/Python/pom/reports'))

Orange = OrangeHRM()
Orange.login_test()
