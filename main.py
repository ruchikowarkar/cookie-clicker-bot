from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Development/chromedriver.exe"
ser = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

my_dict = {
    123456789: "#buyTime machine",
    1000000: "#buyPortal",
    50000: "#buyAlchemy lab",
    7000: "#buyShipment",
    2000: "#buyMine",
    500: "#buyFactory",
    100: "#buyGrandma",
    15: "#buyCursor",
}

cookie = driver.find_element(By.CSS_SELECTOR, '#cookie')

timeout_start = time.time()

while True:
    cookie.click()
    if time.time() > timeout_start + 5:
        timeout_start = time.time()
        money = int(driver.find_element(By.CSS_SELECTOR, '#money').text)
        for key, value in my_dict.items():
            if money > int(key):
                package = driver.find_element(By.CSS_SELECTOR, value)
                package.click()
                break


# driver.close()