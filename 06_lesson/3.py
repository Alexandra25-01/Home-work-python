from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(
    "C:/Users/PK-1/Downloads/chromedriver-win64 (1)/chromedriver-win64"
    "/chromedriver.exe"
    )
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

src = driver.find_element(By.CSS_SELECTOR, 'img#award').get_attribute("src")
print(src)
