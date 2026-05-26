from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object para el formulario de Login de TestDino Store."""

    # --- Locators (verificados con playwright codegen) ---
    USER_ICON      = "[data-testid='header-user-icon']"
    EMAIL_INPUT    = "[data-testid='login-email-input']"
    PASSWORD_INPUT = "[data-testid='login-password-input']"
    SUBMIT_BUTTON  = "[data-testid='login-submit-button']"
    ERROR_MESSAGE  = "[data-testid='login-error-message'], [class*='error'], [class*='alert'], [role='alert'], p:has-text('Invalid'), p:has-text('incorrect'), p:has-text('wrong'), p:has-text('failed')"
    USER_INDICATOR = "[data-testid='header-user-icon'][class*='logged'], [data-testid='user-menu'], [data-testid='logout-button'], [class*='avatar']"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def open(self):
        """Abre la home y hace clic en el ícono de usuario para mostrar el login."""
        self.navigate("/")
        self.page.locator(self.USER_ICON).click()
        self.page.wait_for_timeout(500)

    def fill_email(self, email: str):
        self.page.locator(self.EMAIL_INPUT).click()
        self.page.locator(self.EMAIL_INPUT).fill(email)

    def fill_password(self, password: str):
        self.page.locator(self.PASSWORD_INPUT).click()
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_submit(self):
        self.page.locator(self.SUBMIT_BUTTON).click()
        self.page.wait_for_timeout(1500)

    def login(self, email: str, password: str):
        """Flujo completo: abrir formulario, llenar campos y enviar."""
        self.fill_email(email)
        self.fill_password(password)
        self.click_submit()

    def is_error_visible(self) -> bool:
        """Busca cualquier mensaje de error visible tras un login fallido."""
        try:
            self.page.wait_for_selector(self.ERROR_MESSAGE, timeout=3000)
            return self.page.locator(self.ERROR_MESSAGE).first.is_visible()
        except Exception:
            return False

    def is_login_form_visible(self) -> bool:
        """Retorna True si el formulario de login sigue visible (login falló)."""
        return self.page.locator(self.EMAIL_INPUT).is_visible()

    def is_logged_in(self) -> bool:
        """Retorna True si el indicador de sesión activa es visible."""
        return self.page.locator(self.USER_INDICATOR).first.is_visible()

    def get_current_url(self) -> str:
        return self.page.url