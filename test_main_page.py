from .pages.login_page import LoginPage
from .pages.main_page import MainPage

from selenium.webdriver.remote.webdriver import WebDriver


def test_guest_can_go_to_login_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
