from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service("C:/Users/PK-1/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")

driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")

username = "input#username"
password = "input#password"
button_login = "i.fa"

username_input = driver.find_element(By.CSS_SELECTOR, username)
username_input.send_keys("tomsmith")
password_input = driver.find_element(By.CSS_SELECTOR, password)
password_input.send_keys("SuperSecretPassword!")
sleep(3)
button = driver.find_element(By.CSS_SELECTOR, button_login)
button.click()
sleep(3)

green_text = driver.find_element(By.CSS_SELECTOR, "div#flash").text
print(green_text)

driver.quit()
