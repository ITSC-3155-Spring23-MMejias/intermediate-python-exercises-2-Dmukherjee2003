class BankAccount:
    
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balence = starting_balance


    def withdraw(self, balence):
        self.balence = self.balence - balence


    def deposit(self, balence):
        self.balence = self.balence + balence


    def get_balance(self):
        return (self.account_name + " has a balence of $" + str(self.balence))
        