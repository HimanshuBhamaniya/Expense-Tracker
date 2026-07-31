import json
import os
import tempfile
from typing import List
from models import Expense

class ExpenseRepository:
    def __init__(self, filepath: str = "storage.json"):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        if not os.path.exists(self.filepath):
            self._write_raw([])
            return

        try: 
            with open(self.filepath, "r", encoding="utf-8") as f:
                json.load(f)
        except (json.JSONDecodeError, OSError):
            self._write_raw([])

    def _write_raw(self, data: list) -> None:
        dir_name = os.path.dirname(self.filepath) or "."
        with tempfile.NamedTemporaryFile("w", dir=dir_name, delete=False, encoding="utf-8") as tmp_file:
            json.dump(data, tmp_file, indent=2)
            tmp_path = tmp_file.name

        os.replace(tmp_path, self.filepath)

    def load_all(self) -> List[Expense]:
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Expense.from_dict(item) for item in data]

    def save_all(self, expenses: List[Expense]) -> None:
        data = [expense.to_dict() for expense in expenses]
        self._write_raw(data)