from Account import MainAccount


class ChildrensAccount(MainAccount):
    def __init__(self, initial_amount):
        super().__init__(initial_amount)
        self.interest_rate = 0.007
        self.withdrawal_limit = 0

    def deposit(self, amount):
        interest = amount * self.interest_rate
        self.balance += amount + interest
        print(f"Deposited {amount} with {interest} interest. New balance: {self.balance}")

    def withdraw(self, amount):
        print("Withdrawals are not allowed for Children's Account.")


def main():
    children_account = ChildrensAccount(10000)
    children_account.display_balance()

    while True:
        action = input("Would you like to 'deposit' or 'withdraw'? (Type 'exit' to quit): ").lower()

        if action == 'deposit':
            amount = float(input("Enter the amount to deposit: "))
            children_account.deposit(amount)
        elif action == 'withdraw':
            print("Withdrawals are not allowed for Children's Account.")
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    main()
