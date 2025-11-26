from selenium.webdriver.common.by import By
import allure


class Authorization:
    def __init__(self, driver):
        """
        Конструктор класса Authorization.

        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    @allure.step("Ввод логина '{user_name}' и пароля")
    def input_login(self, user_name: str, password: str) -> None:
        """
        Вводит логин и пароль на странице авторизации.

        :param user_name: str — имя пользователя
        :param password: str — пароль пользователя
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(
            user_name
            )
        self.driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(
            password
            )

    @allure.step("Нажатие кнопки логина")
    def click_login(self) -> None:
        """
        Нажимает кнопку "Login".

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
