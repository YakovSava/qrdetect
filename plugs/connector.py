from requests import get


class Connector:

    def __init__(self):
        self._reqc = 0

    def connect(self, url: str) -> str:
        self._reqc += 1
        return get(url).text

    def reqcount(self) -> int:
        return self._reqc