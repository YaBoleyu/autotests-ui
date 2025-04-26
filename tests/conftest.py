import pytest
from playwright.sync_api import Playwright, Page, sync_playwright

page_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
courses_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"

@pytest.fixture(scope="session")
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(page_url)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    register_button = page.get_by_test_id('registration-page-registration-button')

    email_input.fill("sample_user@mail.ru")
    username_input.fill("username")
    password_input.fill("someWackyPassword")
    register_button.click()
    page.wait_for_timeout(2000)

    context.storage_state(path="../browser-state.json")
    browser.close()


@pytest.fixture(autouse=True)
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="../browser-state.json")
    page = context.new_page()
    yield page
    context.close()
    browser.close()