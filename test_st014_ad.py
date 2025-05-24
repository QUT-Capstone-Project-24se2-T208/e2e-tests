from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from init_test import init_driver
from config import  test_host

 
try:
    driver = init_driver()
    
    driver.get(f"{test_host}/advanced.html") 
     
    print("start test")
    step_items = driver.find_elements(By.CLASS_NAME, "step-item")
    
    assert len(step_items) == 5, "step-items is not 5, but " + str(len(step_items))
    assert "active" in step_items[0].get_attribute("class"), "step-items 0 is not active, but " + step_items[0].get_attribute("class")
    time.sleep(2)
 
    #  goto next step
    
    next_btn = driver.find_element(By.CLASS_NAME, "next-btn")  
    next_btn.click()
    time.sleep(5)
 
    assert "completed" in step_items[0].get_attribute("class"), "step-items 0 is not completed, but " + step_items[0].get_attribute("class")
    assert "active" in step_items[1].get_attribute("class"), "step-items 1 is not active, but " + step_items[0].get_attribute("class")
 
    #  goto next step
    print("leave Usage page")
    next_btn = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[2]/div[3]/button[2]")
    next_btn.click()
    print("goto next   page")
    
    time.sleep(2)
    assert "completed" in step_items[0].get_attribute("class"), "step-items 0 is not completed, but " + step_items[0].get_attribute("class")
    assert "completed" in step_items[1].get_attribute("class"), "step-items 1 is not completed, but " + step_items[0].get_attribute("class")
    assert "active" in step_items[2].get_attribute("class"), "step-items 2 is not active, but " + step_items[0].get_attribute("class")

    
    #  goto next step
    next_btn = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[3]/div[3]/button[2]")
    next_btn.click()
    time.sleep(2)
    assert "completed" in step_items[0].get_attribute("class"), "step-items 0 is not completed, but " + step_items[0].get_attribute("class")
    assert "completed" in step_items[1].get_attribute("class"), "step-items 1 is not completed, but " + step_items[0].get_attribute("class")
    assert "completed" in step_items[2].get_attribute("class"), "step-items 2 is not completed, but " + step_items[0].get_attribute("class")
    assert "active" in step_items[3].get_attribute("class"), "step-items 3 is not active, but " + step_items[0].get_attribute("class")


    panel_calculate_btn = driver.find_element(By.ID, "panel-calculate-btn")
    panel_calculate_btn.click()
    time.sleep(10)
    assert "completed" in step_items[0].get_attribute("class"), "step-items 0 is not completed, but " + step_items[0].get_attribute("class")
    assert "completed" in step_items[1].get_attribute("class"), "step-items 1 is not completed, but " + step_items[0].get_attribute("class")
    assert "completed" in step_items[2].get_attribute("class"), "step-items 2 is not completed, but " + step_items[0].get_attribute("class")
    assert "completed" in step_items[3].get_attribute("class"), "step-items 3 is not completed, but " + step_items[0].get_attribute("class")
    assert "active" in step_items[4].get_attribute("class"), "step-items 4 is not active, but " + step_items[0].get_attribute("class")

    results_popup = driver.find_element(By.ID, "results-popup")
    assert results_popup.is_displayed(), "results-popup is not displayed"
    
    popup_close_btn = driver.find_element(By.ID, "popup-close-btn")
    popup_close_btn.click() 
    time.sleep(2)
    
    month_selector = driver.find_element(By.ID, "month-selector")
    month_selector.send_keys("January")
    time.sleep(5)


finally:
    driver.quit()