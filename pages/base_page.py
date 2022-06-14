from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self, browser: WebDriver, url: str) -> None:
        self.browser: WebDriver = browser
        self.url = url

    def open(self) -> None:
        self.browser.get(self.url)
