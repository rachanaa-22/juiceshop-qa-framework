import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_home_page_loads(page: Page):
    page.goto("/")
    expect(page).to_have_title(re.compile("OWASP Juice Shop"))


@pytest.mark.smoke
@pytest.mark.api
def test_products_api_returns_data(page: Page):
    response = page.request.get("/api/Products")
    assert response.ok
    body = response.json()
    assert len(body["data"]) > 0