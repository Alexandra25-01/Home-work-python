from selenium.webdriver.common.by import By
import allure


class Order:
    def __init__(self, driver):
        """
        Конструктор класса Order.

        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step(
        "Заполнение формы заказа: {first_name} {last_name}, "
        "почтовый код {postal_code}"
    )
    def input_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет форму с информацией о покупателе.

        :param first_name: str — имя
        :param last_name: str — фамилия
        :param postal_code: str — почтовый код
        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "input#first-name"
        ).send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input#last-name"
        ).send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input#postal-code"
        ).send_keys(postal_code)

    @allure.step("Нажатие кнопки 'Continue'")
    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления заказа.

        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "input#continue"
        ).click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self) -> str:
        """
        Получает текст с итоговой суммой заказа.

        :return: str — итоговая сумма
        """
        total = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        ).text
        return total
