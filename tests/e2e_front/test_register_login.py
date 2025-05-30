from page_objects.home_page import HomePage
from page_objects.register_page import RegisterPage
from page_objects.login_page import LoginPage

def test_register_login_with_random_user(page, random_user, ensure_admin_user):
    # Test Step 1: Register random user
    register_page = RegisterPage(page)
    register_page.navigate()
    register_page.register(
        name=random_user.nome,
        email=random_user.email,
        password=random_user.password,
        is_admin=random_user.administrador
    )

    page.wait_for_selector("text=Cadastro realizado com sucesso")
    assert "Cadastro realizado com sucesso" in page.content(), "Error during registration"

    page.wait_for_selector(f"text=Bem vindo {random_user.nome}")
    assert "Bem Vindo" in page.content(), "User is not in Home page"

    # Test Step 2: Check if registered user is in home page
    home_page = HomePage(page)
    assert home_page.cadastrar_usuarios_button.is_visible(), "Home page not loaded after registration"

    # Test Step 3: Log out from account
    page.wait_for_selector("text=Logout")
    home_page.logout()

    # Test Step 4: Log in from registered account before
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email=random_user.email, password=random_user.password)

    # Test Step 5: Check if logged user is in home page
    page.wait_for_selector(f"text=Bem Vindo {random_user.nome}")
    assert "Bem Vindo" in page.content(), "User is not in Home page"
