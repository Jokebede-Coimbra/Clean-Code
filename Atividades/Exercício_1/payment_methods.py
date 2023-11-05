from abc import ABC, abstractmethod
from monthly_usage import MonthlyUsage

class PaymentMethodsInterface(ABC):
    
    @abstractmethod    
    def calcular_total(self, monthly_usage: MonthlyUsage) -> float:
        pass