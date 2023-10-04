from backend.json_helper import get_all_expenses, add_expense, update_expense, delete_expense
from backend.models.expense import Expense


def test_add_expense():
    initial_expenses = get_all_expenses()
    new_expense = Expense(None, "Test Expense", "Food", "2023-10-04", 50.0)
    add_expense(new_expense)
    updated_expenses = get_all_expenses()

    assert len(updated_expenses) == len(initial_expenses) + 1
    assert updated_expenses[-1]["description"] == "Test Expense"


def test_update_expense():
    expenses = get_all_expenses()
    last_expense_id = expenses[-1]["id"]
    updated_expense = Expense(last_expense_id, "Updated Expense", "Entertainment", "2023-10-04", 100.0)
    update_expense(last_expense_id, updated_expense)
    updated_expenses = get_all_expenses()

    assert updated_expenses[-1]["description"] == "Updated Expense"


def test_delete_expense():
    initial_expenses = get_all_expenses()
    last_expense_id = initial_expenses[-1]["id"]
    delete_expense(last_expense_id)
    updated_expenses = get_all_expenses()

    assert len(updated_expenses) == len(initial_expenses) - 1
    assert all(e["id"] != last_expense_id for e in updated_expenses)
