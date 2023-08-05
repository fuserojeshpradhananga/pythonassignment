class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

    def __del__(self):
        print(f"Bank Account {self.account_number} has been closed.")


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = None

    def create_account(self, account_number, balance, account_type):
        self.bank_account = BankAccount(account_number, balance, account_type)

    def display_customer_info(self):
        print("Customer Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

    def __del__(self):
        if hasattr(self, 'bank_account') and self.bank_account:
            del self.bank_account
        print(f"Customer {self.name}'s account has been deleted.")
if __name__ == "__main__":
    customer1 = Customer("John Doe", 30, "123 Main Street")
    customer1.display_customer_info()

    customer1.create_account("5666", 1000, "Savings")
    customer1.bank_account.display_balance()

    customer1.bank_account.deposit(500)
    customer1.bank_account.display_balance()

    customer1.bank_account.withdraw(200)
    customer1.bank_account.display_balance()

    del customer1.bank_account
    del customer1
