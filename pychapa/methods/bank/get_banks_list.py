from typing import List

from pychapa.scaffold import Scaffold
from pychapa.types import Bank


class GetBankLists(Scaffold):
    async def get_bank_lists(self) -> List[Bank]:
        """Get the list of all banks
        Response:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """
        response = await self._send_request("banks")
        banks = response.json()
        return [Bank(**bank) for bank in banks["data"]]
