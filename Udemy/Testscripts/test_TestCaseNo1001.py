from selenium import webdriver
import unittest
# import pytest
import os
import sys
import traceback
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from Syslibrary.datadriver import readjson
jsonread1 = readjson()

from Library.Launchapplication import launchapplication
application = launchapplication()

dir_path = os.path.dirname(os.path.realpath(__file__))

folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))


class TestcaseNo1001(unittest.TestCase):
    def test_testcaseno1001(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            time.sleep(8)
            iframe = browser.switch_to.frame('comp-jgmoxxgs1iframe')
            actionChains = ActionChains(browser)
            actionChains.send_keys(Keys.ESCAPE).perform()
            print('Iframe Exists ')
            time.sleep(5)
            practise = browser.find_element_by_css_selector('#DrpDwnMn04label').click()
            print("Clicked on Practise Page")

        except Exception:
            traceback.print_exc()
            self.fail('TestcaseNo1001 Failed')
        finally:
            application.closeborwser(browser)


if __name__ == '__main__':
    unittest.main()

