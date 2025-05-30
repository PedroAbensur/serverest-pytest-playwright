import pytest
from pydantic import ValidationError
from utils_api.models.user_models import CadastroComSucesso, ErrorEmailJaUtilizado

def test_create_user(client, random_user):
    # Test Step 1: Register an user using the API
    response1 = client.post("/usuarios", random_user.model_dump())

    if response1.status_code == 201:
        try:
            success = CadastroComSucesso(**response1.json())
            assert success.message == "Cadastro realizado com sucesso", "Unexpected success message"
        except ValidationError as e:
            pytest.fail(f"Invalid format on success answer: {e}")

    elif response1.status_code == 400:
        try:
            erro = ErrorEmailJaUtilizado(**response1.json())
            assert "email já está sendo usado" in erro.message.lower(), "Unexpected existing email message"
            pytest.skip("User already exists — test skipped.")
        except ValidationError as e:
            pytest.fail(f"Invalid format on existing email answer: {e}")

    else:
        pytest.fail(f"Unexpected error message creating user: {response1.status_code} - {response1.text}")

    # Test Step 2: Try to register the same user from last step and assert it cannot be done
    response2 = client.post("/usuarios", random_user.model_dump())

    if response2.status_code != 400:
        pytest.fail(f"Expected code 400 on creating existing user, received: {response2.status_code} - {response2.text}")

    try:
        erro = ErrorEmailJaUtilizado(**response2.json())
        assert erro.message == "Este email já está sendo usado", "Unexpected error message trying to create existing user"
    except ValidationError as e:
        pytest.fail(f"Invalid format on creating existing user: {e}")
