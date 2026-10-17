import json

import pytest
from playwright.sync_api import expect

FAKE_PRODUCT = {
    "id": 9999,
    "name": "Mocked Juice",
    "description": "A product that only exists inside this test",
    "price": 1.99,
    "deluxePrice": 1.99,
    "image": "apple_juice.jpg",
}


def mock_product_search(page, products):
    """Make the product search endpoint return whatever we choose."""
    page.route(
        "**/rest/products/search*",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({"status": "success", "data": products}),
        ),
    )


@pytest.mark.regression
def test_ui_shows_a_mocked_product(page, home_page):
    mock_product_search(page, [FAKE_PRODUCT])
    home_page.open()
    expect(page.get_by_text("Mocked Juice")).to_be_visible()


@pytest.mark.regression
def test_ui_handles_empty_product_list(page, home_page):
    mock_product_search(page, [])
    home_page.open()
    expect(home_page.product_cards).to_have_count(0)
