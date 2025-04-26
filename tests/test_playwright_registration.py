import pytest
from playwright.sync_api import sync_playwright, expect, Page
"""
Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
Заполнит поле "Email" значением "user.name@gmail.com"
Заполнит поле "Username" значением "username"
Заполнит поле "Password" значением "password"
Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"

"""
pageUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

@pytest.mark.regression
@pytest.mark.authorization
def test_registration(chromium_page: Page):
    chromium_page.goto(pageUrl)

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    register_button = chromium_page.get_by_test_id('registration-page-registration-button')
    dashboard_text_field = chromium_page.get_by_test_id('dashboard-toolbar-title-text')

    email_input.fill("sample.user@mail.ru")
    username_input.fill("username")
    password_input.fill("someWackyPassword")
    register_button.click()
    expect(dashboard_text_field).to_be_visible()

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):  # Теперь используем фикстуру
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()