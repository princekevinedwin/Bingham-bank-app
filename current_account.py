from Account import MainAccount


class CurrentAccount(MainAccount):
    def __init__(self, initial_amount):
        super().__init__(initial_amount)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def transaction(self):
        while True:
            print("Select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter the deposit amount: "))
                self.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter the withdrawal amount: "))
                self.withdraw(amount)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")


current_account = CurrentAccount(1000000)
current_account.display_balance()

current_account.transaction()

