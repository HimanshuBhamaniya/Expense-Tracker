import datetime
from dataclasses import dataclass, asdict

@dataclass
class Expense:
    id: int
    description: str
    amount: float
    date: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            id=data["id"],
            description=data["description"],
            amount=data["amount"],
            date=data["date"],
        )