import pytest
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru ... etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        if sys.platform == 'win32':
            path = get_path_to_driver_chorme()
        service = Service(path)

        options = Options()

        options.add_argument('--disable-gpu')
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        options.add_experimental_option(
            'prefs', {'intl.accept_language': language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = FFOptions()
        fp.set_preference("intl.accept_languages", language)

        if sys.platform == 'win32':
            path = get_path_to_driver_ff()
        service = FFService(executable_path=path)

        browser = webdriver.Firefox(service=service, options=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


def get_path_to_driver_chorme():
    return os.path.join(os.path.dirname(__file__), './driver/chromedriver.exe')


def get_path_to_driver_ff():
    return os.path.join(os.path.dirname(__file__), './driver/geckodriver.exe')
