class MainAccount:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def display_balance(self):
        print(f"Current balance: {self.balance}")


main_account = MainAccount(1000000)
main_account.display_balance()
