import datetime
from typing import List, Tuple, Optional
from models import Expense
from repository import ExpenseRepository

class ExpenseService:
    def __init__(self, repository: ExpenseRepository):
        self.repo = repository

    def _generate_next_id(self, expenses: List[Expense]) -> int:
        if not expenses:
            return 1
        return max(e.id for e in expenses) + 1

    def add_expense(self, description: str, amount: float) -> Expense:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if not description.strip():
            raise ValueError("Description cannot be empty.")

        expenses = self.repo.load_all()
        next_id = self._generate_next_id(expenses)
        today = datetime.date.today().isoformat()

        new_expense = Expense(
            id=next_id,
            description=description.strip(),
            amount=round(amount, 2),
            date=today
        )
        expenses.append(new_expense)
        self.repo.save_all(expenses)
        return new_expense

    def delete_expense(self, expense_id: int) -> bool:
        expenses = self.repo.load_all()
        initial_count = len(expenses)
        filtered_expenses = [e for e in expenses if e.id != expense_id]

        if len(filtered_expenses) == initial_count:
            raise KeyError(f"Expense with ID {expense_id} not found.")

        self.repo.save_all(filtered_expenses)
        return True

    def update_expense(self, expense_id: int, description: Optional[str], amount: Optional[float]) -> Expense:
        expenses = self.repo.load_all()
        target: Optional[Expense] = None

        for e in expenses:
            if e.id == expense_id:
                target = e
                break

        if not target:
            raise KeyError(f"Expense with ID {expense_id} not found.")

        if amount is not None:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            target.amount = round(amount, 2)

        if description is not None:
            if not description.strip():
                raise ValueError("Description cannot be empty.")
            target.description = description.strip()

        self.repo.save_all(expenses)
        return target 

    def list_expenses(self) -> List[Expense]:
        return self.repo.load_all()

    def get_summary(self, month: Optional[int] = None) -> Tuple[float, Optional[str]]:
        expenses = self.repo.load_all()
        current_year = datetime.date.today().year

        if not expenses:
            return 0.0, None

        if month is not None:
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")

            month_name = datetime.date(current_year, month, 1).strftime("%B")
            
            total = 0.0
            for e in expenses:
                try:
                    exp_date = datetime.datetime.strptime(e.date, "%Y-%m-%d")
                    if exp_date.month == month and exp_date.year == current_year:
                        total += e.amount
                except ValueError:
                    continue  # Ignore invalid date formats safely

            return round(total, 2), month_name

        total = sum(e.amount for e in expenses)
        return round(total, 2), None