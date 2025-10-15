from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service(
    "C:/Users/PK-1/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe"
    )

driver = webdriver.Firefox(service=service)

driver.implicitly_wait(16)
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

driver.implicitly_wait(19)

green_text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(green_text)

driver.quit()
