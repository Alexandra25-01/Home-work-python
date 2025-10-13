from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/PK-1/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/dynamicid")
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()
