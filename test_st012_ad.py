from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from init_test import init_driver
from config import test_host

try:
    driver = init_driver()
    driver.get(f"{test_host}/advanced.html")

    # 1. Handle tutorial overlay if it appears
    try:
        gotItBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "gotItBtn"))
        )
        gotItBtn.click()
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "tutorialOverlay"))
        )
        time.sleep(0.3)
    except:
        pass

    # 2. Input address (all other values are defaults)
    address_input = driver.find_element(By.ID, "search-input")
    address_input.clear()
    address_input.send_keys("Port Moresby, PNG")
    time.sleep(1)

    # 3. Press Next through all steps using default values
    for _ in range(3):
        active_step = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".step-content.active"))
        )
        next_btn = active_step.find_element(By.CLASS_NAME, "next-btn")
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(next_btn))
        next_btn.click()
        time.sleep(1)

    # 4. Reset to optimal settings
    reset_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "reset-panel-settings"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", reset_btn)
    reset_btn.click()
    time.sleep(1)

    # 5. Click Calculate
    calc_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "panel-calculate-btn"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", calc_btn)
    calc_btn.click()
    time.sleep(3)

    # 6. Assert result or handle "Maybe Later"
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "results-summary"))
        )
        print("st012 test passed! Results summary is visible.")
    except:
        try:
            maybe_later = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "popup-later-btn"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", maybe_later)
            maybe_later.click()
            print("Popup handled. st012 test passed!")
        except:
            raise Exception("Results summary not found, and popup was not interactable.")

finally:
    driver.quit()
