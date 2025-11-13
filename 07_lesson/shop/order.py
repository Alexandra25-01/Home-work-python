from selenium.webdriver.common.by import By


class Order:
    def __init__(self, driver):
        self.driver = driver

    def input_form(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.CSS_SELECTOR, "input#first-name"
            ).send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input#last-name"
            ).send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input#postal-code"
            ).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    def get_total(self):
        total = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
            ).text
        return total
