from flask import Flask
from flask import render_template

from backend.routes.expense_routes import expense_blueprint

app = Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(expense_blueprint, url_prefix='/api')


@app.route('/')
def index():
    return render_template('expense.html')


if __name__ == "__main__":
    app.run(debug=True)
