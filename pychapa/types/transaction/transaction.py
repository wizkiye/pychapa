import re
from typing import Optional
from pychapa import types
from ..base_type import BaseType


class Transaction(BaseType):
    def __init__(
        self,
        email: str,
        amount: int,
        first_name: str,
        last_name: str,
        tx_ref: str,
        currency: Optional[str] = "ETB",
        callback_url: Optional[str] = None,
        customization: Optional["types.Customization"] = None,
    ):
        self.customization = customization
        self.callback_url = callback_url
        self.currency = currency
        self.tx_ref = tx_ref
        self.last_name = last_name
        self.first_name = first_name
        self.amount = amount
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("invalid email")
        self.email = email
