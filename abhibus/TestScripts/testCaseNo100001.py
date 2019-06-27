from selenium.webdriver.common.by import By
import unittest
import os
import time
import traceback

from SysLibrary.datadriver import ReadJson
jsonread1 = ReadJson()

from Library.Launchapplication import Launchapplication
application = Launchapplication()

# Get the current working Folder
dir_path = os.path.dirname(os.path.realpath(__file__))

# Get Parent Folder
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))

tf = 'test_TestcaseNo100001'

class TestCaseNo100001(unittest.TestCase):
    def test_TestcaseNo100001(self):
        try:
            browser = application.intilizebrowser()
            application.inputurl(browser)

            # abhibus_locators = jsonread1.jsonread(folder_path + '\Object\Locators.json')
            abhibus_locators = application.abhibus_locators()

            # abhibus_testdata = jsonread1.jsonread(folder_path + '\Data\Testdata.json')
            abhibus_testdata = application.abhibus_testdata()

            abhibuspage_logo_tooltip = browser.find_element(By.XPATH, abhibus_locators['logo'])
            abhibuspage_logo_tooltip = abhibuspage_logo_tooltip.get_attribute("title")
            # print (abhibuspage_logo_tooltip)
            time.sleep(3)
            self.assertEqual(abhibuspage_logo_tooltip, "abhibus.com - India's Fastest Online bus ticket booking site")

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path + "\Screenshots\Testcase-%s.png" % tf)
            self.fail('Testcase No : 100001 is Failed')
        finally:
            browser.close()


if __name__ == '__main__':
    unittest.main()


