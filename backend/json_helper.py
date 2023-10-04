import json
from backend.config import JSON_FILE_PATH
from backend.models.expense import Expense


def read_from_json():
    with open(JSON_FILE_PATH, 'r') as file:
        return json.load(file)


def write_to_json(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)


def get_all_expenses():
    return read_from_json()


def add_expense(expense):
    data = read_from_json()
    new_id = max([e["id"] for e in data]) + 1 if data else 1
    expense.id = new_id
    data.append(expense.__dict__)
    write_to_json(data)


def update_expense(expense_id, updated_expense):
    data = read_from_json()
    index = next((i for i, e in enumerate(data) if e["id"] == expense_id), None)
    if index is not None:
        data[index] = updated_expense.__dict__
        write_to_json(data)


def delete_expense(expense_id):
    data = read_from_json()
    data = [e for e in data if e["id"] != expense_id]
    write_to_json(data)
