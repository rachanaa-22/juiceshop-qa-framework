import allure
import pytest
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import expect

# Baseline: the test fails only if serious/critical violations go ABOVE this number.
# Run once, read the printed counts, then lower this to the real number.
MAX_SEVERE_VIOLATIONS = 3

PAGES = [
    ("/#/", "mat-card"),
    ("/#/login", "#email"),
]


@pytest.mark.a11y
@pytest.mark.parametrize("path, ready_selector", PAGES)
def test_page_has_no_new_severe_accessibility_violations(page, path, ready_selector):
    page.goto(path)
    expect(page.locator(ready_selector).first).to_be_visible()

    results = Axe().run(page)
    violations = results.response["violations"]
    severe = [v for v in violations if v["impact"] in ("serious", "critical")]

    summary = "\n".join(
        f"{v['impact']}: {v['id']} - {v['help']} ({len(v['nodes'])} elements)"
        for v in violations
    )
    allure.attach(
        summary or "No violations",
        name=f"axe violations for {path}",
        attachment_type=allure.attachment_type.TEXT,
    )
    print(f"\n[a11y] {path}: {len(severe)} serious/critical, {len(violations)} total")
    print(summary)

    assert len(severe) <= MAX_SEVERE_VIOLATIONS

