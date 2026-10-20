from playwright.sync_api import APIRequestContext, APIResponse


class JuiceShopClient:
    """Thin wrapper around the Juice Shop REST API."""

    def __init__(self, request: APIRequestContext):
        self.request = request
        self.token: str | None = None
        self.basket_id: int | None = None

    def register(self, email: str, password: str) -> APIResponse:
        """Create a new user account (POST /api/Users)."""
        return self.request.post(
            "/api/Users",
            data={"email": email, "password": password, "passwordRepeat": password},
        )

    def login(self, email: str, password: str) -> APIResponse:
        """Log in and store the auth token and basket id for later calls."""
        response = self.request.post(
            "/rest/user/login", data={"email": email, "password": password}
        )
        if response.ok:
            auth = response.json()["authentication"]
            self.token = auth["token"]
            self.basket_id = auth["bid"]
        return response

    def _auth_headers(self) -> dict:
        """Build the Authorization header from the stored token."""
        return {"Authorization": f"Bearer {self.token}"}

    def get_products(self) -> APIResponse:
        """Fetch the full product list."""
        return self.request.get("/api/Products")

    def get_product(self, product_id: int) -> APIResponse:
        """Fetch a single product by id."""
        return self.request.get(f"/api/Products/{product_id}")

    def add_to_basket(self, product_id: int, quantity: int = 1) -> APIResponse:
        """Add a product to the logged-in user's basket."""
        return self.request.post(
            "/api/BasketItems",
            headers=self._auth_headers(),
            data={
                "ProductId": product_id,
                "BasketId": str(self.basket_id),
                "quantity": quantity,
            },
        )

    def get_basket(self) -> APIResponse:
        """Fetch the logged-in user's basket contents."""
        return self.request.get(
            f"/rest/basket/{self.basket_id}", headers=self._auth_headers()
        )
