from playwright.sync_api import sync_playwright, expect
"""
Открыть страницу регистрации: https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration.
Проверить, что кнопка "Registration" находится в состоянии disabled.
Заполнить поле Email значением: user.name@gmail.com.
Заполнить поле Username значением: username.
Заполнить поле Password значением: password.
Проверить, что кнопка "Registration" перешла в состояние enabled.

"""


pageUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
emailField = "//label[text()='Email']"
usernameField = "//label[text()='Username']"
passwordField = "//label[text()='Password']"
registrationButton = "//button[@data-testid='registration-page-registration-button']"


def test_registration_button_disabled():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(pageUrl)

        email_input = page.locator(emailField)
        password_input = page.locator(passwordField)
        username_input = page.locator(usernameField)
        register_button = page.locator(registrationButton)

        expect(register_button).to_be_disabled()
        email_input.fill("sample.user@mail.ru")
        username_input.fill("username")
        password_input.fill("someWackyPassword")
        expect(register_button).to_be_enabled()
