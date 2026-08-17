"""
ITECC04 Data Structures & Algorithms
Laboratory 1, Task B: the BankAccount class

The simpler of the two tasks. Same rules as Task A: the data stays private,
the operations are public, and the class refuses anything that would break
its own rule.

The rule this class protects: the balance may never go below zero.

Fill in one step at a time and run the tests after each one:

    python test_bank_account.py

Step 1  __init__       store the owner and the opening balance, privately
Step 2  get_balance    return the balance
Step 3  deposit        add to the balance, refusing zero or negative amounts
Step 4  withdraw       subtract, refusing anything that would overdraw
Step 5  __str__        return text such as 'Juan: 1500.00'
"""


class BankAccount:
    """An account that will not let itself go negative."""

    def __init__(self, owner, balance=0):
        # Step 1
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._owner = owner
        self._balance = balance

    def get_balance(self):
        # Step 2
        return self._balance

    def deposit(self, amount):
        # Step 3
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        # Step 4
        if amount < 0:
            raise ValueError("Witdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __str__(self):
        # Step 5
        return f"{self._owner}: {self._balance:.2f}"

if __name__ == "__main__":
    print("BankAccount starter. Run: python test_bank_account.py")
