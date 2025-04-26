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


def test_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(pageUrl)

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        register_button = page.get_by_test_id('registration-page-registration-button')
        dashboard_text_field = page.get_by_test_id('dashboard-toolbar-title-text')

        email_input.fill("sample.user@mail.ru")
        username_input.fill("username")
        password_input.fill("someWackyPassword")
        register_button.click()
        expect(dashboard_text_field).to_be_visible()


from playwright.sync_api import sync_playwright, expect


def test_successful_registration():  # Создаем тестовую функцию
    # Все остальные действия остаются без изменений
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        page.wait_for_timeout(5000)
