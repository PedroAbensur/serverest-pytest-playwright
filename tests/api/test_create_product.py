import pytest
from pydantic import ValidationError
from utils_api.models.product_models import (
    ArrayProduto,
    ExisteProdutoComEsseNome,
    TokenAusenteInvalidoExpirado,
    RotaParaAdministradores
)
from utils_api.models.user_models import CadastroComSucesso

def test_create_product_api(client, ensure_admin_user, random_product):
    # Test Step 1: Create a product via the API as Admin User, using the Admin Token
    response = client.post("/produtos", random_product.model_dump())

    if response.status_code == 201:
        try:
            data = CadastroComSucesso(**response.json())
            assert data.message == "Cadastro realizado com sucesso", "Unexpected success message"
        except ValidationError as e:
            pytest.fail(f"Invalid success response format: {e}")

    elif response.status_code == 400:
        try:
            data = ExisteProdutoComEsseNome(**response.json())
            assert data.message == "Produto com esse nome já existe", "Unexpected duplicated product message"
            pytest.skip("Duplicated Product — test skipped.")
        except ValidationError as e:
            pytest.fail(f"Invalid duplicate response format: {e}")

    elif response.status_code == 401:
        try:
            data = TokenAusenteInvalidoExpirado(**response.json())
            assert data.message == "Token de acesso ausente", "Unexpected token error message"
            pytest.fail(f"Unauthorized access: {data.message}")
        except ValidationError as e:
            pytest.fail(f"Invalid 401 response format: {e}")

    elif response.status_code == 403:
        try:
            data = RotaParaAdministradores(**response.json())
            assert data.message == "Rota exclusiva para administradores", "Unexpected admin error message"
            pytest.fail(f"Forbidden: {data.message}")
        except ValidationError as e:
            pytest.fail(f"Invalid 403 response format: {e}")

    else:
        pytest.fail(f"Unexpected error when creating product: {response.status_code} - {response.text}")

    # Test Step 2: Search for the recently created Product using the API
    response_get = client.get("/produtos")
    if response_get.status_code != 200:
        pytest.fail(f"Error fetching products: {response_get.status_code} - {response_get.text}")

    try:
        produtos_data = response_get.json()["produtos"]
        produtos = [ArrayProduto(**produto) for produto in produtos_data]
    except ValidationError as ve:
        pytest.fail(f"Error processing products: {ve}")
    except Exception as e:
        pytest.fail(f"Unexpected error processing products: {e}")

    match = next(
        (p for p in produtos if p.nome == random_product.nome and p.descricao == random_product.descricao), None)
 
    assert match is not None, "Product not found in listing"
