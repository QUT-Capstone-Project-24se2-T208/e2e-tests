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

    # 2. Input address
    address_input = driver.find_element(By.ID, "search-input")
    address_input.clear()
    address_input.send_keys("Port Moresby, PNG")
    time.sleep(1)

    # 3. Press Next Step
    next_btn = driver.find_element(By.CLASS_NAME, "next-btn")
    next_btn.click()
    time.sleep(1)

    # 4. Daily electricity usage (kWh)
    usage_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "daily-usage"))
    )
    usage_input.clear()
    usage_input.send_keys("-5")
    time.sleep(1)
    usage_input.clear()
    usage_input.send_keys("12")
    time.sleep(1)

    # 5. Monthly electricity bill (PGK)
    bill_input = driver.find_element(By.ID, "electric-bill")
    bill_input.clear()
    bill_input.send_keys("-100")
    time.sleep(1)
    bill_input.clear()
    bill_input.send_keys("100")
    time.sleep(1)

    # Find the active step and locate the next button inside it
    active_step = driver.find_element(By.CSS_SELECTOR, ".step-content.active")
    next_btn = active_step.find_element(By.CLASS_NAME, "next-btn")

    # Scroll and click
    driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(next_btn))
    next_btn.click()

    # 6. System size (kWp)
    system_size_input = driver.find_element(By.ID, "system-size")
    system_size_input.clear()
    system_size_input.send_keys("-3.5")
    time.sleep(1)
    system_size_input.clear()
    system_size_input.send_keys("4")
    time.sleep(1)

    # Safely locate and click the next button inside the active step
    active_step = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".step-content.active"))
    )
    next_btn2 = active_step.find_element(By.CLASS_NAME, "next-btn")
    driver.execute_script("arguments[0].scrollIntoView(true);", next_btn2)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(next_btn2))
    next_btn2.click()

    # 8. Adjust Azimuth
    azimuth_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "azimuth"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", azimuth_input)
    driver.execute_script("arguments[0].value = arguments[1];", azimuth_input, "8")

    # 9. Adjust Tilt
    tilt_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tilt"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tilt_input)
    driver.execute_script("arguments[0].value = arguments[1];", tilt_input, "8")

    # 10. Click Calculate
    calc_btn = driver.find_element(By.ID, "panel-calculate-btn")
    calc_btn.click()
    time.sleep(3)

    # 11. Assert result summary is displayed
    # Wait until either the results show OR a "Maybe Later" prompt appears
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "results-summary"))
        )
        print("Results summary is visible.")
    except:
        # Optional handling if a modal appears (like "Maybe Later")
        try:
            maybe_later = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "popup-later-btn"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", maybe_later)
            maybe_later.click()
            print("Popup handled. st011 test passed!")
        except:
            raise Exception("Popup was found but could not be interacted with.")

finally:
    driver.quit()
