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
    time.sleep(2)
    # 1.close tutorialOverlay
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert  tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
    gotItBtn = driver.find_element(By.ID, "gotItBtn")
    assert  gotItBtn.is_displayed(), "gotItBtn is not displayed"
    
    gotItBtn.click()
    time.sleep(1)
    
    try:
        audio_status_indicator = driver.find_element(By.ID, 'audio-status-indicator')
        assert False, "audio status indicator is visible"
    except: 
        time.sleep(1)
    
    listen_buttons = driver.find_element(By.ID, 'listen-button')
    listen_buttons.click()
    time.sleep(0.5)
    
    audio_status_indicator = driver.find_element(By.ID, 'audio-status-indicator')
    audio_status_indicator_classes=audio_status_indicator.get_attribute("class")
    assert 'visible' in audio_status_indicator_classes, "audio status indicator is not visible"
    time.sleep(1)
    
    stop_buttons = driver.find_element(By.ID, 'stop-audio-button')
    stop_buttons.click()
    time.sleep(1)
       
    audio_status_indicator = driver.find_element(By.ID, 'audio-status-indicator')
    audio_status_indicator_classes=audio_status_indicator.get_attribute("class")
    assert 'visible' not in audio_status_indicator_classes, "audio status indicator is visible"
    time.sleep(1)
    
    listen_buttons = driver.find_element(By.ID, 'listen-button')
    listen_buttons.click()
    time.sleep(12)
    
    audio_status_indicator = driver.find_element(By.ID, 'audio-status-indicator')
    audio_status_indicator_classes=audio_status_indicator.get_attribute("class")
    assert 'visible' not in audio_status_indicator_classes, "audio status indicator is visible"
    time.sleep(1)
 
finally:
    driver.quit()