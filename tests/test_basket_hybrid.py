import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_item_added_via_api_appears_in_basket_ui(api, basket_page):
    product_name = api.get_product(1).json()["data"]["name"]

    # Step 1: arrange through the API, and prove it worked
    add_response = api.add_to_basket(product_id=1)
    assert add_response.ok, add_response.text()
    basket_products = api.get_basket().json()["data"]["Products"]
    assert 1 in [product["id"] for product in basket_products]

    # Step 2: assert through the UI
    basket_page.open()
    expect(basket_page.product(product_name)).to_be_visible()


@pytest.mark.regression
def test_new_user_basket_is_empty(api, basket_page):
    assert api.get_basket().json()["data"]["Products"] == []

    basket_page.open()
    expect(basket_page.checkout_button).to_be_visible()