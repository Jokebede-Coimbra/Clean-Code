from customer import Customer
from paper_boy import PaperBoy

customer = Customer("Well", "Gênio boy")
paper_boy = PaperBoy()

cost_of_magazine = 10.0
paper_boy.DeliverMagazine(customer, cost_of_magazine)
