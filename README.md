# juiceshop-qa-framework

Playwright + Python test automation framework for [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), built with pytest.

## What's inside

- Page Object Model for UI tests (login, home, basket)
- API client layer for registering users, logging in and managing the basket
- Hybrid tests: set up data through the API, verify in the UI
- Isolated test data: every test creates its own fresh user
- Parallel runs with pytest-xdist
- HTML report with a screenshot attached to each failed UI test

## Project structure

```
api/        API client for Juice Shop
pages/      Page objects
tests/      UI, API and hybrid tests
utils/      Config loaded from .env
conftest.py Shared fixtures
```

## How to run

1. Start Juice Shop:
```
   docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop
```
2. Create a virtual environment and install dependencies:
```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   playwright install
```
3. Copy `.env.example` to `.env` and fill in the values.
4. Run the tests:
```
   pytest -n 4
```
   The report is written to `reports/report.html`.

## Roadmap

- [ ] Network mocking, accessibility and visual regression tests
- [ ] GitHub Actions CI pipeline
- [ ] Allure report published to GitHub Pages