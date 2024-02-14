import requests

from sys import argv # A temporary solution
from json import loads
from typing import Callable

class MoySklad:

    def __init__(self, token:str="", test:bool=False):
        self._token = token
        self._headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            "Accept-Encoding": "gzip"
        }
        self._start_url = "https://api.moysklad.ru/api/remap/1.2/"
        self._is_test = test

    def _get(self, method:str='entity/assortment'):
        if self._is_test:
            with open('test.json', 'r', encoding='utf-8') as file:
                return loads(file.read())
        else:
            resp = requests.get(
                url=self._start_url+method,
                headers=self._headers
            )
            return resp.json()

    def _get_all_lambda(self, data:list=[], lam:Callable=lambda x: x) -> list:
        return list(map(
            lam,
            data
        ))

    def _get_normal(self) -> list[dict]:
        return self._get_all_lambda(data=self._get()['rows'], lam=lambda x: {
            'code': x['code'],
            'name': x['name'],
            'barcode': x['barcodes'][0]['ean13']
        })

    def get_with_barcode(self, barcode:int=0) -> list[dict]:
        if not barcode:
            return {}
        for item in self._get_normal():
            if item['barcode'] == barcode:
                return item

    def add(self, ):

    def delete(self, id: str=None):
        if id is None:
            raise
        return

if __name__ == '__main__':
    ms = MoySklad(token=argv[1])
    ms._get()
