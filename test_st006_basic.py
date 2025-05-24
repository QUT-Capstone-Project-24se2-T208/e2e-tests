from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from config import  test_host
from config import driver_path

from init_test import init_driver
 
try:
    driver = init_driver()
    
    driver.get(f"{test_host}/") 
    
    # 2. click select 2 bedrooms
    div_basic = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div[1]/div[2]')
    div_basic.click()
    time.sleep(1)
    
    
    div_basic_btn = driver.find_element(By.XPATH, '//*[@id="calculator-options"]/div/div/div[2]/div[2]/div[2]/a')
    div_basic_btn.click()
    time.sleep(1)
    
    
  

    total_value = driver.find_element(By.ID, "total-load-kw")
    assert "0.00"== total_value.text, "test total-kwh-value failed, expected 0.00, but got " + total_value.text
 
 
    # 2. click select 3 bedrooms
    bedroom3_buttons = driver.find_element(By.CSS_SELECTOR, 'button[data-bedrooms="3"]')
    bedroom3_buttons.click()
    time.sleep(3)


    total_value = driver.find_element(By.ID, "total-load-kw")
    assert "8.14"== total_value.text, "test total-kwh-value failed, expected 8.14, but got " + total_value.text

 
    # remove Fan - Ceiling
    rows = driver.find_elements(By.CSS_SELECTOR, "#appliance-list tr")

    for row in rows:
        appliance_name = row.find_element(By.CLASS_NAME, "appliance-title").text
        if appliance_name == "Fan - Ceiling":
            row.find_element(By.CLASS_NAME, "remove-btn").click()
            break
    time.sleep(1)
    
    # test total-kwh-value
    total_value = driver.find_element(By.ID, "total-load-kw")
    assert "8.02"== total_value.text, "test total-kwh-value failed, expected 8.02, but got " + total_value.text

finally:
    driver.quit()