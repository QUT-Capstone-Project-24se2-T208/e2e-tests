from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from config import  test_host
from init_test import init_driver
 
try:
    driver = init_driver()
    
    driver.get(f"{test_host}/assistive.html") 
    
 
 
    # 2. click select 4 bedrooms
    bedroom4_buttons = driver.find_element(By.ID, "bedroom4-label")
    bedroom4_buttons.click()
    time.sleep(3)

     # 3. select less Sun
    less_sun_label = driver.find_element(By.ID, "less-sun-label")
    less_sun_label.click()
    time.sleep(3)

    backup_options = driver.find_element(By.XPATH, '//*[@id="step-1"]/div[3]/div[1]')
    backup_options.click()
    time.sleep(3)


    # 4. goto next step
    to_step_2_buttons = driver.find_element(By.ID, "to-step-2")
    to_step_2_buttons.click()
    time.sleep(3)
    

    # 5. minus one Dryer  
    minus_button = driver.find_element(By.CSS_SELECTOR, "div.appliance-card[data-title='Dryer'] button.minus-btn")
    minus_button.click()
    time.sleep(3)
    
    minus_button = driver.find_element(By.CSS_SELECTOR, "div.appliance-card[data-title='Kettle'] button.minus-btn")
    minus_button.click()
    time.sleep(2)
    minus_button.click()
    time.sleep(2)
    
    
    # 8. goto next step
    to_step_3_buttons = driver.find_element(By.ID, "to-step-3")
    to_step_3_buttons.click()
    time.sleep(3)
    
    # test total-kwh-value
    total_value = driver.find_element(By.ID, "total-kwh-value")
    assert "18.3"== total_value.text, "test total-kwh-value failed, expected 18.3, but got " + total_value.text

    time.sleep(3)

finally:
    driver.quit()