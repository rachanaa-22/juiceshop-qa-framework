import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def dismiss_overlays(context, base_url):
    """Pre-set the cookies that hide Juice Shop's welcome and cookie banners."""
    context.add_cookies([
        {"name": "welcomebanner_status", "value": "dismiss", "url": base_url},
        {"name": "cookieconsent_status", "value": "dismiss", "url": base_url},
    ])


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page)