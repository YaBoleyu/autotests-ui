import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
"""
Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
Заполнит поле "Email" значением "user.name@gmail.com"
Заполнит поле "Username" значением "username"
Заполнит поле "Password" значением "password"
Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"

"""


@pytest.mark.regression
@pytest.mark.authorization
def test_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.fill_registration_form("username@mail.com","123321","username")
    registration_page.click_registration_button()
    dashboard_page.validate_dashboard_text()

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