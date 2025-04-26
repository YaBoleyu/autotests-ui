from playwright.sync_api import sync_playwright, expect
"""
Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
Заполнит поле "Email" значением "user.name@gmail.com"
Заполнит поле "Username" значением "username"
Заполнит поле "Password" значением "password"
Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"

"""


pageUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
emailField = "//label[text()='Email']"
usernameField = "//label[text()='Username']"
passwordField = "//label[text()='Password']"
registrationButton = "//button[@data-testid='registration-page-registration-button']"
dashboardText = "//h6[text()='Dashboard']"


def test_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(pageUrl)

        email_input = page.locator(emailField)
        password_input = page.locator(passwordField)
        username_input = page.locator(usernameField)
        register_button = page.locator(registrationButton)
        dashboard_text_field = page.locator(dashboardText)

        email_input.fill("sample.user@mail.ru")
        username_input.fill("username")
        password_input.fill("someWackyPassword")
        register_button.click()
        expect(dashboard_text_field).to_be_visible()