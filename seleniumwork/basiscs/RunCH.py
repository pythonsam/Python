from selenium import webdriver
import os


class RunCHTest:

    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        # driver = webdriver.Ie()

        # serverlocation = 'C:/Users/shyam.emmadi/Downloads/Python/seleniumserver/selenium-server-standalone-3.141.59.jar'
        # os.environ['SELENIUM_SERVER_JAR'] = serverlocation
        # driver = webdriver.Safari()

        driver.maximize_window()
        driver.get(baseURL)


ch = RunCHTest()
ch.test()

