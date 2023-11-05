from customer_type import CustomerType
from monthly_usage import MonthlyUsage
from payment_methods import PaymentMethodsInterface

class MonthlyStatement:
    def __init__(self) -> None:
        self.call_cost: float
        self.sms_cost: float
        self.total_cost: float

    def generate(self, monthly_usage: MonthlyUsage, payment: PaymentMethodsInterface):
        if (monthly_usage.customer.customer_type == CustomerType.PAY_AS_YOU_GO):
            return payment.calcular_total(monthly_usage)
        elif (monthly_usage.customer.customer_type == CustomerType.UNLIMITED):
            return payment.calcular_total()
        else:
            raise Exception("The current customer type is not supported")
