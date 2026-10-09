from playwright.sync_api import Page

from pages.base_page import BasePage


class HomePage(BasePage):
    path = "/#/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.product_cards = page.locator("mat-card")
        self.search_icon = page.locator("#searchQuery")
        self.search_input = page.locator("app-mat-search-bar input")

    def search(self, term: str):
        self.search_icon.click()
        self.search_input.fill(term)
        self.search_input.press("Enter")