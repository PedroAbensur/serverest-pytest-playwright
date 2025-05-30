import pytest
import time
from page_objects.register_page import RegisterPage
from page_objects.register_product import RegisterProductPage
from page_objects.login_page import LoginPage
from page_objects.home_store_page import HomeStorePage
from page_objects.shopping_list_page import ShoppingListPage


@pytest.fixture
def initial_setup(page, ensure_admin_user, random_product, random_user):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email=ensure_admin_user.email, password=ensure_admin_user.password)

    page.wait_for_selector("text=Bem Vindo")
    cadastro_page = RegisterProductPage(page)
    cadastro_page.navigate()

    cadastro_page.fill_form(random_product)
    cadastro_page.register()

    page.wait_for_selector(f"text={random_product.nome}")

    assert page.locator(f"text={random_product.nome}").is_visible(), "Product is not present in Product Listing"

    cadastro_page.navigate()
    cadastro_page.fill_form(random_product)
    cadastro_page.register()

    cadastro_page.logout()

    register_page = RegisterPage(page)
    register_page.navigate()
    register_page.register(
        name=random_user.nome,
        email=random_user.email,
        password=random_user.password,
        is_admin=False
    )

    page.wait_for_selector("text=Cadastro realizado com sucesso")
    assert "Cadastro realizado com sucesso" in page.content(), "Error during registration"

    page.wait_for_selector("text=Serverest Store")
    assert "Serverest Store" in page.content(), "User is not in Home page"

    yield random_product


def test_add_shopping_list(page, initial_setup, random_product, random_user):
    store_page = HomeStorePage(page)

    store_page.search_product(random_product.nome)
    time.sleep(3)
    store_page.add_to_shopping_by_exact_name(random_product.nome)

    page.wait_for_selector("text=Lista de Compras")
    assert "Lista de Compras" in page.content(), "User is not in shopping list"

    shopping_list = ShoppingListPage(page)

    assert shopping_list.get_total_product(random_product.nome) == 1, "Product not present in shopping list"
