from .bank import Bank
from .transaction import Transaction
from .sub_account import SubAccount


class Methods(Bank, Transaction, SubAccount):
    pass
