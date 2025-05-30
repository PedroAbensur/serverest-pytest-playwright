import pytest
from pydantic import ValidationError
from utils_api.models.user_models import ErrorEmailJaUtilizado, CadastroComSucesso, AlteradoComSucesso

@pytest.fixture
def initial_setup(client, random_user):
    create_response = client.post("/usuarios", random_user.model_dump())

    if create_response.status_code == 400:
        pytest.skip("User already exists - test skipped.")

    user_id = create_response.json().get("_id")
    assert user_id, "ID do usuário não retornado após criação."

    yield user_id

def test_edit_user(client, initial_setup, random_user2):
    edit_response = client.put(f"/usuarios/{initial_setup}", random_user2.model_dump())

    if edit_response.status_code == 200:
        try:
            success = AlteradoComSucesso(**edit_response.json())
            assert success.message == "Registro alterado com sucesso", "Unexpected success message"
        except ValidationError as e:
            pytest.fail(f"Invalid edit user success response format: {e}")

    elif edit_response.status_code == 201:
        try:
            data = CadastroComSucesso(**edit_response.json())
            assert data.message == "Cadastro realizado com sucesso", "Unexpected register message"
        except ValidationError as e:
            pytest.fail(f"Invalid register response format: {e}")

    elif edit_response.status_code == 400:
        try:
            data = ErrorEmailJaUtilizado(**edit_response.json())
            assert data.message == "E-mail já cadastrado", "Unexpected existing email message"
            pytest.skip("User already exists — test skipped.")
        except ValidationError as e:
            pytest.fail(f"Invalid existing email response format: {e}")
