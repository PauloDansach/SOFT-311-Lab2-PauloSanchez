from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object para la página principal de TestDino Store."""

    # --- Locators (verificados con playwright codegen) ---
    LOGO         = "[class*='logo'], [alt*='logo'], header img"
    PRODUCT_CARD = "[class*='product'], [class*='card'], [class*='item']"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def open(self):
        """Abre la página principal."""
        self.navigate("/")

    def is_logo_visible(self) -> bool:
        """Retorna True si el logo del sitio es visible."""
        return self.page.locator(self.LOGO).first.is_visible()

    def get_product_count(self) -> int:
        """Retorna la cantidad de productos visibles en la home."""
        return self.page.locator(self.PRODUCT_CARD).count()

    def get_nav_links_count(self) -> int:
        """Retorna la cantidad de enlaces de navegación usando get_by_role."""
        return self.page.get_by_role("link").count()