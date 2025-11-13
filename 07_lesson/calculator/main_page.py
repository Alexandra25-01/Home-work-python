from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java"
                        "/slow-calculator.html")
        self.driver.maximize_window()

    def delay_clear(self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    def set_delay(self, value):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(value)

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
