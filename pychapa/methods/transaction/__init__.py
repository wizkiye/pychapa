from .initialize_transaction import InitializeTransaction
from .verify_transaction import VerifyTransaction


class Transaction(InitializeTransaction, VerifyTransaction):
    pass
