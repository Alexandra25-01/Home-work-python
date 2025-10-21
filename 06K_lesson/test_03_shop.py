from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    service = Service(
        "C:/Users/PK-1/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe"
        )

    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(4)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(
        "standard_user"
        )
    driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(
        "secret_sauce"
        )
    driver.find_element(By.CSS_SELECTOR, "input.submit-button").click()

    driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack"
        ).click()
    driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
    driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie"
        ).click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "button#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys(
        "Alexandra"
        )
    driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys(
        "Andronova"
        )
    driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys(
        "101600"
        )
    driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    WebDriverWait(driver, 4).until(
        EC.text_to_be_present_in_element((
            By.CLASS_NAME, "summary_total_label"
            ), "$58.29")
            )

    driver.quit()
