

class BankAccount:
    def __init__(self):
        pass

    def CreateAccount(self, name = "Unnamed Account"):
        self.name = name
        self.balance = 0


    def Deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited ${amount}, Current balance: ${self.balance}")

    def Withdraw(self, amount):

        if self.balance - amount < 0:
            answer = input("You are going into negative balance, this will lead to fees, continue? y/n ")
            if answer.lower() == "y":
                self.balance -= amount
                print(f"{self.name} withdrew ${amount}, Current balance: ${self.balance}")
            elif answer.lower() != "n" or answer.lower() != "y":
                print("The answer is not valid, Withdraw canceled")
            else:
                print("Withdraw canceled")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew ${amount}, Current balance: ${self.balance}")

    def ChangeAccountName():
        name = input("Please enter a new name: ")
        self.name = name
        



