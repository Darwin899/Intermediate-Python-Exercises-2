class BankAccount:
    # constructor to initialize instance variable
    def __init__(self,account_name,starting_balance):
        self.account_name=account_name
        self.balance=starting_balance

    # method to deposit amount
    def deposit(self,amount):
        # add amount into balance
        self.balance=self.balance+amount

    # method to withdraw amount
    def withdraw(self,amount):
        # if balance is greater than or equal to amount,then withdraw amount
        if self.balance>=amount:
            # subtract amount from balance
            self.balance=self.balance-amount
        # otherwise display the message
        else:
            print("No sufficient balance to withdraw")

    # method to return balance
    def get_balance(self):
        return str(self.account_name)+" has a balance of $"+str(self.balance)
