from flask import Blueprint, jsonify, request
from backend.json_helper import get_all_expenses, add_expense, update_expense, delete_expense
from backend.models.expense import Expense

expense_blueprint = Blueprint('expense', __name__)


@expense_blueprint.route('/expenses', methods=['GET'])
def get_all_expenses_route():
    expenses = get_all_expenses()
    return jsonify(expenses)


@expense_blueprint.route('/expense', methods=['POST'])
def add_expense_route():
    data = request.json
    expense = Expense(None, data["description"], data["category"], data["date"], data["amount"])
    add_expense(expense)
    return jsonify({"message": "Expense added successfully."}), 201


@expense_blueprint.route('/expense/<int:id>', methods=['PUT'])
def update_expense_route(id):
    data = request.json
    updated_expense = Expense(id, data["description"], data["category"], data["date"], data["amount"])
    update_expense(id, updated_expense)
    return jsonify({"message": f"Expense with ID {id} updated successfully."})


@expense_blueprint.route('/expense/<int:id>', methods=['DELETE'])
def delete_expense_route(id):
    delete_expense(id)
    return jsonify({"message": f"Expense with ID {id} deleted successfully."})
