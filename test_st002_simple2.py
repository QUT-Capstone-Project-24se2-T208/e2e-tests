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
    
    # 1.close tutorialOverlay
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert  tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
    gotItBtn = driver.find_element(By.ID, "gotItBtn")
    assert  gotItBtn.is_displayed(), "gotItBtn is not displayed"
    
    gotItBtn.click()
    time.sleep(2)

 
    # 2. click select 3 bedrooms
    bedroom3_buttons = driver.find_element(By.ID, "bedroom3-label")
    bedroom3_buttons.click()
    time.sleep(3)

     # 3. select More Sun
    more_sun_label = driver.find_element(By.ID, "more-sun-label")
    more_sun_label.click()
    time.sleep(3)

    # 4. goto next step
    to_step_2_buttons = driver.find_element(By.ID, "to-step-2")
    to_step_2_buttons.click()
    time.sleep(3)
    

    # 5. add one Dryer  
    dplus_button = driver.find_element(By.CSS_SELECTOR, "div.appliance-card[data-title='Dryer'] button.plus-btn")
    dplus_button.click()
    time.sleep(3)
    
    # 6. back to previous step
    back_to_step_1_buttons = driver.find_element(By.ID, "to-step-1")
    back_to_step_1_buttons.click() 
    time.sleep(3)
    
    
    # 7. goto next step
    to_step_2_buttons = driver.find_element(By.ID, "to-step-2")
    to_step_2_buttons.click()
    time.sleep(3)
    
    
    # 8. goto next step
    to_step_3_buttons = driver.find_element(By.ID, "to-step-3")
    to_step_3_buttons.click()
    time.sleep(3)
    
    # test total-kwh-value
    total_value = driver.find_element(By.ID, "total-kwh-value")
    assert "17.3"== total_value.text, "test total-kwh-value failed, expected 17.3, but got " + total_value.text

    time.sleep(3)

finally:
    driver.quit()