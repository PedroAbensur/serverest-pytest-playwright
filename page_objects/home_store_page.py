from page_objects.components.navbar_component_user import NavbarComponent
import pytest

class HomeStorePage(NavbarComponent):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.get_by_placeholder("Pesquisar Produtos")
        self.search_button = page.get_by_role("button", name="Pesquisar")

    def search_product(self, nome_produto: str):
        self.search_input.fill(nome_produto)
        self.search_button.click()

    def add_to_shopping_by_exact_name(self, nome_produto: str):
        try:
            botao_adicionar = self.page.get_by_role("button", name="Adicionar a lista")
            botao_adicionar.click()
        except Exception as e:
            pytest.fail(f"Product '{nome_produto}' not found in Screen. Error: {e}")