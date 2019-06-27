"""
Mouse Hover Actions
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHover:
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(4)
        driver.execute_script("window.scrollBy(0,1000);")

        mouseHover = driver.find_element(By.ID, "mousehover")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.move_to_element(mouseHover).perform()
            print("Mouse Hovered on element")
            time.sleep(2)

            elementTop = driver.find_element(By.XPATH, "//div[@class = 'mouse-hover-content']//a[text()='Top']")
            actions.move_to_element(elementTop).click().perform()
            time.sleep(3)
            print("Item Clicked")
        except:
            print("Item Not Clicked")


ch = MouseHover()
ch.test()
