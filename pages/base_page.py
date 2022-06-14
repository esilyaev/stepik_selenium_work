from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        self.browser: WebDriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: By, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True
