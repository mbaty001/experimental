from dataclasses import dataclass

@dataclass
class Bank():
    owner: str
    balance: float


bank = Bank("michal", 123)
print(bank)