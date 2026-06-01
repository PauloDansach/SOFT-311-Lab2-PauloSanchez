import sys
import os
import pytest
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

SCREENSHOTS_DIR = "screenshots"


@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    context.close()


def pytest_configure(config):
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if call.when == "call":
        page = item.funcargs.get("page")
        if page is None:
            return

        safe_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
        screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{safe_name}.png")

        try:
            page.screenshot(path=screenshot_path, full_page=True)
        except Exception:
            return

        if report.when == "call":
            try:
                from pytest_html import extras
                extra = getattr(report, "extras", [])
                extra.append(extras.image(screenshot_path))
                report.extras = extra
            except ImportError:
                pass