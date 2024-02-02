from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def initiate_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.maximize_window()
    
    return driver, wait