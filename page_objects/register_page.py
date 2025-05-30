class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('input[placeholder="Digite seu nome"]')
        self.email_input = page.locator('input[placeholder="Digite seu email"]')
        self.password_input = page.locator('input[placeholder="Digite sua senha"]')
        self.admin_perm_input = page.locator('input[type="checkbox"]')
        self.register_button = page.get_by_role("button", name="Cadastrar")

    def navigate(self):
        self.page.goto("https://front.serverest.dev/cadastrarusuarios")

    def register(self, name: str, email: str, password: str, is_admin: bool = False):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)

        if is_admin:
            self.admin_perm_input.check()

        self.register_button.click()