import pytest
from pages.login_page import LoginPage
from config import BASE_URL

@pytest.fixture
def page(browser):
    context = browser.new_context(base_url = BASE_URL)
    page = context.new_page()
    return page

@pytest.fixture
def credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def logged_in_page(page, credentials):
    login = LoginPage(page)
    login.navigate()
    login.login(credentials["username"], credentials["password"])
    return page

def pytest_configure(config):
    config._metadata = {
        "Project": "Playwright QA framework",
        "Tester": "Daniel",
        "Environment": "QA"
    }