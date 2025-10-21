from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_fields_colors():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(
        r"C:\Users\PK-1\Downloads\edgedriver_win64\msedgedriver.exe"
        )
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(4)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
               )

    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(
        "Иван"
        )
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(
        "Петров"
        )
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(
        "Ленина, 55-3"
        )
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(
        "Москва"
        )
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(
        "Россия"
        )
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(
        "test@skypro.com"
        )
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(
        "+7985899998787"
        )
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']"
                        ).send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(
        "SkyPro"
        )

    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#first-name"))
    )

    green_fields = ["first-name", "last-name", "address", "city", "country",
                    "e-mail", "phone", "job-position", "company"]

    for field in green_fields:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, field))
            )
        border_color = element.value_of_css_property("border-color")
        assert "rgb(186, 219, 204)" in border_color, (
            f"Поле {field} не зеленое!"
        )

    zip_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "zip-code")
        ))
    zip_border = zip_input.value_of_css_property("border-color")
    assert "rgb(245, 194, 199)" in zip_border, (
        "Поле Zip code не подсвечено красным!"
    )

    driver.quit()
