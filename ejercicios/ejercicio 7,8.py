class bankAccount:
    def __init__(self,number_account,owners,balance):
        self.number_account=number_account
        self.owners=owners
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

