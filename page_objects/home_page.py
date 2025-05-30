from page_objects.components.navbar_component_admin import NavbarComponent

class HomePage(NavbarComponent):
    def __init__(self, page):
        super().__init__(page)
        self.cadastrar_usuarios_button = page.get_by_text("Cadastrar", exact=True).nth(0)
        self.listar_usuarios_button = page.get_by_text("Listar", exact=True).nth(0)
        self.cadastrar_produtos_button = page.get_by_text("Cadastrar", exact=True).nth(1)
        self.listar_produtos_button = page.get_by_text("Listar", exact=True).nth(1)
        self.ver_relatorios_button = page.get_by_text("Ver", exact=True)

    def click_cadastrar_usuarios(self):
        self.cadastrar_usuarios_button.click()

    def click_listar_usuarios(self):
        self.listar_usuarios_button.click()

    def click_cadastrar_produtos(self):
        self.cadastrar_produtos_button.click()

    def click_listar_produtos(self):
        self.listar_produtos_button.click()

    def click_ver_relatorios(self):
        self.ver_relatorios_button.click()
