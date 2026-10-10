import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_item_added_via_api_appears_in_basket_ui(api, logged_in_page, basket_page):
    # Arrange through the API (fast), assert through the UI (what the user sees)
    api.add_to_basket(product_id=1)
    product_name = api.get_product(1).json()["data"]["name"]

    basket_page.open()

    expect(basket_page.items).to_have_count(1)
    expect(basket_page.items.first).to_contain_text(product_name)


@pytest.mark.regression
def test_new_user_basket_is_empty(basket_page):
    basket_page.open()
    expect(basket_page.items).to_have_count(0)