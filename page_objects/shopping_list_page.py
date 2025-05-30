from page_objects.components.navbar_component_user import NavbarComponent

class ShoppingListPage(NavbarComponent):
    def __init__(self, page):
        super().__init__(page)
        self.button_home_page = page.get_by_role("button", name="Página Inicial")
        self.button_add_cart = page.get_by_role("button", name="Adicionar no carrinho")
        self.button_clear_list = page.get_by_role("button", name="Limpar Lista")

    def go_to_home_page(self):
        self.button_home_page.click()

    def add_cart(self):
        self.button_add_cart.click()

    def clear_list(self):
        self.button_clear_list.click()

    def _get_card_product(self, nome_produto: str):
        return self.page.locator("div.card").filter(
            has=self.page.locator(f"[data-testid='shopping-cart-product-name']", has_text=f"Produto:{nome_produto}")
        )

    def add_quantity(self, nome_produto: str):
        card = self._get_card_product(nome_produto)
        botao_inc = card.locator("[data-testid='product-increase-quantity']")
        botao_inc.click()

    def decrease_quantity(self, nome_produto: str):
        card = self._get_card_product(nome_produto)
        botao_dec = card.locator("[data-testid='product-decrease-quantity']")
        botao_dec.click()

    def get_quantity_product(self, nome_produto: str) -> int:
        card = self._get_card_product(nome_produto)
        quantidade_texto = card.locator("div.row > div.col-3 > p").nth(1).inner_text()
        return int(quantidade_texto.strip())

    def get_total_product(self, nome_produto: str) -> int:
        card = self._get_card_product(nome_produto)
        total_text = card.locator("[data-testid='shopping-cart-product-quantity'] > p").inner_text()
        total_num = total_text.split(":")[-1].strip()
        return int(total_num)
