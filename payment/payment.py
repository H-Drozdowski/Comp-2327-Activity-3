"""This module defines the Payment class."""

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

__author__ = "Hudson Drozdowski"
__version__ = "3.14.2"

class Payment():
    """Represents a payment."""
    
    def __init__(self, strategy : PaymentStrategy):
        """Initializes a new instance of the Payment class.
        
        Args: 
            strategy (PaymentStrategy): A object representing the 
                payment strategy.
        
        Raises:
            - ValueError: A ValueError is raised when the argument value
            of strategy is not of the PaymentStrategy type.
        """

        if not isinstance(strategy, PaymentStrategy):
            raise ValueError("Invalid Strategy")
        else:
            self.__strategy = strategy

    def pay_bill(self, account : BillingAccount, payee : Payee, 
                 amount : float) -> str:
        """Pays the bill processes the payment and returns the payment
        confirmation message.
        
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

        payment_confirmation = self.__strategy.process_payment(account, payee, amount)

        return payment_confirmation

