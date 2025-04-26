import time

from playwright.sync_api import sync_playwright, expect
"""
Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
Заполнить форму регистрации и нажать на кнопку "Registration"
Сохранить состояние браузера
Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
Проверить наличие и текст заголовка "Courses" 
Проверить наличие и текст блока "There is no results"

"""


pageUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
emailField = "//label[text()='Email']"
usernameField = "//label[text()='Username']"
passwordField = "//label[text()='Password']"
registrationButton = "//button[@data-testid='registration-page-registration-button']"

coursesUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
coursesText = "//h6[text()='Courses']"
coursesTextBlock = "//h6[text()='There is no results']"

def test_registration_button_disabled():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(pageUrl)

        email_input = page.locator(emailField)
        password_input = page.locator(passwordField)
        username_input = page.locator(usernameField)
        register_button = page.locator(registrationButton)
        courses_text = page.locator(coursesText)
        courses_test_block = page.locator(coursesTextBlock)

        email_input.fill("sample.user@mail.ru")
        username_input.fill("username")
        password_input.fill("someWackyPassword")
        expect(register_button).to_be_enabled()
        register_button.click()
        context.storage_state(path="browser-state.json")
        page.goto(coursesUrl)
        expect(courses_text).to_be_visible()
        expect(courses_test_block).to_be_visible()
        expect(courses_test_block).to_have_text('There is no results')
        time.sleep(2)
