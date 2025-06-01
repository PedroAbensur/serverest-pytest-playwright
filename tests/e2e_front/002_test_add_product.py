import pytest
from page_objects.register_product import RegisterProductPage
from page_objects.login_page import LoginPage
from playwright.sync_api import sync_playwright, TimeoutError

@pytest.fixture
def login_setup(page, ensure_admin_user):
    # Initial Setup
    # 1. Log into admin account
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email=ensure_admin_user.email, password=ensure_admin_user.password)

    try:
        page.wait_for_selector("text=Bem Vindo")
    except TimeoutError:
        pytest.fail("Initial Setup: Login to admin account failed")

    yield page


def test_add_product(page, login_setup, random_product):
    # Test Step 1: Register a product as Admin User
    cadastro_page = RegisterProductPage(page)
    cadastro_page.navigate()

    cadastro_page.fill_form(random_product)
    cadastro_page.register()

    # Test Step 2: Check if the product is in Product Listing
    try:
        page.wait_for_selector(f"text={random_product.nome}")
    except TimeoutError:
        pytest.fail("Product is not present in Product Listing")

    try:
        if not page.locator(f"text={random_product.nome}").is_visible():
            pytest.fail("Product is not present in Product Listing")
    except TimeoutError:
        pytest.fail("Error checking product visibility in listing")

    # Test Step 3: Try to register same product again
    cadastro_page.navigate()
    cadastro_page.fill_form(random_product)
    cadastro_page.register()

    # Test Step 4: Check error that shows that product already exists
    try:
        page.wait_for_selector("text=Já existe produto com esse nome")
    except TimeoutError:
        pytest.fail("Duplicate product name message not displayed")

    try:
        if "Já existe produto com esse nome" not in page.content():
            pytest.fail("Duplicate product name message not displayed")
    except TimeoutError:
        pytest.fail("Error checking for duplicate product name message")
