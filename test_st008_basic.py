from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from init_test import init_driver
from config import test_host

try:
    driver = init_driver()
    driver.get(f"{test_host}/")

    # 1. Click on Basic mode tab
    basic_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-mode="basic"]'))
    )
    basic_tab.click()
    time.sleep(1)

    # 2. Click on "Use Basic Calculator" button
    basic_button = driver.find_element(By.CSS_SELECTOR, 'a.basic.mode-button')
    basic_button.click()

    # 3. Handle tutorial overlay using gotItBtn
    try:
        gotItBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "gotItBtn"))
        )
        gotItBtn.click()

        # Wait until overlay is gone
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "tutorialOverlay"))
        )
        time.sleep(0.3)  # Allow time for animations to finish
    except:
        pass

    # 4. Select 1 Bedroom template
    bedroom1_btn = driver.find_element(By.CSS_SELECTOR, 'button[data-bedrooms="1"]')
    bedroom1_btn.click()
    time.sleep(1)

    # 5. Add TV (LED)
    tv_appliance = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-title="TV (LED)"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tv_appliance)
    time.sleep(0.3)
    tv_appliance.click()
    time.sleep(1)

    # 6. Change TV hours to 8
    tv_row = driver.find_element(By.XPATH, "//td[contains(text(), 'TV (LED)')]/..")
    tv_hour_input = tv_row.find_element(By.CLASS_NAME, "hours-per-day")
    tv_hour_input.clear()
    tv_hour_input.send_keys("8")
    time.sleep(1)

    # 7. Change Simultaneous Usage to 70%
    usage_select = driver.find_element(By.ID, "simultaneous-usage")
    usage_select.send_keys("70")
    time.sleep(1)

    # 8. Set Reserve Days to 0.5
    reserve_input = driver.find_element(By.ID, "reserve-days")
    reserve_input.clear()
    reserve_input.send_keys("0.5")
    time.sleep(1)

    # 9. Set Sun Hours to 1
    sun_hours_input = driver.find_element(By.ID, "sun-hours")
    sun_hours_input.clear()
    sun_hours_input.send_keys("1")
    time.sleep(1)

    # 10. Validate inverter, solar panel, battery are not empty
    inverter = driver.find_element(By.ID, "inverter-size").text.strip()
    solar = driver.find_element(By.ID, "solar-panel-size").text.strip()
    battery = driver.find_element(By.ID, "battery-capacity").text.strip()

    print("Inverter:", inverter)
    print("Solar Panels:", solar)
    print("Battery:", battery)

    assert inverter != "", "Inverter recommendation is empty"
    assert solar != "", "Solar panel recommendation is empty"
    assert battery != "", "Battery recommendation is empty"

    print("st008 test passed!")

finally:
    driver.quit()
