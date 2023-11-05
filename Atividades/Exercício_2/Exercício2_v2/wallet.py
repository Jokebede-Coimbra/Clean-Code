class Wallet():
    
    def __init__(self, money_amount):
        self.money_amount = money_amount
    
    def AddMoney(self, amount: float):
       
        self.money_amount += amount
        
    def WithdrawMoney(self, amount: float):
       
        self.money_amount -= amount
           
           