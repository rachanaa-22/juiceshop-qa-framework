import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.regression
def test_products_are_displayed(home_page):
    home_page.open()
    expect(home_page.product_cards.first).to_be_visible()


@pytest.mark.regression
def test_search_finds_matching_product(home_page):
    home_page.open()
    home_page.search("apple")
    expect(home_page.product_cards.first).to_contain_text("Apple")


@pytest.mark.regression
def test_search_with_no_match_shows_no_products(home_page):
    home_page.open()
    home_page.search("zzzzzzzz")
    expect(home_page.product_cards).to_have_count(0)