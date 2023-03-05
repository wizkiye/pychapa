import json


class Customization:
    def __init__(self, title: str, description: str, logo: str):
        self.logo = logo
        self.description = description
        self.title = title

    def dict(self):
        data = {}
        for attr in self.__dict__.items():
            data.update({f"customization[{attr[0]}]": attr[1]})
        return data
