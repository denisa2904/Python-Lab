class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        pass

    def calc_interest(self):
        pass


class SavingAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.balance < amount:
            raise RuntimeError('Balance not enough')
        self.balance -= amount

    def calc_interest(self):
        self.balance += self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self.fee = 0

    def withdraw(self, amount):
        if self.balance < amount:
            raise RuntimeError('Balance not enough')
        self.balance -= amount
        self.balance -= self.fee


def main():
    saving = SavingAccount(1000, 0.01)
    saving.deposit(100)
    saving.withdraw(200)
    saving.calc_interest()
    print(f'Saving balance: {saving.balance:.2f}')

    checking = CheckingAccount(1000)
    checking.deposit(100)
    checking.withdraw(200)
    print(f'Checking balance: {checking.balance:.2f}')


if __name__ == '__main__':
    main()
