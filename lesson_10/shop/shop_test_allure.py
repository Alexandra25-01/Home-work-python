import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from authorization_allure import Authorization
from mainPage_allure import MainPage
from cart_allure import Cart
from order_allure import Order
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    chrome_driver_path = (
        "C:/Users/PK-1/Downloads/chromedriver-win64 (1)/"
        "chromedriver-win64/chromedriver.exe"
    )
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Покупка нескольких товаров и проверка итоговой суммы")
@allure.description(
    "Тест проверяет добавление товаров в корзину, оформление заказа "
    "и проверку итоговой суммы."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    auth = Authorization(driver)
    with allure.step("Авторизация пользователя"):
        auth.input_login("standard_user", "secret_sauce")
        auth.click_login()

    main = MainPage(driver)
    with allure.step("Добавление товаров в корзину"):
        main.add_to_cart("Sauce Labs Backpack")
        main.add_to_cart("Sauce Labs Bolt T-Shirt")
        main.add_to_cart("Sauce Labs Onesie")
        main.click_cart()

    cart = Cart(driver)
    with allure.step("Проверка товаров в корзине"):
        cart_items = cart.get_cart_items()
        assert "Sauce Labs Backpack" in cart_items
        assert "Sauce Labs Bolt T-Shirt" in cart_items
        assert "Sauce Labs Onesie" in cart_items
        cart.click_checkout()

    order = Order(driver)
    with allure.step("Заполнение формы заказа"):
        order.input_form("Alexandra", "Andronova", "12345")
        order.click_continue()

    with allure.step("Проверка итоговой суммы заказа"):
        total_text = order.get_total()
        assert "$58.29" in total_text, (
            f"Ожидалась сумма $58.29, получено {total_text}"
        )
