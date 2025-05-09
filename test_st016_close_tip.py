from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from init_test import init_driver
from config import  test_host

try:
    driver = init_driver()

    driver.get(f"{test_host}/simple.html") 

    # Test gotItBtn click event
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert  tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
    gotItBtn = driver.find_element(By.ID, "gotItBtn")
    assert  gotItBtn.is_displayed(), "gotItBtn is not displayed"
    
    gotItBtn.click()
    
    time.sleep(2)
    
    openTutorialBtn = driver.find_element(By.ID, "openTutorialBtn")
    assert openTutorialBtn.is_displayed(), "openTutorialBtn is not displayed"
    
    openTutorialBtn.click()
    time.sleep(0.5)    
    
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
 
    time.sleep(3)
    
finally:
    driver.quit()