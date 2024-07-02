""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    #init a class constructor
    #self is telling the class that it is calling one of its own variables;
    #needed for all variables in a class
    def __init__(self, balance=0, interest=0):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the account"""
        self.interest = interest
