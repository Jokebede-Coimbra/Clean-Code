from customer import Customer

class PaperBoy: 
        
    def DeliverMagazine(self, customer, cost_of_magazine):
        
        if customer.enough_money(cost_of_magazine):
            customer.withdraw_money(cost_of_magazine)
            print("Magazine delivered")
        else:
            print("Come back later")
        
        
 
