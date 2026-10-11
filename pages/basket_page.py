from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class BasketPage(BasePage):
    path = "/#/basket"

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.locator("#checkoutButton")

    def product(self, name: str) -> Locator:
        return self.page.get_by_text(name).first