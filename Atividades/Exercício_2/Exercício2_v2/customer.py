from wallet import Wallet

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.wallet = Wallet(1000.0)
        
 
    def enough_money(self, cost_of_magazine):
        return self.wallet.money_amount >= cost_of_magazine

    def withdraw_money(self, cost_of_magazine):
        self.wallet.WithdrawMoney(cost_of_magazine)     