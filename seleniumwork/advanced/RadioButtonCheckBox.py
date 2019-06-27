from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RadioCheckBox:
    def test(self):
        baseURL ="https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        radioButton1 = driver.find_element(By.CSS_SELECTOR, '#bmwradio')
        if radioButton1.is_enabled():
            radioButton1.click()
            print('Radio Button is Enabled')
        else:
            print('Radio Button is Not Enabled')

        time.sleep(4)
        radioButton2 = driver.find_element(By.ID, "benzradio")
        radiobtn2 = radioButton2.is_enabled()
        print('Radio Button2 is Enabled ' + str(radiobtn2))

        checkBox1 = driver.find_element(By.CSS_SELECTOR, '#bmwcheck')
        chkbox1 = checkBox1.is_enabled()
        print('Check Box is Selected ' + str(chkbox1))

        checkBox2 = driver.find_element(By.ID, "benzcheck")
        if checkBox2.is_enabled():
            checkBox2.click()
            print('Check Box2 is Selected')
        else:
            print("Check Box 2 is Not Selected")


ch =RadioCheckBox()
ch.test()
