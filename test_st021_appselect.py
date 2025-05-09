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

    # 1. Handle tutorial overlay
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

    # 2. Select an appliance, e.g. "TV (LED)"
    tv_appliance = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-title="TV (LED)"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tv_appliance)
    tv_appliance.click()
    time.sleep(1)

    # 3. Assert appliance was added to the table
    tv_row = driver.find_element(By.XPATH, "//td[contains(text(), 'TV (LED)')]/..")
    assert tv_row is not None, "TV (LED) not found in appliance list"

    print("st021 test passed!")

finally:
    driver.quit()
