import pytest
from playwright.sync_api import expect

from utils.config import USER_EMAIL, USER_PASSWORD


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(login_page):
    login_page.open()
    login_page.login(USER_EMAIL, USER_PASSWORD)
    expect(login_page.basket_button).to_be_visible()


@pytest.mark.regression
def test_wrong_password_shows_error(login_page):
    login_page.open()
    login_page.login(USER_EMAIL, "definitely-wrong-password")
    expect(login_page.error_message).to_contain_text("Invalid email or password")


@pytest.mark.regression
def test_empty_credentials_disable_login(login_page):
    login_page.open()
    expect(login_page.login_button).to_be_disabled()