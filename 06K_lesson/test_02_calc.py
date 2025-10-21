from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    service = Service(
        "C:/Users/PK-1/Downloads/chromedriver-win64 (1)/chromedriver-win64"
        "/chromedriver.exe"
        )
    driver = webdriver.Chrome(service=service)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
    driver.find_element(By.XPATH, "//span[text() = '7']").click()
    driver.find_element(By.XPATH, "//span[text() = '+']").click()
    driver.find_element(By.XPATH, "//span[text() = '8']").click()
    driver.find_element(By.XPATH, "//span[text() = '=']").click()

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
            )

    driver.quit()
