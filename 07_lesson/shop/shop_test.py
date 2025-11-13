from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from authorization import Authorization
from mainPage import MainPage
from cart import Cart
from order import Order


def test_shop():
    service = Service("C:/Users/PK-1/Downloads/chromedriver-win64 (1)"
                      "/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    auth = Authorization(driver)
    auth.input_login("standard_user", "secret_sauce")
    auth.click_login()

    main = MainPage(driver)
    main.add_to_cart("Sauce Labs Backpack")
    main.add_to_cart("Sauce Labs Bolt T-Shirt")
    main.add_to_cart("Sauce Labs Onesie")
    main.click_cart()

    cart = Cart(driver)
    cart_items = cart.get_cart_items()
    assert "Sauce Labs Backpack" in cart_items
    assert "Sauce Labs Bolt T-Shirt" in cart_items
    assert "Sauce Labs Onesie" in cart_items
    cart.click_checkout()

    order = Order(driver)
    order.input_form("Alexandra", "Andronova", "12345")
    order.click_continue()

    total_text = order.get_total()
    print("Итог:", total_text)

    assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получено {
        total_text
        }"

    driver.quit()
