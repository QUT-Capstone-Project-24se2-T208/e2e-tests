from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from config import  test_host
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
    
    
    

 
    # 2. click select 2 bedrooms
    bedroom2_buttons = driver.find_element(By.CSS_SELECTOR, 'button[data-bedrooms="2"]')
    bedroom2_buttons.click()
    time.sleep(1)

     
    # 4. LED Lights (10x)
    div_led_lights = driver.find_element(By.CSS_SELECTOR, 'div[data-title="LED Lights (10x)"]')
    div_led_lights.click()
    time.sleep(1)
    

    # test total-kwh-value
    total_value = driver.find_element(By.ID, "total-load-kw")
    assert "3.71"== total_value.text, "test total-kwh-value failed, expected 3.71, but got " + total_value.text

    time.sleep(3)
    
    # goto home page
    home_btn = driver.find_element(By.XPATH, '/html/body/div[4]')
    home_btn.click()
    time.sleep(1)
    
    assert driver.current_url == f"{test_host}/index.html", "test goto home page failed"

finally:
    driver.quit()