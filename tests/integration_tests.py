import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_all_expenses(client):
    response = client.get("/expenses")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_add_and_delete_expense(client):
    new_expense = {
        "description": "Integration Test Expense",
        "category": "Travel",
        "date": "2023-10-04",
        "amount": 150.0
    }
    response = client.post("/expense", json=new_expense)
    assert response.status_code == 201
    assert response.json["message"] == "Expense added successfully."

    all_expenses = client.get("/expenses").json
    last_expense_id = all_expenses[-1]["id"]
    response = client.delete(f"/expense/{last_expense_id}")
    assert response.status_code == 200
    assert response.json["message"] == f"Expense with ID {last_expense_id} deleted successfully."
