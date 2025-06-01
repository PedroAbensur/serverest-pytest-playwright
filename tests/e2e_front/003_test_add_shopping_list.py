import pytest
import time
from page_objects.register_page import RegisterPage
from page_objects.register_product import RegisterProductPage
from page_objects.login_page import LoginPage
from page_objects.home_store_page import HomeStorePage
from page_objects.shopping_list_page import ShoppingListPage
from playwright.sync_api import sync_playwright, TimeoutError


@pytest.fixture
def initial_setup(page, ensure_admin_user, random_product, random_user):
    # Initial Setup
    # 1. Log into Admin Account
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email=ensure_admin_user.email, password=ensure_admin_user.password)

    try:
        page.wait_for_selector("text=Bem Vindo")
    except TimeoutError:
        pytest.fail("Initial Setup: Login to admin account failed")

    # 2. Register a Random Product
    cadastro_page = RegisterProductPage(page)
    cadastro_page.navigate()

    cadastro_page.fill_form(random_product)
    cadastro_page.register()

    # 3. Check if product is registered correctly
    try:
        page.wait_for_selector(f"text={random_product.nome}")
    except TimeoutError:
        pytest.fail("Initial Setup: Product is not present in Product Listing")

    assert page.locator(f"text={random_product.nome}").is_visible(), "Product is not present in Product Listing"

    # 4. Logout from admin account and enter home page as buyer user
    cadastro_page.logout()

    yield random_product


def test_add_shopping_list(page, initial_setup, random_product, random_user):
    # Test Step 1: Register and log in as new user
    register_page = RegisterPage(page)
    register_page.navigate()
    register_page.register(
        name=random_user.nome,
        email=random_user.email,
        password=random_user.password,
        is_admin=False
    )

    try:
        page.wait_for_selector("text=Cadastro realizado com sucesso")
    except TimeoutError:
        pytest.fail("Error during registration")

    try:
        page.wait_for_selector("text=Serverest Store")
    except TimeoutError:
        pytest.fail("User is not in Home page")

    # Test Step 2: Search product added in Initial Setup
    store_page = HomeStorePage(page)

    store_page.search_product(random_product.nome)
    time.sleep(5)

    # Test Step 3: Add it to Shopping List
    store_page.add_to_shopping_by_exact_name(random_product.nome)
    time.sleep(4)

    try:
        page.wait_for_selector("text=Lista de Compras")
    except TimeoutError:
        pytest.fail("User is not in shopping list")

    # Test Step 4: Assert that product is present in Shopping List
    shopping_list = ShoppingListPage(page)
    assert shopping_list.get_total_product(random_product.nome) == 1, "Product not present in shopping list"
