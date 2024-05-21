class balanceException(Exception):
    pass

class bankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"Account {self.name} created! The balance is ${self.balance:.2f}")

    def get_balance(self):
        print(f"Account '{self.name}' has ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"The amount of ${amount} has been successfully deposited")
        self.get_balance()  

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise balanceException(f"The funds are insufficient for this transaction. Available Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("Withdraw complete")
            self.get_balance() 
        except balanceException as error:
            print(f"Withdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("********** BEGINNING TRANSFER **********")        
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("********** Transfer Complete **********")
        except balanceException as error:
            print(f"Transfer interrupted: {error}")    

class InterestRewardsAcct(bankAccount):     
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit Complete!")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 2.00  # Assuming a fixed withdrawal fee for SavingsAcct

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw complete")
            self.get_balance()
        except balanceException as error:
            print(f"Withdraw interrupted: {error}")


Mustafa = bankAccount(1000, "Mustafa")
Bilal = bankAccount(700, "Bilal")
Dave = InterestRewardsAcct(500, "Dave")
Sara = SavingsAcct(800, "Sara")