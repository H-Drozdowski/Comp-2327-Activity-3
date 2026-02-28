"""This module defines the BillingAccount class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from payee.payee import Payee

class BillingAccount():
    """A class to represent a user's balances for various utility bills.
    """

    def __init__(self):
        """Initializes a new instance of the BillingAccount class.
        
        All balances are initialized to zero.
        """

        self.__balances = {Payee.ELECTRICITY: 0.0, 
                           Payee.INTERNET: 0.0,
                           Payee.TELEPHONE: 0.0}

    def add_balance(self, payee: Payee, amount: float):
        """Adds funds to the balance of a particular utility.

        Args:
            payee (Payee): The payee to which the funds will be applied.
            amount (float): The amount to apply to the balance.
        
        Raises: 
            TypeError: 
                - Raised when the amount is non-numeric type.
                - Raised when the payee is not a Payee type.
        """

        if not isinstance(amount, (float, int)):
            raise TypeError("Amount must be numeric.")
        
        if not isinstance(payee, Payee):
            raise TypeError("Payee must be Payee type.")
        
        if payee in self.__balances:
            self.__balances[payee] += amount
        

    def deduct_balance(self, payee: Payee, amount: float) -> None:
        """Deducts funds from the balance of a particular utility.

        Args:
            payee (Payee): The payee to which the funds will be 
                deducted.
            amount (float): The amount to deduct from the balance.
        
        Raises: 
            TypeError: 
                - Raised when the amount is non-numeric type.
                - Raised when the payee is not a Payee type.
        """

        if not isinstance(amount, (float, int)):
            raise TypeError("Amount must be numeric.")
        
        if not isinstance(payee, Payee):
            raise TypeError("Payee must be Payee type.")
        
        if payee in self.__balances:
            self.__balances[payee] -= amount

    def get_balance(self, payee: Payee) -> float | None:
        """Returns the balance of the specified utility.
        
        Args:
            payee (Payee): The utility of which the balance is 
                requested.

        Raises: 
            TypeError: 
                - Raised when the payee is not a Payee type.
        
        Returns:
            float: The balance of the specified utility.
        """

        if not isinstance(payee, Payee):
            raise TypeError("Payee must be Payee type.")

        return self.__balances[payee]

    def __str__(self) -> str:
        """Returns a string representation of the BillingAccount object.
        
        Returns:
            string: A representation of the BillingAccount object.
        """
        
        return (f"Electricity Balance: ${self.__balances[Payee.ELECTRICITY]:,.2f}\n"
                f"Internet Balance: ${self.__balances[Payee.INTERNET]:,.2f}\n"
                f"Telephone Balance: ${self.__balances[Payee.TELEPHONE]:,.2f}")
