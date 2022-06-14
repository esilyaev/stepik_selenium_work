from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_bucket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BUCKET), "Add to bucket not found on page"
        name = self.get_product_name()
        price = self.get_product_price()

        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET)
        btn.click()

        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
