import pytest
from playwright.sync_api import Page, Playwright

from pages.login_page import LoginPage



@pytest.fixture(scope="session")
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()