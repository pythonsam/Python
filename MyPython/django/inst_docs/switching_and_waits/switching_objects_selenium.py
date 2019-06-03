
import os
from selenium import webdriver


cwd = os.getcwd()
html_file = "file:///" + cwd + os.path.sep + "main_page.html"

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(html_file)
    return driver

def check_data_in_paragraph(expected_text):
    print("Verifying click")
    paraRef = driver.find_element_by_id("para1")
    if expected_text not in paraRef.text:
        print("Error: Click failed. Expected text not present")

def check_frame_A(driver):
    print("Switching to frame A")
    driver.switch_to_frame("frame_a")
    print("CLicking button 1")
    f1b1 = driver.find_element_by_id("frame_a_b1")
    f1b1.click()
    check_data_in_paragraph("Frame A button1")

    print("CLicking button 2")
    f1b1 = driver.find_element_by_id("frame_a_b2")
    f1b1.click()
    check_data_in_paragraph("Frame A button2")

def check_frame_B(driver):
    """
    This function checks the button functionality
    It also handles an alert that was opened
    """
    print("Switching to frame B")
    driver.switch_to_default_content()
    driver.switch_to_frame("frame_b")
    print("CLicking button 1")
    f1b1 = driver.find_element_by_id("frame_b_b1")
    f1b1.click()
    check_data_in_paragraph("Frame B button1")

    print("CLicking button 2")
    f1b1 = driver.find_element_by_id("frame_b_b2")
    f1b1.click()
    print("Handling alert")
    alertObj = driver.switch_to_alert()
    alertObj.send_keys("Button2 tested")
    alertObj.accept()

def check_frame_C(driver):
    """
    This function switches to frame C test all buttons
    Also this clicks the link and does some functionality
    in the newly opened tab
    """
    print("Switching to frame C")
    driver.switch_to_default_content()
    frameRef = driver.find_element_by_name("frame_c")
    driver.switch_to.frame(frameRef)
    print("CLicking button 1")
    f1b1 = driver.find_element_by_id("frame_c_b1")
    f1b1.click()
    check_data_in_paragraph("Frame C button1")
    print("CLicking button 2")
    f1b1 = driver.find_element_by_id("frame_c_b2")
    f1b1.click()
    check_data_in_paragraph("Frame C button2")

    print("Clicking python link in frame C")
    driver.find_element_by_link_text("Visit Python site!").click()
    print("Switching control to new window")
    # Switching to the last window
    driver.switch_to_window(driver.window_handles[-1])
    do_page_test_about(driver)
    do_page_test_downloads(driver)
    print("Closing new opened tab and switching back to main tab")
    driver.close()
    # Switching back to some window after closing a tab
    driver.switch_to_window(driver.window_handles[-1])

def do_page_test_about(driver):
    about_elem = driver.find_element_by_xpath('//*[@id="about"]/a')
    about_elem.click()
    driver.back()

def do_page_test_downloads(driver):
    downloads_elem = driver.find_element_by_xpath('//*[@id="downloads"]/a')
    downloads_elem.click()
    driver.back()

def close_browser(driver):
    if driver:
        driver.quit()

if __name__ == "__main__":
    try:
        driver = open_browser()
        check_frame_A(driver)
        check_frame_B(driver)
        check_frame_C(driver)
    except Exception as e:
        print("Exception occured: %s"%e)
    finally:
        close_browser(driver)

