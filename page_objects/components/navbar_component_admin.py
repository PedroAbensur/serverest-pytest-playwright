class NavbarComponent:
    def __init__(self, page):
        self.page = page
        self.home_button = page.get_by_role("link", name="Home")
        self.cadastrar_usuarios_button = page.get_by_role("link", name="Cadastrar Usuários")
        self.listar_usuarios_button = page.get_by_role("link", name="Listar Usuários")
        self.cadastrar_produtos_button = page.get_by_role("link", name="Cadastrar Produtos")
        self.listar_produtos_button = page.get_by_role("link", name="Listar Produtos")
        self.relatorios_button = page.get_by_role("link", name="Relatórios")
        self.logout_button = page.get_by_role("button", name="Logout")

    def go_to_home(self):
        self.home_button.click()

    def go_to_cadastrar_usuarios(self):
        self.cadastrar_usuarios_button.click()

    def go_to_listar_usuarios(self):
        self.listar_usuarios_button.click()

    def go_to_cadastrar_produtos(self):
        self.cadastrar_produtos_button.click()

    def go_to_listar_produtos(self):
        self.listar_produtos_button.click()

    def go_to_relatorios(self):
        self.relatorios_button.click()

    def logout(self):
        self.logout_button.click()
