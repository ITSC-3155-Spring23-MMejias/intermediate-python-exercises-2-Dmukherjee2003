from BankAccount import BankAccount
if __name__ == "__main__":
    bnk = BankAccount("Dhruv", 3450)
    bnk.deposit(950)
    bnk.withdraw(400)
    print(bnk.get_balance())