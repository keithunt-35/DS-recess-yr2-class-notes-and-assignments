#real world Scenario or problem

#Bank account: savings acount and current account inherit from bank account

#deposit. withdraw, displa balance, types of accounts

#super class
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
        
def deposit(self, amount):
    if amount <= self.balance:
        self.balance += amount
        print(f'deposited {amount}. New balance is now: {self.balance}')
    else:
        print('Insufficient funds')
        
def display_balance(self):
    print(f'Account {self.acocunt_number} Balance: {self.balance}')
    
    
#sub class : saving account
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate #store the interest rate
        
    #new method for the interes rate calculation
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        #ading the interest
        
        self.balance += interest
        print(f' Interest of {interest} added. New balance : {self.balance}')
        
 #child class : Current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance,overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit # to store the over draft
            
            
           #overdraft withdraw method to allow overdraft
    def withdraw(self, amount):
        if amount<= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'withedrew {amount}. New balance:{self.balance}')
        else:
            print("you have exeeded the overdraft limit")
                    
                    
#creating the objects

saving = SavingAccount('SAV0555555555', 10000000,5)
current = CurrentAccount('CURO57778787887',500000,10)

#test method display
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)
print('LB______________________')

current.display_balance()
current.withdraw(70000)
current.withdraw(45000)