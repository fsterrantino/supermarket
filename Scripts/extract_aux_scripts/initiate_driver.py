from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def initiate_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.maximize_window()
    url = 'https://www.jumbo.com.ar/'

    try:
        driver.get(url)
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)
    return driver, wait