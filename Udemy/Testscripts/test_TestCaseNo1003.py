from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import sys
import traceback
import unittest
import pytest

from Syslibrary.datadriver import readjson
jsonread1 = readjson()

from Library.Launchapplication import launchapplication
application = launchapplication()

dir_path = os.path.dirname(os.path.realpath(__file__))

folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))


# @pytest.mark.flaky(rerun =5)
class TestcaseNo1003(unittest.TestCase):
    def test_testcaseno1003(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            time.sleep(8)

            letsKode_data = application.testdata()
            letskode_locators = application.loocators()

            iframe = browser.switch_to.frame('comp-jgmoxxgs1iframe')
            actionChains = ActionChains(browser)
            actionChains.send_keys(Keys.ESCAPE).perform()
            time.sleep(2)

            practise = browser.find_element_by_css_selector('#DrpDwnMn04label')
            practise.click()

            title = browser.title

            login = browser.find_element(By.XPATH,letskode_locators['Login'])
            # login.click()
            # print('Login Link Clicked')
            #
            self.assertTrue(login.is_displayed())


        except Exception:
            traceback.print_exc()
            self.fail('TestcaseNo1001 Failed')
        finally:
            application.closeborwser(browser)


if __name__ == '__main__':
    unittest.main()
