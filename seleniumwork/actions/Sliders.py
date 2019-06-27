from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Sliders:
    def test(self):
        baseURL = 'https://jqueryui.com/slider/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(4)

        driver.switch_to.frame(0)
        sliderElement = driver.find_element(By.XPATH,"//div[@id='slider']//span")

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(sliderElement,100,0).perform()
            print("Slider Successfull")
        except:
            print("Slider Unsuccessfull")


ch = Sliders()
ch.test()

