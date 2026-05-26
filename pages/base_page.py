from playwright.sync_api import Page


class BasePage:
    """Clase base para todas las páginas del POM."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate(self, path: str = ""):
        self.page.goto(f"{self.base_url}{path}")
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url
