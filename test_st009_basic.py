from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from init_test import init_driver
from config import test_host

try:
    driver = init_driver()
    driver.get(f"{test_host}/basic.html")

    # 1. Handle tutorial overlay if present
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

    # 2. Select 2 Bedrooms template
    bedroom_button = driver.find_element(By.CSS_SELECTOR, ".template-btn[data-bedrooms='2']")
    bedroom_button.click()
    time.sleep(2)

    # 3. Track how many rows exist before adding
    rows_before = driver.find_elements(By.CSS_SELECTOR, "#appliance-list tr")

    # 4. Wait for and scroll to "Custom Appliance"
    custom_appliance = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-title='Custom Appliance']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", custom_appliance)

    # 5. Wait for any tooltip to disappear
    try:
        tooltip = driver.find_element(By.CLASS_NAME, "tutorial-tooltip")
        WebDriverWait(driver, 5).until(EC.invisibility_of_element(tooltip))
        time.sleep(0.3)
    except:
        pass

    # 6. Click the Custom Appliance
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-title='Custom Appliance']"))
    ).click()
    time.sleep(1)

    # 7. Wait until a new row is added to the table
    WebDriverWait(driver, 5).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#appliance-list tr")) > len(rows_before)
    )

    # 8. Get the new row (assumed last)
    all_rows = driver.find_elements(By.CSS_SELECTOR, "#appliance-list tr")
    appliance_row = all_rows[-1]

    # 9. Modify wattage and hours
    wattage_input = appliance_row.find_element(By.CLASS_NAME, "wattage")
    wattage_input.clear()
    wattage_input.send_keys("-10")
    time.sleep(0.5)
    wattage_input.clear()
    wattage_input.send_keys("27")

    hours_input = appliance_row.find_element(By.CLASS_NAME, "hours-per-day")
    hours_input.clear()
    hours_input.send_keys("-2")
    time.sleep(0.5)
    hours_input.clear()
    hours_input.send_keys("2")
    time.sleep(1)

    # 10. Validate field values
    assert wattage_input.get_attribute("value") == "27", "Wattage not set to 27"
    assert hours_input.get_attribute("value") == "2", "Hours not set to 2"

    # 11. Check average energy per day
    avg_energy = float(driver.find_element(By.ID, "total-kwh-per-day").text)
    assert 7.16 <= avg_energy <= 7.21, f"Expected avg kWh 7.16–7.21, got {avg_energy}"

    print("st009 test passed!")

finally:
    driver.quit()
