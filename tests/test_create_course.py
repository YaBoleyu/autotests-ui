import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.authorization
def test_create_course(
                       create_course_page: CreateCoursePage):
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form("", "", "",  "0","0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form("Playwright", "2 weeks", "Playwright",  "100", "10")
    create_course_page.click_create_course_button()
    create_course_page.check_visible_create_course_title()
    create_course_page.check_visible_create_course_button()
    create_course_page.page.wait_for_timeout(2000)