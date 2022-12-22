from entities import errors
import random


class Account(object):
    acceptedCurrency = ['BGN', 'EUR', 'USD', 'JPY']
    acceptedAccount = ['CURRENT', 'SAVINGS', 'CREDIT']

    def __init__(self, currency: str, acc_type: str):
        self.IBAN = f'BG{random.randint(1000, 9999)}'
        self.balance = 0
        if currency not in self.acceptedCurrency:
            raise errors.InvalidAccountCurrency('Not a valid currency')
        if acc_type not in self.acceptedAccount:
            raise errors.InvalidAccountType('Not a valid account type!')
        self.acc_type = acc_type
        self.currency = currency

    def __repr__(self):
        return f'Account: {self.balance} {self.currency} {self.acc_type}'
