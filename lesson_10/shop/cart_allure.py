from selenium.webdriver.common.by import By
import allure


class Cart:
    def __init__(self, driver):
        """
        Конструктор класса Cart.

        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Получение списка товаров в корзине")
    def get_cart_items(self) -> list[str]:
        """
        Получает список названий товаров в корзине.

        :return: list[str] — список названий товаров
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    @allure.step("Нажатие кнопки 'Checkout'")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()
