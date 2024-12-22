class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def display_account_info(self):
        print(f"Account Number: {self._account_number}")
        self._display_balance()

    def _display_balance(self):
        print(f"Balance: {self._balance}")

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        self._display_balance() #Corrected to call the internal display method

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Error: Balance cannot be negative")

account = BankAccount("123456789", 100.0)
account.deposit(50)
account.withdraw(30)
account.set_balance(-20)  # Invalid balance
account.display_account_info()