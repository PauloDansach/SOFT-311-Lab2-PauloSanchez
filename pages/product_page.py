from playwright.sync_api import Page
from pages.base_page import BasePage


class ProductPage(BasePage):
    """Page Object para listado de productos y acción de agregar al carrito."""

    # --- Locators (verificados con playwright codegen) ---
    ADD_TO_CART_BTN = "[data-testid='add-to-cart-button']"
    CART_ICON       = "[data-testid='header-cart-icon']"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def open(self):
        self.navigate("/")

    def go_to_first_product(self):
        """Home → Audio & Camera → JBL Charge 4."""
        self.page.get_by_role("link", name="camera Audio & Camera").click()
        self.page.wait_for_load_state("networkidle")
        self.page.get_by_role("link", name="JBL Charge 4 Bluetooth").click()
        self.page.wait_for_load_state("networkidle")

    def click_add_to_cart(self):
        """Clic en Add to cart con data-testid exacto."""
        btn = self.page.get_by_test_id("add-to-cart-button")
        btn.wait_for(state="visible")
        btn.click()
        self.page.wait_for_timeout(1000)

    def open_cart(self):
        """Navega al carrito usando navigate() directo — más confiable que clic en ícono."""
        self.navigate("/cart")

    def get_cart_item_count(self) -> int:
        """Cuenta ítems en el carrito inspeccionando cualquier elemento hijo de la lista."""
        self.page.wait_for_timeout(1000)
        selectors = [
            "[data-testid*='cart-item']",
            "[class*='CartItem']",
            "[class*='cart-item']",
            "[class*='cart_item']",
            "ul li",
        ]
        for selector in selectors:
            count = self.page.locator(selector).count()
            if count > 0:
                return count
        return 0

    def is_cart_empty(self) -> bool:
        """Retorna True si el carrito muestra mensaje de vacío."""
        empty_selectors = [
            "[data-testid='empty-cart']",
            "p:has-text('empty')",
            "p:has-text('vacío')",
            "p:has-text('Your cart is empty')",
            "[class*='empty']",
        ]
        for selector in empty_selectors:
            if self.page.locator(selector).is_visible():
                return True
        return False