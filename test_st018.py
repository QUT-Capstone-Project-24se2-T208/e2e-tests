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
    
    driver.get(f"{test_host}/simple.html") 
    time.sleep(1)
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
        
 
    print_button = driver.find_element(By.CLASS_NAME, "print-button")
    print_button.click()
    time.sleep(2)   

    all_windows = driver.window_handles
    assert len(all_windows) != 3, "system print window is not found"
    
    time.sleep(2)
    
finally:
    driver.quit()
    
    