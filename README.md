# Reqres API Test Framework (Pytest + Allure)

This project is a robust, modular, and maintainable API test framework built using **Python**, **Pytest**, and **Allure Reporting**, targeting [Reqres API](https://reqres.in/).

---

## 📁 Project Structure

```
reqres_api_tests/
│
├── config/
│   └── settings.py           # Handles environment switching and base URL config
│
├── data/
│   └── test_data.py          # Test payloads and expected responses
│
├── tests/
│   ├── test_users.py         # Retrieves users
│   ├── test_login.py         # Tests login
│   ├── test_update.py        # PUT update test
│   ├── test_delete.py        # DELETE user test
│   ├── test_negative.py      # Negative test cases
│   └── test_delay.py         # Measures delayed responses
│
├── utils/
│   ├── assertions.py         # Assertion helpers
│   └── request_helper.py     # Wrapper around requests module
│
├── .env                      # contains environment-specific secrets (like API key)
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Python dependencies
├── conftest.py               # Fixtures and reusable setup
└── README.md                 # Project documentation
```

---

## ⚙️ Features

- 🔄 **Reusable Request Layer** with headers and base URL handling
- 🧪 **Parameterized Tests** with negative cases and edge validations
- 🧵 **Environment Switching** via `--env` flag (`local`, `staging`, `prod`)
- 📈 **Allure Reporting** integration
- ✅ **Status Code & JSON Key Assertions** in one place

---

## 🚀 Getting Started

### 1. Clone and Setup
```bash
git clone <https://github.com/BigAFJohn/pytest-framework.git>
cd reqres_api_tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Environment Variables (Optional)
Create a `.env` file with:
```
ENV=local
API_KEY=reqres-free-v1
```

### 3. Run Tests
```bash
pytest --alluredir=allure-results
```

### 4. View Allure Report
```bash
allure serve allure-results
```

---

## 🧪 Test Case Coverage

| Test File         | Description                              |
|-------------------|------------------------------------------|
| `test_users.py`   | Validates user list retrieval            |
| `test_login.py`   | Tests successful login                   |
| `test_update.py`  | PUT update for a user                    |
| `test_delete.py`  | Deletes a user and checks response       |
| `test_negative.py`| Covers missing password and 404 scenarios|
| `test_delay.py`   | Measures if delayed response ≤ 3.5s      |

---

## 💻 GitHub Actions

Framework supports GitHub Actions with Allure report publishing to `gh-pages`. Example command:

```bash
pytest --env=staging --alluredir=allure-results
```

---

## 📎 Notes

- `requests.post(..., json=data)` automatically sets `Content-Type: application/json`
- Delayed tests use `time.time()` to measure round-trip duration

---

## 👥 Contributing

Feel free to open issues or PRs to enhance this framework or add more APIs to test.

---

© 2025 — MIT License
