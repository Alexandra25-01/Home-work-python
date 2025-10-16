from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(
    "C:/Users/PK-1/Downloads/chromedriver-win64 (1)/chromedriver-win64"
    "/chromedriver.exe"
    )
driver = webdriver.Chrome(service=service)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

waiter = WebDriverWait(driver, 10)
image1 = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "img#compass"))
)
image2 = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "img#calendar"))
)

image3 = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "img#award"))
)

image4 = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "img#landscape"))
)

src = driver.find_element(By.CSS_SELECTOR, 'img#award').get_attribute("src")
print(src)
