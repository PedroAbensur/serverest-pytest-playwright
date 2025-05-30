import pytest
import uuid
import random
from playwright.sync_api import sync_playwright
from utils_api.client import ServerestClient
from utils_api.models.login_models import RequestBodyLogin
from utils_api.models.user_models import RequestBodyUsuarios
from utils_api.models.product_models import RequestBodyProduto

BASE_URL = "https://serverest.dev"

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def client():
    return ServerestClient()


@pytest.fixture
def ensure_admin_user(client):
    admin_data = RequestBodyUsuarios(
        nome="joaop",
        email="jpaam@gmail.com",
        password="1234",
        administrador="true"
    )

    response = client.post(f"/usuarios", admin_data.model_dump())

    if response.status_code not in [201, 400] and "Este email já está sendo usado" not in response.text:
        pytest.fail(f"Failed to create admin: {response.text}")

    login_data = RequestBodyLogin(email=admin_data.email, password=admin_data.password)
    login_response = client.post("/login", login_data.model_dump())

    if login_response.status_code != 200:
        pytest.fail(f"Failed to login: {login_response.text}")

    token = login_response.json()["authorization"]
    client.set_token(token)

    return login_data

@pytest.fixture
def random_user():
    return RequestBodyUsuarios(
        nome=f"usuario_{uuid.uuid4().hex[:6]}",
        email=f"{uuid.uuid4().hex[:6]}@teste.com",
        password=uuid.uuid4().hex[:8],
        administrador="false"
    )

@pytest.fixture
def random_user2():
    return RequestBodyUsuarios(
        nome=f"usuario_{uuid.uuid4().hex[:6]}",
        email=f"{uuid.uuid4().hex[:6]}@gmail.com",
        password=uuid.uuid4().hex[:8],
        administrador="false"
    )

@pytest.fixture
def random_product():
    return RequestBodyProduto(
        nome=f"Produto_{uuid.uuid4().hex[:6]}",
        preco=random.randint(100, 1000),
        descricao=f"Descrição do produto {uuid.uuid4().hex[:8]}",
        quantidade=random.randint(100, 1000)
    )
