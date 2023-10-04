
document.addEventListener('DOMContentLoaded', function() {
    fetchExpenses();
    document.getElementById("addExpenseForm").addEventListener("submit", addExpense);
});

function fetchExpenses() {
    fetch('/api/expenses')
        .then(response => response.json())
        .then(data => {
            const expensesList = document.getElementById('expensesList');
            expensesList.innerHTML = '';
            data.forEach(expense => {
                const li = document.createElement('li');
                li.textContent = `${expense.description} - ${expense.category} - ${expense.date} - ${expense.amount} `;
                
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = function() { deleteExpense(expense.id); };
                
                li.appendChild(deleteButton);
                expensesList.appendChild(li);
            });
        });
}

function addExpense(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    
    fetch('/api/expense', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchExpenses();
    });
}

function deleteExpense(id) {
    fetch(`/api/expense/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchExpenses();
    });
}
    