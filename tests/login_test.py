import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


BASE_URL = "https://storedemo.testdino.com"

INVALID_EMAIL    = "usuario_falso@noexiste.com"
INVALID_PASSWORD = "ContraseñaIncorrecta999!"


# TC-001: Carga y renderizado de la página principal
class TestTC001HomeCarga:

    def test_titulo_contiene_nombre_del_sitio(self, page):
        home = HomePage(page, BASE_URL)
        home.open()
        title = home.get_title()
        assert "TestDino" in title, (
            f"El título esperaba contener 'TestDino', pero fue: '{title}'"
        )

    def test_logo_es_visible(self, page):
        home = HomePage(page, BASE_URL)
        home.open()
        assert home.is_logo_visible(), (
            "El logo del sitio no es visible en el encabezado."
        )

    def test_productos_visibles_en_home(self, page):
        home = HomePage(page, BASE_URL)
        home.open()
        count = home.get_product_count()
        assert count > 0, (
            f"Se esperaba al menos 1 producto en la home, pero se encontraron: {count}"
        )

    def test_navegacion_contiene_enlaces(self, page):
        home = HomePage(page, BASE_URL)
        home.open()
        links = home.get_nav_links_count()
        assert links > 0, (
            f"Se esperaban enlaces en la navegación, pero se encontraron: {links}"
        )


# TC-005: Login con credenciales inválidas
class TestTC005LoginInvalido:

    def test_login_invalido_mantiene_formulario_visible(self, page):
        login = LoginPage(page, BASE_URL)
        login.open()
        login.login(INVALID_EMAIL, INVALID_PASSWORD)
        assert login.is_login_form_visible(), (
            "Se esperaba que el formulario permaneciera visible tras credenciales inválidas."
        )

    def test_login_invalido_no_redirige(self, page):
        login = LoginPage(page, BASE_URL)
        login.open()
        login.login(INVALID_EMAIL, INVALID_PASSWORD)
        current_url = login.get_current_url()
        assert "/dashboard" not in current_url and "/profile" not in current_url, (
            f"El sistema redirigió a una sección protegida con credenciales inválidas: '{current_url}'"
        )

    def test_login_invalido_no_inicia_sesion(self, page):
        login = LoginPage(page, BASE_URL)
        login.open()
        login.login(INVALID_EMAIL, INVALID_PASSWORD)
        assert not login.is_logged_in(), (
            "Se detectó sesión activa tras un login con credenciales inválidas."
        )


# TC-010: Agregar un producto al carrito
class TestTC010AgregarAlCarrito:

    def test_url_cambia_al_abrir_carrito(self, page):
        product = ProductPage(page, BASE_URL)
        product.open()
        product.go_to_first_product()
        product.click_add_to_cart()
        product.open_cart()
        current_url = product.get_current_url()
        assert "cart" in current_url.lower(), (
            f"Se esperaba navegar al carrito, URL actual: '{current_url}'"
        )

    def test_carrito_no_esta_vacio_tras_agregar(self, page):
        product = ProductPage(page, BASE_URL)
        product.open()
        product.go_to_first_product()
        product.click_add_to_cart()
        product.open_cart()
        assert not product.is_cart_empty(), (
            "El carrito muestra el estado 'vacío' después de agregar un producto."
        )

    def test_agregar_producto_aumenta_items_en_carrito(self, page):
        product = ProductPage(page, BASE_URL)
        product.open()
        product.go_to_first_product()
        product.click_add_to_cart()
        product.open_cart()
        item_count = product.get_cart_item_count()
        assert item_count > 0, (
            f"Se esperaba al menos 1 ítem en el carrito, pero se encontraron: {item_count}"
        )