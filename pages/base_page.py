import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import math


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

    def solve_quiz_and_get_code(self):
        time.sleep(1)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(60)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
