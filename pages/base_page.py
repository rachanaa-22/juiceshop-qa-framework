from playwright.sync_api import Page


class BasePage:
    path = "/"

    def __init__(self, page: Page):
        self.page = page
        # The basket button only appears when a user is logged in
        self.basket_button = page.get_by_role("button", name="Show the shopping cart")

    def open(self):
        self.page.goto(self.path)
        return self