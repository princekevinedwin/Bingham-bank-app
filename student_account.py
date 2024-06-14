from Account import MainAccount


class StudentAccount(MainAccount):
    def __init__(self, initial_amount):
        super().__init__(initial_amount)

        self.withdrawal_limit = 2000
        self.deposit_limit = 50000

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print("Withdrawal limit exceeded")
        else:
            self.balance -= amount
            print(f'withdrawal successful. new balance: {self.balance}')

    def deposit(self, amount):
        if amount > self.deposit_limit:
            print("Deposit limit exceeded")
        else:
            self.balance += amount
            print(f'deposit successful. new balance: {self.balance}')

    def perform_operation(self):
        while True:
            operation = int(input("Choose an operation: \n1. Withdrawal\n2. Deposit\n3. "
                                  "Check Balance\n4. Exit\nEnter your choice: "))
            if operation == 1:
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif operation == 2:
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif operation == 3:
                self.display_balance()
            elif operation == 4:
                print("Exiting the program")
                break
            else:
                print("Invalid choice. Please choose a valid option")


student_account = StudentAccount(1000000)
student_account.perform_operation()
