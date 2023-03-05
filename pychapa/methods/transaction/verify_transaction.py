from typing import Dict, Union

from pychapa.scaffold import Scaffold


class VerifyTransaction(Scaffold):
    async def verify_transaction(
        self, transaction_id: str
    ) -> Dict[str, Union[str, None]]:
        """Verify the transaction

        Args:
            transaction_id (str): transaction id

        Response:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """
        response = await self._send_request(f"transaction/verify/{transaction_id}")
        return response.json()
