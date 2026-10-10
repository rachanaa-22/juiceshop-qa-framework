from playwright.sync_api import Page

from pages.base_page import BasePage


class BasketPage(BasePage):
    path = "/#/basket"

    def __init__(self, page: Page):
        super().__init__(page)
        self.items = page.locator("mat-row")