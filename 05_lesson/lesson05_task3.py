from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/PK-1/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")

driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/inputs")

search = "[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search)
search_input.send_keys("Sky")
search_input.clear()
search_input.send_keys("Pro")
driver.quit()
