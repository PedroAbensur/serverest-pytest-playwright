import pytest
from page_objects.register_product import RegisterProductPage
from page_objects.login_page import LoginPage

@pytest.fixture
def login_setup(page, ensure_admin_user):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email=ensure_admin_user.email, password=ensure_admin_user.password)

    page.wait_for_selector("text=Bem Vindo")
    yield page


def test_create_product(page, login_setup, random_product):
    cadastro_page = RegisterProductPage(page)
    cadastro_page.navigate()

    cadastro_page.fill_form(random_product)
    cadastro_page.register()

    page.wait_for_selector(f"text={random_product.nome}")

    assert page.locator(f"text={random_product.nome}").is_visible(), "Product is not present in Product Listing"
