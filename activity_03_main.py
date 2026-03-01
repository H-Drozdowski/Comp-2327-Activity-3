"""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "Hudson Drozdowski"
__version__ = "3.14.2"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from payment.payment import Payment
from patterns.strategy import *

def strategy():
    """Demonstrates the use of the classes defined in this activity."""
    
    print("STRATEGY PATTERN OUTPUT")

    # Given: Instantiates a BillingAccount object and 
    # adds the current balance owed for each utility.
    account = BillingAccount()
    account.add_balance(Payee.ELECTRICITY, 200.0)
    account.add_balance(Payee.INTERNET, 100.0)
    account.add_balance(Payee.TELEPHONE, 150.0)

    print("Initial Balances:")
    print(account, "\n")

    # 1. Instantiate a Payment object with a PenaltyStrategy payment 
    # strategy.
    try:
        penalty_payment = Payment(PenaltyStrategy())
    except ValueError as exception:
        print(str(exception))

    # 2. Use the Payment object's pay_bill method to pay the ELECTRICITY
    # bill with an amount that does not pay off the entire balance shown 
    # above - print the result of the pay_bill method.
    try:
        penalty_payment_str = penalty_payment.pay_bill(account, Payee.ELECTRICITY, 100)
        print(penalty_payment_str)
    except TypeError as exception:
        print(str(exception))
        
    # 3. Instantiate a Payment object with a PartialPaymentStrategy 
    # payment strategy.
    try:
        partial_payment = Payment(PartialPaymentStrategy())
    except ValueError as exception:
        print(str(exception))

    # 4. Use the Payment object's pay_bill method to pay the TELEPHONE 
    # bill with an amount that does not pay off the entire balance shown
    # above - print the result of the pay_bill method.
    try:
        partial_payment_str = partial_payment.pay_bill(account, Payee.TELEPHONE, 75)
        print(partial_payment_str)
    except TypeError as exception:
        print(str(exception))

    # 5. Using the Payment object created in step 3, make another 
    # payment for the TELEPHONE bill with an amount that pays off the 
    # remainder of the balance - print the result of the pay_bill 
    # method.
    try:
        partial_payment_str = partial_payment.pay_bill(account, Payee.TELEPHONE, 75)
        print(partial_payment_str)
    except TypeError as exception:
        print(str(exception)) 

    # 6. Print the BillingAccount object to show the updated balances 
    # for each of the payees.
    print(account)

if __name__ == "__main__":
    strategy()
