from dataclasses import dataclass


@dataclass
class Expense:
    id: int
    description: str
    category: str
    date: str
    amount: float
