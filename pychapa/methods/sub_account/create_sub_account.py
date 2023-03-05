from pychapa.scaffold import Scaffold
from pychapa.types import SubAccount


class CreateSubAccount(Scaffold):
    async def create_sub_account(self, account: SubAccount):
        """Create a sub_account

        Args:
            account (SubAccount): The vendor/merchant detail the sub_account for

        Response:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """
        response = await self._send_request(
            "subaccount",
            data=account.dict(),
        )
        return response.json()
