class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.locator('input[placeholder="Digite seu email"]')
        self.password_input = page.locator('input[placeholder="Digite sua senha"]')
        self.login_button = page.get_by_text("Entrar")

    def navigate(self):
        self.page.goto("https://front.serverest.dev/login")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
