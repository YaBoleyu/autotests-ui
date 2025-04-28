from playwright.sync_api import Page, expect

from pages.base_page import BasePage

pageUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(pageUrl)
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.register_button = page.get_by_test_id('registration-page-registration-button')
        self.dashboard_text_field = page.get_by_test_id('dashboard-toolbar-title-text')

    def fill_registration_form(self, email: str, password: str, username: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

    def click_registration_button(self):
        self.register_button.click()