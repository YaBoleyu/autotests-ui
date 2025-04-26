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


page_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
courses_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"


def test_empty_courses_list():
        with sync_playwright() as playwright:
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
            expect(register_button).to_be_enabled()
            register_button.click()
            context.storage_state(path="browser-state.json")
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(storage_state='browser-state.json')
            page = context.new_page()

            courses_text = page.get_by_test_id("courses-list-toolbar-title-text")
            courses_test_block = page.get_by_test_id("courses-list-empty-view-title-text")

            page.goto(courses_url)
            expect(courses_text).to_be_visible()
            expect(courses_test_block).to_be_visible()
            expect(courses_test_block).to_have_text('There is no results')