from typing import List, Dict, Union

import httpx

from pychapa.types import Bank, SubAccount, Transaction, Initialized


class Scaffold:
    def __init__(self, api_key: str, api_version: str):
        self._s = None
        self.api_key = api_key
        self.api_version = api_version
        self._base_url = f"https://api.chapa.co/" + self.api_version + "/{}"
        self._headers = {"Authorization": f"Bearer {self.api_key}"}

    async def _send_request(
        self, endpoint: str, method: str = "GET", data: dict = None, **kwargs
    ) -> httpx.Response:
        pass

    async def create_sub_account(self, account: SubAccount):
        pass

    async def get_bank_lists(self) -> List[Bank]:
        pass

    async def initialize_tx(self, transaction: Transaction) -> Initialized:
        pass

    async def verify_transaction(self, transaction: str) -> Dict[str, Union[str, None]]:
        pass
