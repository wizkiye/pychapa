from typing import Union, Dict, Optional

from ..base_type import BaseType


class Initialized(BaseType):
    def __init__(
        self,
        status: Optional[str] = None,
        data: Optional[Union[None, Dict[str, str]]] = None,
        message: Optional[str] = None,
    ):
        self.message = message
        self.data = data
        self.status = True if status == "success" else False
        self.checkout_url = data.get("checkout_url") if data else None
