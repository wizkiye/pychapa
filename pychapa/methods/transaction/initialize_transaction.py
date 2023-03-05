from pychapa.scaffold import Scaffold
from pychapa.types import Transaction, Initialized


class InitializeTransaction(Scaffold):
    async def initialize_tx(self, transaction: Transaction) -> Initialized:
        """
        Initialize the Transaction

        Args:
            transaction (Transaction): customer details
        Return:
            dict: response from the server
            response(Response): Initialized object of the response data return from the Chapa server.
        """
        data = transaction.dict()
        if transaction.customization:
            data.update({**transaction.customization})
        response = await self._send_request(
            "transaction/initialize",
            data=data,
        )
        return Initialized(**response.json())
