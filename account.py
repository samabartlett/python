class Account:
    def __init__(self, name: str):
        self._account_name = name
        self._account_balance = 0

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._account_balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self._account_balance

    def get_name(self) -> str:
        return self._account_name