from playwright.sync_api import Page, expect

from pages.base_page import BasePage

pageUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_text_field = page.get_by_test_id('dashboard-toolbar-title-text')

    def validate_dashboard_text(self):
        expect(self.dashboard_text_field).to_be_visible()