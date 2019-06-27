from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class DropDownlist:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(4)
        element = driver.find_element(By.CSS_SELECTOR, '#carselect')
        sel = Select(element)

        # SELECT BY VALUE
        sel.select_by_value('benz')
        print('Select Benz by Value')
        time.sleep(2)

        # SELECT BY VISIBLE TEXT
        sel.select_by_visible_text("BMW")
        print('Select BMW by Visible Text')

        # SELECT BY INDEX
        sel.select_by_index(2)
        print('Select Honda by Index')


ch = DropDownlist()
ch.test()