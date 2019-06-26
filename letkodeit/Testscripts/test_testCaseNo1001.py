from selenium import webdriver
import unittest
import os
import traceback
import time

from Syslibrary.datadriver import readjson
jsonread1 = readjson()

from Library.Launchapplication import launchapplication
application = launchapplication()

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

tf = 'test_TestcaseNo1001'


class TestcaseNo1001(unittest.TestCase):
    def test_TestcaseNo1001(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)

            app_testdata = jsonread1.jsonread(folder_path + '\Data\Testdata.json')
            actual_title = app_testdata["title"]
            print(actual_title)

            expected_title = browser.title
            print('Title is :' + expected_title)
            self.assertEqual(actual_title, expected_title)

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path + '\Screenshots\Testcase-%s.png' % tf)
            self.fail('Test case No : 100001 is failed')
        finally:
            application.closebrowser(browser)


if __name__ == '__main__':
    unittest.main()


