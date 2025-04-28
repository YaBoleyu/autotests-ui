import pytest
from playwright.sync_api import sync_playwright, expect, Page, Playwright

from pages.courses_list_page import CoursesListPage
from pages.dashboard_page import DashboardPage

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

@pytest.mark.courses
@pytest.mark.regression
def test_with_clean_page(chromium_page: Page):
    page = chromium_page
    page.goto(page_url)
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    register_button = page.get_by_test_id('registration-page-registration-button')

    email_input.fill("sample_user@mail.ru")
    username_input.fill("username")
    password_input.fill("someWackyPassword")
    register_button.click()


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(dashboard_page_with_state: DashboardPage, courses_list_page: CoursesListPage):
    dashboard_page_with_state.page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    dashboard_page_with_state.navbar.check_visible("username")
    dashboard_page_with_state.sidebar.check_visible()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()

