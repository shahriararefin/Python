class Account:
    
    def __init__(self, balance, accNo) -> None:
        self.balance = balance
        self.accNo = accNo
    
    def  debit(self, amount):
        self.balance -= amount
        print("Taka: ", amount, "was debited")
        print("total balance = ", self.getBalance())
        
    def  credit(self, amount):
        self.balance += amount
        print("Taka: ", amount, "was credited")
        print("total balance = ", self.getBalance())
    
    def getBalance(self):
        return self.balance  

accNo1 = Account(23441, 106050)


print("Balance: ", accNo1.balance)
print("Account No: ", accNo1.accNo)
accNo1.debit(509)
accNo1.credit(2014)



