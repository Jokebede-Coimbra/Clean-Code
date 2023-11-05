from monthly_usage import MonthlyUsage
from payment_methods import PaymentMethodsInterface

class PaymentPrePago(PaymentMethodsInterface):
         
    def calcular_total(self, monthly_usage: MonthlyUsage) -> float:
        return 54.90 
        
    