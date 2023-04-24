from BankAccount import BankAccount
if __name__ == "__main__":
    # create an instance of BankAccount class
    account=BankAccount("John",1000)
    # call deposit() function
    account.deposit(600)
    # call withdraw() function
    account.withdraw(100)
    # call get_balance() function and display result
    print(account.get_balance())