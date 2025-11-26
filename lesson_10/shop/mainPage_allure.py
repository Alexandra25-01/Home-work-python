from selenium.webdriver.common.by import By
import allure


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Добавление товара '{product_name}' в корзину")
    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.

        :param product_name: str — название товара
        :return: None
        """

        self.driver.find_element(
            By.XPATH,
            (
                f"//div[text()='{product_name}']"
                f"/ancestor::div[@class='inventory_item']"
                f"//button[text()='Add to cart']"
                    )
                        ).click()

    @allure.step("Переход в корзину")
    def click_cart(self) -> None:
        """
        Переходит в корзину покупок.

        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
            ).click()
