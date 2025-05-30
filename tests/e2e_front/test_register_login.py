from page_objects.home_page import HomePage
from page_objects.register_page import RegisterPage
from page_objects.login_page import LoginPage

def test_register_login_with_random_user(page, random_user, ensure_admin_user):
    register_page = RegisterPage(page)
    register_page.navigate()
    register_page.register(
        name=random_user.nome,
        email=random_user.email,
        password=random_user.password,
        is_admin=random_user.administrador
    )

    page.wait_for_selector("text=Cadastro realizado com sucesso")

    page.wait_for_selector(f"text=Bem vindo {random_user.nome}")
    home_page = HomePage(page)

    assert home_page.cadastrar_usuarios_button.is_visible(), "Home page not loaded after registration"

    page.wait_for_selector("text=Logout")
    home_page.logout()

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email=random_user.email, password=random_user.password)

    page.wait_for_selector(f"text=Bem Vindo {random_user.nome}")

    assert "Bem Vindo" in page.content()
