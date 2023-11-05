from payment_methods import PaymentMethodsInterface
from monthly_usage import MonthlyUsage

class PaymentPosPago(PaymentMethodsInterface):
    
    def __init__(self) -> None:
        self.call_cost: float
        self.sms_cost: float
        self.total_cost: float
      
    def calcular_total(self, monthly_usage: MonthlyUsage) -> float:
            self.call_cost = 0.12 * monthly_usage.call_minutes
            self.sms_cost = 0.12 * monthly_usage.sms_count
            self.total_cost = self.call_cost + self.sms_cost
            return self.total_cost