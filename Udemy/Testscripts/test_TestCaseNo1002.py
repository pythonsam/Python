from selenium import webdriver
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

@pytest.mark.flaky(rerun =5)
class TestcaseNo1002(unittest.TestCase):
    def test_testcaseno1002(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            time.sleep(8)

            letsKode_data = application.testdata()
            letskode_locators = application.loocators()

            iframe = browser.switch_to.frame('comp-jgmoxxgs1iframe')
            actionChains = ActionChains(browser)
            actionChains.send_keys(Keys.ESCAPE).perform()
            print('Iframe Exists ')
            time.sleep(5)

            practise = browser.find_element_by_css_selector('#DrpDwnMn04label')
            practise.click()
            print("Clicked on Practise Page")

            title = browser.title
            print(title)
            print(letskode_locators['browsertitle'])
            self.assertEqual(title, letskode_locators['browsertitle'])

        except Exception:
            traceback.print_exc()
            self.fail('TestcaseNo1001 Failed')
        finally:
            application.closeborwser(browser)


if __name__ == '__main__':
    unittest.main()
