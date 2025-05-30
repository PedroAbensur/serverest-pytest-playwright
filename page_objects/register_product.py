from page_objects.components.navbar_component_admin import NavbarComponent
from utils_api.models.product_models import RequestBodyProduto

class RegisterProductPage(NavbarComponent):
    def __init__(self, page):
        super().__init__(page)
        self.nome_input = page.locator('input[placeholder="Digite o nome do produto"]')
        self.preco_input = page.locator('input[placeholder="Digite o valor do produto"]')
        self.descricao_input = page.locator('textarea[placeholder="Digite a descrição do produto"]')
        self.quantidade_input = page.locator('input[placeholder="Digite aquantidade do produto"]')
        self.imagem_input = page.locator('input[type="file"]')
        self.cadastrar_button = page.get_by_role("button", name="Cadastrar")

    def navigate(self):
        self.page.goto("https://front.serverest.dev/admin/cadastrarprodutos")

    def fill_name(self, nome: str):
        self.nome_input.fill(nome)

    def fill_price(self, preco: int):
        self.preco_input.fill(str(preco))

    def fill_description(self, descricao: str):
        self.descricao_input.fill(descricao)

    def fill_quantity(self, quantidade: int):
        self.quantidade_input.fill(str(quantidade))

    def send_image(self, caminho_imagem: str):
        self.imagem_input.set_input_files(caminho_imagem)

    def fill_form(self, produto: RequestBodyProduto):
        self.fill_name(produto.nome)
        self.fill_price(produto.preco)
        self.fill_description(produto.descricao)
        self.fill_quantity(produto.quantidade)

    def register(self):
        self.cadastrar_button.scroll_into_view_if_needed()
        self.cadastrar_button.click()
