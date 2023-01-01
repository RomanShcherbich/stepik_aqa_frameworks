import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

os.environ.update({"SELENIUM_CHROMEDRIVER_PATH": "/Users/romanshcherbich/PycharmProjects/StepikSelenium/chromedriver"})

STEPIK_USER = os.environ.get("STEPIK_USER")
STEPIK_PASS = os.environ.get("STEPIK_PASS")


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="es",
                     help="Choose testing locale: es, fr, etc")


@pytest.fixture(scope="session")
def browser_language(request):
    browser_language = request.config.getoption("language")
    assert browser_language, "user language param is not provided. Example: 'pytest --language=es'"
    return browser_language


@pytest.fixture(scope="function")
def browser(request, browser_language):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_service = Service(os.environ.get("SELENIUM_CHROMEDRIVER_PATH"))
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": browser_language})
        browser = webdriver.Chrome(service=chrome_service, options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
