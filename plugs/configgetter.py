from toml import dumps, loads
from typing import Any


class Config:

    def __init__(self, config_filename: str=""):
        if not config_filename:
            raise
        self._conf = {}
        self._conffilename = config_filename
        self._reload()

    def _reload(self) -> None:
        pass

    def get(self, key: str) -> Any:
        return self._conf.get(key)
