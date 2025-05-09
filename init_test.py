
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import driver_path

def init_driver():
    print("Initializing Service...")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    return driver
