"""This module defines the PartialPaymentStrategy class."""

from payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee 

__author__ = "Hudson Drozdowski"
__version__ = "3.14.2"

class PartialPaymentStrategy(PaymentStrategy):
    """Represents a partial payment strategy."""
    
    def process_payment(account : BillingAccount, payee : Payee, 
                        amount : float) -> str:
        """Processes a partial payment being paid to a payee and returns
        a string representing the processed payment.
        
        Args:
            account (BillingAccount): An instance of the BillingAccount
                class representing a users billing account.
            payee (Payee): An instance of the Payee class representing 
                the receiver of the payment.
            amount (float): The amount of money being paid to the payee. 
            
        Returns:
            str: Returns a string representing the partial or full 
            payment and the new balance.
        """

        account.deduct_balance(payee, amount)
        new_balance = account.get_balance(payee)

        if new_balance <= 0:
            return(f"Processed payment of ${amount}. New Balance: ${new_balance:,.2f}.")
        else:
            return(f"Partial payment of ${amount} accepted. New balance ${new_balance:,.2f}.")
