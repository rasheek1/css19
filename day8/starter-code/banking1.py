class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        self.transactions = []
    def __str__(self):
        return '{label} currently has {balance} in account.'.format(label = self.label, balance = self.balance)
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(time.time(), 'withdraw', amount))
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(time.time(), 'deposit', amount))
    def rename(self, new_name):
        if new_name:
            self.label = new_name
    def transfer(self,dest_account, amount):
        if amount > 0 and amount <= self.balance:
            dest_account.balance += amount
            self.balance -= amount
            self.transactions.append(Transaction(time.time(), 'transfer', amount, dest_account.label))
    def see_transactions(self):
        for transcation in self.transactions:
            print(transcation)

class Transaction(object):
    def __init__(self, timestamp, type, amount, dest_account = None):
        self.time = timestamp
        self.type = type
        self.amount = amount 
        if type == 'transfer':
            self.dest_account = dest_account
    def __str__(self):
        if self.type == 'transfer':
            return '{0}: transfer ${1} to account {2}'.format(self.time, self.amount, self.dest_account)
        else:
            return '{0}: {1} ${2}'.format(self.time, self.type, self.amount)
