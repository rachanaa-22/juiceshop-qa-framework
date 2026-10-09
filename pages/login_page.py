from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    path = "/#/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#loginButton")
        self.error_message = page.locator(".error")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()