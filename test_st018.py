from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC

from init_test import init_driver
from config import  test_host

 
try:
    driver = init_driver()
    
    driver.get(f"{test_host}/assistive.html") 
    time.sleep(1)
 
 
    # 2. click bedroom2
    bedroom2_buttons = driver.find_element(By.ID, "bedroom2-label")
    bedroom2_buttons.click()
    time.sleep(2)
 
    # 3. goto next step
    to_step_2_buttons = driver.find_element(By.ID, "to-step-2")

    to_step_2_buttons.click()
    time.sleep(2)


    # 5. goto next step
    to_step_3_buttons = driver.find_element(By.ID, "to-step-3")
    to_step_3_buttons.click()
    time.sleep(2)
    
    original_window = driver.current_window_handle
    print_results = driver.find_element(By.ID, "print-results")
    print_results.click()
    time.sleep(2)
 
    all_windows = driver.window_handles
    if len(all_windows) > 1:
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
                print("switch to ", driver.title)
                assert "Solar Calculator Results" in driver.title, "print window is not opened"
                break
    else:
        assert False, "print window is not opened"
        

    time.sleep(2)   

    
finally:
    driver.quit()
    
    