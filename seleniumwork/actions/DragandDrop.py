from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragandDrop:
    def test(self):
        baseURL = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Switch to iFrame
        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement, toElement).perform()

            # Another way to perform Drag and Drop ActionChains
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and Drop Action Performed")
        except:
            print("Drag and Drop Action Not Performed")


ch = DragandDrop()
ch.test()




