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
1. User registration, logout, and login.
2. Product registration by admin and verification in the product listing.
3. User adding product to buyer's shopping list.

### 🔹 API Tests
1. User creation and duplicate email validation test.
2. Product creation and duplicate validation test with product listing verification.
3. Update existing user test with response validation.

Detailed test case specifications, such as initial setup, steps and expected results can be found expanding the session bellow:
<details>
  <summary>Test Specifications</summary>
    # Test Specifications

    This document describes the detailed specifications for the automated tests implemented using Python, Pytest, and Playwright.

    ---

    ## Frontend (E2E) Tests

    ### Test Case #1: User registration, logout, and login

    | **Test ID**         | `E2E-FRONT-001`                        |
    |---------------------|----------------------------------------|
    | **Description**     | Validates that a user can register, log out, and log back in successfully. |
    | **Initial Setup**   | None                                   |
    | **Test Steps**      | 1. Register random user <br/> 2. Check if registered user is in home page <br/> 3. Log out from account <br/> 4. Log in from registered account before <br/> 5. Check if logged user is in home page |
    | **Expected Result** | User is redirected to home page after registration and login.               |

    ---

    ### Test Case #2: Product registration by admin and verification in the product listing

    | **Test ID**         | `E2E-FRONT-002`                              |
    |---------------------|----------------------------------------------|
    | **Description**     | Admin registers a product and verifies its presence in the product listing, as well as the duplicated error when trying to create it again. |
    | **Initial Setup**   | Log into admin account                          |
    | **Test Steps**      | 1. Register the product as Admin User <br/> 2. Check if the product is in Product Listing <br/> 3. Try to register same product again <br/> 4. Check error that shows that product already exists|
    | **Expected Result** | 1. Product created is listed with correct name and visible to admin <br/> 2. When trying to create product with same name, error is shown on screen             |

    ---

    ### Test Case #3: Product registration by admin and addition to buyer's shopping list

    | **Test ID**         | `E2E-FRONT-003`                              |
    |---------------------|----------------------------------------------|
    | **Description**     | Tests product creation by admin and addition by buyer to shopping list. |
    | **Initial Setup**   | 1. Log into Admin Account <br/> 2. Register a Random Product <br/> 3. Check if product is registered correctly <br/> 4. Logout from admin account|
    | **Test Steps**      | 1. Register and log in as new user <br/> 2. Search product added in Initial Setup <br/> 3. Add it to Shopping List <br/> 4. Assert that product is present in Shopping List|
    | **Expected Result** | Product is present in shopping list with quantity = 1               |

    ---

    ## API Tests

    ### Test Case #1: User creation and duplicate email validation test

    | **Test ID**         | `API-001`                                  |
    |---------------------|---------------------------------------------|
    | **Description**     | Tests user creation and error when trying to register an existing email. |
    | **Initial Setup**   | None                                        |
    | **Test Steps**      | 1. Register an user using the API and assert it is created <br/> 2. Try to register the same user from Step 1 and assert it cannot be done |
    | **Expected Result** | 1. User can be succesfully registered <br/> 2. When trying to create user with same information API returns error.                  |

    ---

    ### Test Case #2: Product creation and duplicate validation test with product listing verification

    | **Test ID**         | `API-002`                                  |
    |---------------------|---------------------------------------------|
    | **Description**     | Product is created via API and duplicate creation is rejected.              |
    | **Initial Setup**   | Admin token generated (conftest fixture)                       |
    | **Test Steps**      | 1. Create a product via the API as Admin User, using the Admin Token <br/> 2. Get the Products array using the API <br/> 3. Search and assert the product is present in products array got from API|
    | **Expected Result** | Product is succesfully created by the Admin and validated it exists in the products listing             |

    ---

    ### Test Case #3: Update existing user test with response validation

    | **Test ID**         | `API-003`                                  |
    |---------------------|---------------------------------------------|
    | **Description**     | Updates a user's details and validates the response.                        |
    | **Initial Setup**   | Create a normal user                      |
    | **Test Steps**      | 1. Edit an existing user using the API (PUT) and assert the possible responses     |
    | **Expected Result** | API returns success and user data is updated and possible error treated.                              |

    ---
</details>

### Project Setup:
```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

playwright install

playwright install-deps chromium
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