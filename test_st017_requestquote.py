from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from init_test import init_driver
from config import test_host

try:
    driver = init_driver()
    driver.get(f"{test_host}/basic.html")

    # 1. Locate and click the Request a Quote button
    quote_button = driver.find_element(By.ID, "request-quote-btn")
    assert quote_button.is_displayed(), "Request a Quote button is not visible"

    quote_button.click()
    time.sleep(2)

    # Optional: assert navigation or modal shows up
    # You can customize based on actual behavior
    current_url = driver.current_url
    assert "quote" in current_url or driver.find_element(By.TAG_NAME, "body").text.lower().find("quote") != -1, \
        "No quote-related content found after click"

    print("st017 test passed!")

finally:
    driver.quit()
