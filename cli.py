import argparse
import sys
from repository import ExpenseRepository
from service import ExpenseService

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="expense-tracker", description="CLI Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add a new expense")
    parser_add.add_argument("--description", required=True, type=str, help="Expense description")
    parser_add.add_argument("--amount", required=True, type=float, help="Expense amount")

    subparsers.add_parser("list", help="List all expenses")

    parser_summary = subparsers.add_parser("summary", help="Show total expenses")
    parser_summary.add_argument("--month", type=int, choices=range(1, 13), help="Filter summary by month (1-12)")

    parser_delete = subparsers.add_parser("delete", help="Delete an expense by ID")
    parser_delete.add_argument("--id", required=True, type=int, help="Expense ID")

    parser_update = subparsers.add_parser("update", help="update an expense")
    parser_update.add_argument("--id", required=True, type=int, help="Expense ID")
    parser_update.add_argument("--description", type=str, help="New description")
    parser_update.add_argument("--amount", type=float, help="New amount")

    return parser

def run_cli():
    parser = build_parser()
    args = parser.parse_args()

    repo = ExpenseRepository("storage.json")
    service = ExpenseService(repo)

    try:
        if args.command == "add":
            expense = service.add_expense(args.description, args.amount)
            print(f"# Expense added successfully (ID: {expense.id})")

        elif args.command == "list":
            expenses = service.list_expenses()
            if not expenses:
                print("No expenses recorded yet.")
                return 

            print(f"{'ID':<4} {'Date':<12} {'Description':<18} {'Amount':<8}")
            print("-" * 45)
            for e in expenses:
                print(f"{e.id:<4} {e.date:<12} {e.description:<18} ₹{e.amount:.2f}")

        elif args.command == "summary":
            total, month_name = service.get_summary(args.month)
            if month_name:
                print(f"# Total expenses for {month_name}: ₹{total:.2f}")
            else:
                print(f"# Total expenses: ₹{total:.2f}")

        elif args.command == "delete":
            service.delete_expense(args.id)
            print("# Expense deleted successfully")

        elif args.command == "update":
            if args.description is None and args.amount is None:
                print("Error: Provide at least --description or --amount to update.", file=sys.stderr)
                sys.exit(1)
            service.update_expense(args.id, args.description, args.amount)
            print("# Expense updated successfully")

    except (ValueError, KeyError) as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)