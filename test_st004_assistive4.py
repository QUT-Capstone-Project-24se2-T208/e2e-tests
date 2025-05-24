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
    
 
 
    # 2. click select 2 bedrooms
    bedroom2_buttons = driver.find_element(By.ID, "bedroom2-label")
    bedroom2_buttons.click()
    time.sleep(1)

     
    # 4. goto next step
    to_step_2_buttons = driver.find_element(By.ID, "to-step-2")
    to_step_2_buttons.click()
    time.sleep(1)
    

    
    category_general = driver.find_element(By.ID, "category-general")
    category_general.click()
    time.sleep(1)
    
    add_custom_appliance = driver.find_element(By.CLASS_NAME, "add-custom-appliance")
    add_custom_appliance.click()
    time.sleep(1)
    
    #editable-appliance-name
    editable_appliance_name = driver.find_element(By.CLASS_NAME, "editable-appliance-name")
    editable_appliance_name.clear()
    editable_appliance_name.send_keys("Air Purifier")
    time.sleep(1)
    
    #custom-wattage
    custom_wattage = driver.find_element(By.CLASS_NAME, "custom-wattage")
    # up and down arrow key to select 27 Wattage
    custom_wattage.click()
    custom_wattage.clear()
    custom_wattage.send_keys("27")
    #custom_wattage.send_keys(Keys.ARROW_DOWN)
    #for i in range(27):
    #    custom_wattage.send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)
 
    #custom-hours
    custom_hours = driver.find_element(By.CLASS_NAME, "custom-hours")
    # up and down arrow key to select 24 Wattage
    custom_hours.click()
    custom_hours.clear()
    custom_hours.send_keys("24")
    
    time.sleep(2)
    # 8. goto next step
    to_step_3_buttons = driver.find_element(By.ID, "to-step-3")
    to_step_3_buttons.click()
    time.sleep(2)
    
    # test total-kwh-value
    total_value = driver.find_element(By.ID, "total-kwh-value")
    assert "9.0"== total_value.text, "test total-kwh-value failed, expected 9.0, but got " + total_value.text

    time.sleep(3)

finally:
    driver.quit()