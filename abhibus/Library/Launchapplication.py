"""
ALl the classes and corresponding methods will be here, all the methods are reusable components
The methods are loosely coupled so anyone can make use of these methods
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import sys

# getting current working Folder
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# getting Parent folder for current working folder
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

# Navigating to desired folder
sys.path.insert(0, folder_path + "\SysLibrary")

# Importing the module from SysLibrary
from SysLibrary.datadriver import ReadJson
# Creating class object and instances of that object
jsonread1 = ReadJson()


class Launchapplication():
    def intilizebrowser(self):
        env = jsonread1.jsonread(folder_path + "\Env\setup.json")
        # print(env)
        if env['browser'] == 'chrome':
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'firefox':
            browser = webdriver.Firefox()
            browser.implicitly_wait(5)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'headlessChrome':
            chrome_options = Options()
            # chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            # chrome_options.add_argument("--window-size - 1920x1080") # optional
            # chrome_driver = folder_path + "Env\chromedriver.exe" ignore this path use below path
            chrome_driver = "C:\\Python36\\chromedriver.exe"
            # print(chrome_driver)
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
            browser.implicitly_wait(6)
            # print('Headless browser executed')
            return browser

    def closebrowser(self, browser):
            browser.close()

    def inputurl(self, browser):
            url = jsonread1.jsonread(folder_path + "\Env\setup.json")
            # print(url)
            if url['url'] == 'prestagurl':
                prestagurl = jsonread1.jsonread(folder_path + '\Env\setup.json')
                browser.get(prestagurl['prestagurl'])

            elif url['url'] == 'stagurl':
                stagurl = jsonread1.jsonread(folder_path + '\Env\setup.json')
                browser.get(stagurl['stagurl'])

    def abhibus_locators(self):
            abhibus_locators = jsonread1.jsonread(folder_path + '\Object\Locators.json')
            # print(abhibus_locators)
            return abhibus_locators

    def abhibus_testdata(self):
            abhibus_testdata = jsonread1.jsonread(folder_path + '\Data\Testdata.json')
            # print(abhibus_testdata)
            return abhibus_testdata






