#Bank Account Manager

class Accounts(object):
    def __init__(self, balance):
        self.balance = balance

    def getBalance(self):
        print("Your balance is $" + str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("Your new balance is $" + str(self.balance))

    def withdrawal(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print("Your new balance is $" + str(self.balance))
        else:
            print("There is not enough money in your account to make this withdrawal")


class Savings(Accounts):
    def calc_interest(self):
        interest = self.balance * 0.01
        print("You earned $%s in interest this month." %(interest))


class Checking(Accounts):
    def withdrawal(self, amount):
        if self.balance - amount > 100:
           self.balance -= amount
           print("Your new balance is $" + str(self.balance))
        else:
            print("There is not enough money in your account to make this withdrawal") 



print("Welcome to Mrs. Leveto's ATM")
accountType = int(input("What type of account? 1:Savings; 2:Checking?"))
if accountType == 1:
    accountPicked = Savings(1500)
elif accountType == 2:
    accountPicked = Checking(1000)


action = 0 
while action != 5:
    action = int(input("What would you like to do? 1: Check Balance; 2: Make a deposit; 3: Withdraw money; 4: Calculate monthly Interest on Savings; 5:Exit -"))
    if action == 1:
        accountPicked.getBalance()
    elif action == 2:
        depositAmount=int(input("How much would you like to deposit? "))
        accountPicked.deposit(depositAmount)
    elif action == 3:
        amount=int(input("How much would you like to withdraw? "))
        accountPicked.withdrawal(amount)
    elif action == 4:
        accountPicked.calc_interest()
    elif action == 5:
        print("Goodbye")
