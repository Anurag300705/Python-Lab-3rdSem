class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        # Private attributes
        self.account_number = account_number
        self.balance = initial_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to check balance (no direct access to private variable)
    def get_balance(self):
        return self.balance

    # Method to get account number
    def get_account_number(self):
        return self.account_number


# Example usage:
account = BankAccount("123456789", 1000)
print(f"Account Number: {account.get_account_number()}")
print(f"Initial Balance: ${account.get_balance():.2f}")

account.deposit(500)

account.withdraw(300)

print(f"Balance after attempting over-withdrawal: ${account.get_balance():.2f}")
