from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(
    "C:/Users/PK-1/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe"
    )

driver = webdriver.Firefox(service=service)
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

waiter = WebDriverWait(driver, 20)
green_text_element = waiter.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "p.bg-success"))
)

green_text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(green_text)

driver.quit()
