from pychapa.types import BaseType


class SubAccount(BaseType):
    def __init__(
        self,
        business_name: str,
        account_name: str,
        bank_code: str,
        account_number: str,
        split_type: str,
        split_value: float,
    ):
        self.split_value = split_value
        self.split_type = split_type
        self.account_number = account_number
        self.bank_code = bank_code
        self.account_name = account_name
        self.business_name = business_name
