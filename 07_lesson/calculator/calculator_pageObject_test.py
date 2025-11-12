from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main_page import MainPage


def test_calculator():
    service = Service(
        "C:/Users/PK-1/Downloads/chromedriver-win64 (1)/chromedriver-win64"
        "/chromedriver.exe"
    )
    driver = webdriver.Chrome(service=service)
    main_page = MainPage(driver)
    main_page.delay_clear()
    main_page.set_delay("45")
    main_page.click_button("7")
    main_page.click_button("+")
    main_page.click_button("8")
    main_page.click_button("=")
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"), "15")
    )
    result = main_page.get_result()
    assert result == "15"
    driver.quit()
