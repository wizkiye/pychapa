import httpx

from pychapa.methods import Methods
from pychapa.scaffold import Scaffold


class Chapa(Methods, Scaffold):
    def __init__(self, api_key: str, api_version: str = "v1"):
        super(Chapa, self).__init__(api_key, api_version)
        self._s = httpx.AsyncClient(headers=self._headers)

    async def _send_request(
        self, endpoint: str, data: dict = None, **kwargs
    ) -> httpx.Response:
        method = "POST" if data else "GET"
        if data:
            data = {k: v for k, v in data.items() if v is not None}
        res = await self._s.request(
            url=self._base_url.format(endpoint), method=method, json=data, **kwargs
        )
        return res
