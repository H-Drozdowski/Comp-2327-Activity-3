"""This module defines the PenaltyStrategy class."""

from .payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee 

__author__ = "Hudson Drozdowski"
__version__ = "3.14.2"

class PenaltyStrategy(PaymentStrategy):
    """Represents the penalty payment strategy."""

    def process_payment(self, account : BillingAccount, payee : 
                        Payee, amount : float) -> str:
        """Processes a payment being paid to a payee and returns a 
        string representing the processed payment. If the updated 
        balance is greater than 0 a fee is applied.
        
        Args:
            account (BillingAccount): An instance of the BillingAccount
                class representing a users billing account.
            payee (Payee): An instance of the Payee class representing 
                the receiver of the payment.
            amount (float): The amount of money being paid to the payee. 
            
        Returns:
            str: Returns a string representing the payment and new 
            balance. If the payment is not paid in full a alert of a 
            penalty fee is added to the string.
        """

        account.deduct_balance(payee, amount)
        new_balance = account.get_balance(payee)

        if new_balance <= 0:
            return(f"Processed payment of ${amount}. New balance: ${new_balance:,.2f}.")
        else:
            account.add_balance(payee, 10.0)
            new_balance = account.get_balance(payee)
            return(f"Insufficient payment. Added penalty fee of "
                   f"$10.00. New balance: ${new_balance}.")
