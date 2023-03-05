import json


class BaseType:
    def dict(self) -> dict:
        return json.loads(json.dumps(self.__dict__, default=lambda o: o.json()))
