import requests

class MoySklad:

    def __init__(self, token:str=""):
        self._token = token
        self._headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        self._start_url = "https://api.moysklad.ru/api/remap/1.2/"

    def _get(self, method:str='entity/assortment'):
        pass

    def send(self, color: str=None, size: int=None):
        if (color is None) or (size is None):
            raise
        return

    def delete(self, id: str=None):
        if id is None:
            raise
        return
