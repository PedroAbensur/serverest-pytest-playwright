class NavbarComponent:
    def __init__(self, page):
        self.page = page
        self.home_button = page.get_by_role("link", name="Home")
        self.lista_compras_button = page.get_by_role("link", name="Lista de Compras")
        self.carrinho_button = page.get_by_role("link", name="Carrinho")
        self.logout_button = page.get_by_role("button", name="Logout")

    def go_to_home(self):
        self.home_button.click()

    def go_to_lista_compras(self):
        self.lista_compras_button.click()

    def go_to_carrinho(self):
        self.carrinho_button.click()

    def logout(self):
        self.logout_button.click()

