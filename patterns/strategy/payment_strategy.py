"""This module defines the PaymentStrategy class."""

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee 

__author__ = "Hudson Drozdowski"
__version__ = "3.14.2"

class PaymentStrategy(ABC):
    """Represents a payment strategy."""

    @abstractmethod
    def process_payment(account : BillingAccount, payee : 
                        Payee, amount : float) -> str:
        """Processes a payment being paid to a payee and returns a 
        string representing the processed payment.
        
        Args:
            account (BillingAccount): An instance of the BillingAccount
                class representing a users billing account.
            payee (Payee): An instance of the Payee class representing 
                the receiver of the payment.
            amount (float): The amount of money being paid to the payee. 
            
        Returns:
            str: Returns a string representing the payment and new 
            balance.
        """

        pass
    