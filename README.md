# Automated Testing Project with Python, Pytest, and Playwright for [Serverest](https://serverest.dev) application.

- **Python** – Programming language
- **Pytest** – Test framework
- **Playwright (Python)** – E2E UI automation
- **HTTPX** – HTTP client for API testing
- **Pydantic** – Data validation and parsing for models
- **Page Object Model (POM)** – Design pattern for UI automation
- **conftest.py** – Shared fixtures and utilities


## Implemented Test Scenarios

### 🔹 Frontend (E2E) Tests
1. User Registration and Login
2. Admin User Create and Validate new Product
3. User Adding Products to Shopping List

### 🔹 API Tests
1. User Registration and Login
2. Admin User Create and Validate new Product
3. Admin User Edit Existing User


### Project Setup:
```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

playwright install
```

### Run all tests
```bash
pytest
```

### Run api tests
```bash
pytest tests/api/
```

### Run e2e tests
```bash
pytest tests/e2e_front/
```