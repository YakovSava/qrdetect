from typing import Any

class Cache:

    def __init__(self):
        self._set = {}

    def add(self, key:str, data:Any) -> None:
        self._set[key] = data

    def delete(self, key:str) -> None:
        self._set.pop(key)

    def get(self, key:str) -> Any:
        self._set.get(key)