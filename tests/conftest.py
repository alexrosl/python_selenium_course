import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from src.base.webdriverfactory import WebDriverFactory
from src.pages.home.navigation_page import NavigationPage
from src.utilities.constants import Constants
from src.pages.home.login_page import LoginPage


@pytest.yield_fixture()
def setup():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver
    driver.get(Constants().base_url)

    yield driver
    print("Running one time tearDown")
    driver.quit()


@pytest.yield_fixture(scope="class")
def one_time_setup_login(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver
    driver.get(Constants.base_url)
    login_page = LoginPage(driver)
    nav_page = NavigationPage(driver)
    try:
        driver.find_element(By.XPATH, login_page.successful_login)
    except NoSuchElementException:
        login_page.login(Constants.login, Constants.password)

    yield driver
    nav_page.logout()
    print("Running one time tearDown")

    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")