from selenium.webdriver.common.by import By


class Authorization:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def input_login(self, user_name, password):
        self.driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(
            user_name
            )
        self.driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(
            password
            )

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
