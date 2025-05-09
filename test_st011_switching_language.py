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
    
    # 1.close tutorialOverlay
    tutorialOverlay = driver.find_element(By.ID, "tutorialOverlay")
    assert  tutorialOverlay.is_displayed(), "tutorialOverlay is not displayed"
    
    gotItBtn = driver.find_element(By.ID, "gotItBtn")
    assert  gotItBtn.is_displayed(), "gotItBtn is not displayed"
    
    gotItBtn.click()
    time.sleep(2)
    
    
    language_buttons = driver.find_elements(By.CLASS_NAME, "lang-btn")
 
    assert len(language_buttons) == 2, "Expected 2 language buttons, but found {}".format(len(language_buttons))
       
     
    for button in language_buttons:
        language_name = button.text.strip()
        print(f"Switching to language: {language_name}")

        button.click()
        time.sleep(2)

        home_type_question = driver.find_element(By.ID, "home-type-question").text.strip()
        print(f"Header text after switching to {language_name}: {home_type_question}")

        if language_name == "English":
            assert "What type of home do you have?" in home_type_question, "Language switch to English failed"
        elif language_name == "Tok Pisin":
            assert "Wanem kain haus yu gat?" in home_type_question, "Language switch to TokPisin failed"
        else:
            assert False, f"Unexpected language: {language_name}"
        
    print("Language switch test completed successfully!")
    time.sleep(2)
 
finally:
    driver.quit()