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
    
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert tutorialOverlay is None or not tutorialOverlay.is_displayed(), "tutorialOverlay is  displayed"
 
    time.sleep(3)
    
    # Test closeTutorialBtn click event
    driver.refresh()
    time.sleep(5)
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert  tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
    closeTutorialBtn = driver.find_element(By.ID, "closeTutorialBtn")
    assert  closeTutorialBtn.is_displayed(), "closeTutorialBtn is not displayed"
    
    closeTutorialBtn.click()
    
    time.sleep(2)
    
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert tutorialOverlay is None or not tutorialOverlay.is_displayed(), "tutorialOverlay is  displayed"
 
    time.sleep(3)
     
    
    # Test dontShowAgain click event
    driver.refresh()
    time.sleep(5)
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert  tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
    closeTutorialBtn = driver.find_element(By.ID, "closeTutorialBtn")
    assert  closeTutorialBtn.is_displayed(), "closeTutorialBtn is not displayed"

    dontShowAgain = driver.find_element(By.ID, "dontShowAgain")
    assert  dontShowAgain.is_displayed(), "dontShowAgain is not displayed"
    
    dontShowAgain.click()
    time.sleep(2)
    closeTutorialBtn.click()
    time.sleep(2)
    
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert tutorialOverlay is None or not tutorialOverlay.is_displayed(), "tutorialOverlay is  displayed"
 
    time.sleep(3)
    
    driver.refresh()
    time.sleep(5)
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert not  tutorialOverlay.is_displayed(), "tutorialOverlay is displayed"
    
    time.sleep(3)
    
finally:
    driver.quit()