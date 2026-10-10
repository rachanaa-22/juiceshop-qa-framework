import json
import uuid

import pytest

from api.client import JuiceShopClient
from pages.basket_page import BasketPage
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
def api(playwright, base_url):
    request_context = playwright.request.new_context(base_url=base_url)
    yield JuiceShopClient(request_context)
    request_context.dispose()


@pytest.fixture
def new_user(api):
    """Create a brand-new user through the API so every test is isolated."""
    email = f"qa_{uuid.uuid4().hex[:10]}@example.com"
    password = "Test@12345"
    response = api.register(email, password)
    assert response.status == 201, response.text()
    return {"email": email, "password": password}


@pytest.fixture
def logged_in_page(page, api, new_user, base_url):
    """A browser page that is already logged in as a fresh user (no UI login)."""
    response = api.login(new_user["email"], new_user["password"])
    assert response.ok, response.text()
    page.add_init_script(
        f"localStorage.setItem('token', {json.dumps(api.token)});"
        f"sessionStorage.setItem('bid', {json.dumps(str(api.basket_id))});"
    )
    page.context.add_cookies([{"name": "token", "value": api.token, "url": base_url}])
    return page


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def basket_page(logged_in_page) -> BasketPage:
    return BasketPage(logged_in_page)