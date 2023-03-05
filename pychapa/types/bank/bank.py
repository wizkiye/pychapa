from typing import Union

from pychapa.types import BaseType


class Bank(BaseType):
    def __init__(
        self,
        id: str,
        swift: str,
        name: str,
        currency: str,
        acct_length: int,
        country_id: str,
        created_at: str,
        updated_at: str,
        is_mobilemoney: Union[bool, None],
    ):
        self.currency = currency
        self.is_mobilemoney = is_mobilemoney
        self.acct_length = acct_length
        self.swift = swift
        self.updated_at = updated_at
        self.created_at = created_at
        self.country_id = country_id
        self.name = name
        self.id = id
