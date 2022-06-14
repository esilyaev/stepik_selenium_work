import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions


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
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        options.add_experimental_option(
            'prefs', {'intl.accept_language': language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = FFOptions()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
