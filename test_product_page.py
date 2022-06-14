from .pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver


def test_guest_can_add_product_to_basket(browser: WebDriver):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(url=url, browser=browser)
    product_page.open()
    product_page.add_to_bucket()
