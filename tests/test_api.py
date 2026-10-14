import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_products_list_is_not_empty(api):
    response = api.get_products()
    assert response.ok
    assert len(response.json()["data"]) > 0


@pytest.mark.api
def test_new_user_can_log_in_and_gets_token(api, new_user):
    response = api.login(new_user["email"], new_user["password"])
    assert response.status == 200
    assert api.token
    assert api.basket_id


@pytest.mark.api
def test_login_with_wrong_password_is_rejected(api, new_user):
    response = api.login(new_user["email"], "wrong-password")
    assert response.status == 401


@pytest.mark.api
def test_item_can_be_added_to_basket(api, new_user):
    api.login(new_user["email"], new_user["password"])
    add_response = api.add_to_basket(product_id=1)
    assert add_response.ok, add_response.text()

    products = api.get_basket().json()["data"]["Products"]
    assert any(product["id"] == 1 for product in products)

@pytest.mark.api
def test_single_product_has_name_and_price(api):
    response = api.get_product(1)
    assert response.ok
    product = response.json()["data"]
    assert product["name"]
    assert product["price"] > 0


@pytest.mark.api
def test_single_product_has_name_and_price(api):
    response = api.get_product(1)
    assert response.ok
    product = response.json()["data"]
    assert product["name"]
    assert product["price"] > 0
