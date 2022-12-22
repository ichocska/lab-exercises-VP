
from entities import errors
import random
class Account(object):
    __acceptedCurrency = ['BGN' , 'EUR', 'USD', 'JPY']
    __acceptedAccount = ['CURRENT', 'SAVINGS', 'CREDIT']
    def __init__(self, currency: str, acc_type : str) -> None:
        self.IBAN = f'BG{random.randint(1000,9999)}'
        self.balance = 0
        if currency not in self.__acceptedCurrency:
            raise errors.InvalidAccountCurrency('Not a valid currency')
        if acc_type not in self.__acceptedAccount:
            raise errors.InvalidAccountType('Not a valid account type!')
        self.acc_type = acc_type
        self.currency = currency
    def __repr__(self) -> str:
        return f'Account: {self.balance} {self.currency} {self.acc_type}'