class BankAccount:
    def __init__(self, accNumber, accHolderName, accBalance):
        self.accNumber= accNumber
        self.accHolderName= accHolderName
        self.accBalance = accBalance

    def deposit(self,amount):
        self.accBalance+=amount

    def withdraw(self,amount):
        self.accBalance-=amount

    def displayAccountInformation(self):
        print(f"Account Number: {self.accNumber}")
        print(f"Account Holder Name: {self.accHolderName}")
        print(f"Account Balance : {self.accBalance}")

obj= BankAccount(226169, 'Aryesh', 10000)

obj.deposit(2000)
obj.withdraw(1500)
obj.displayAccountInformation()