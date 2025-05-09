from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from init_test import init_driver
from config import  test_host

 
try:
    driver = init_driver()
    
    driver.get(f"{test_host}/simple.html") 
    
    # 1. close tutorialOverlay
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert  tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
    gotItBtn = driver.find_element(By.ID, "gotItBtn")
    assert  gotItBtn.is_displayed(), "gotItBtn is not displayed"
    
    gotItBtn.click()
    time.sleep(2)

 
    # 2. click bedroom2
    bedroom2_buttons = driver.find_element(By.ID, "bedroom2-label")
    bedroom2_buttons.click()
    time.sleep(3)
 
    # 3. goto next step
    to_step_2_buttons = driver.find_element(By.ID, "to-step-2")

    to_step_2_buttons.click()
    time.sleep(3)

    #plus_btn_buttons = driver.find_element(By.CLASS_NAME, "plus-btn")
    #dplus_button = driver.find_element(By.XPATH, '//*[@id="appliance-grid-container"]/div[1]/div[3]/button[2]')
    dplus_button = driver.find_element(By.CSS_SELECTOR, "div.appliance-card[data-title='LED Lights (10x)'] button.plus-btn")
    # 4. add one LED lights(10x)
    dplus_button.click()
    time.sleep(3)

    # 5. goto next step
    to_step_3_buttons = driver.find_element(By.ID, "to-step-3")
    to_step_3_buttons.click()
    time.sleep(3)
    
    # 6. test total-kwh-value
    total_value = driver.find_element(By.ID, "total-kwh-value")
    assert "8.8"== total_value.text, "test total-kwh-value failed, expected 8.8, but got " + total_value.text


    time.sleep(3)

finally:
    driver.quit()