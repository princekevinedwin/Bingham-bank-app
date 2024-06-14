from MainAccount import MainAccount


class SavingsAccount(MainAccount):
    def __init__(self, initial_amount):
        super().__init__(initial_amount)
        self.__interest_rate = 0.005
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        interest = amount * self.__interest_rate
        self.balance += amount + interest
        print(f"Deposited {amount} with {interest} interest. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal amount exceeds the limit of {self.withdrawal_limit}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


def main():
    savings_account = SavingsAccount(1000000)
    savings_account.display_balance()

    while True:
        action = input("Would you like to 'deposit' or 'withdraw'? (Type 'exit' to quit): ").lower()

        if action == 'deposit':
            amount = float(input("Enter the amount to deposit: "))
            savings_account.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter the amount to withdraw: "))
            savings_account.withdraw(amount)
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

        savings_account.display_balance()


if __name__ == "__main__":
    main()
