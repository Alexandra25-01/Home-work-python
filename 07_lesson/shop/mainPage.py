from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']"
                                 "/ancestor::div[@class='inventory_item']"
                                 "//button[text()='Add to cart']"
                                 ).click()

    def click_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
            ).click()
