import base64
import requests

from time import sleep
from json import loads, dumps
from typing import Callable
from pprint import pprint # A temporary solution
from sys import argv # A temporary solution
from random import randint # A temporary solution

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

    def _put(self, method:str='entity/product/', uuid:str='', data:dict={}):
        return requests.put(
            url=self._start_url+method+uuid,
            data=dumps(data),
            headers=self._headers
        )

    def _get_all_lambda(self, data:list=[], lam:Callable=lambda x: x) -> list:
        return list(map(
            lam,
            data
        ))

    def _filter_data(self, data:list=[], lam:Callable=lambda x: x) -> list:
        return list(filter(
            lam,
            data
        ))

    def _fmap(self, x:dict):
        try:
            return {
                'uuid': x['id'],
                'code': x['code'],
                'name': x['name'],
                'barcode': x['barcodes'][0]['ean13'],
                'quantity': x['quantity']
            }
        except:
            return {
                'uuid': x['id'],
                'code': x['code'],
                'name': x['name'],
                'barcode': x['barcodes'][0]['ean13'],
                'quantity': 0
            }

    def _get_normal(self) -> list[dict]:
        return self._get_all_lambda(data=self._get()['rows'], lam=self._fmap)

    def get_with_barcode(self, barcode:int=0) -> dict:
        if not barcode:
            return {}
        for item in self._get_normal():
            if item['barcode'] == barcode:
                return item

    def register_product(self, uuid:str='', quantity:int=0):
        data = self._filter_data(
            data=self._get()['rows'],
            lam=lambda x: x['id'] == uuid
        )[0]
        data['quantity'] += float(quantity)
        data['stock'] += float(quantity)
        return self._put(
            uuid=uuid,
            data=data
        ).json()

    def delete(self, id: str=None):
        if id is None:
            raise
        return

if __name__ == '__main__':
    ms = MoySklad(token=argv[1], test=False)
    # filtred_list = list(filter(
    #     lambda x: x['code'] == '32121903',
    #     ms._get()['rows']
    # ))
    # pprint(filtred_list)
    # ms.register_product(uuid='0862a568-cb55-11ee-0a80-16c200085f85')
    data = list(filter(
        lambda x: x['barcodes'][0]['ean13'] == '2000000008356',
        ms._get()['rows']
    ))[0]
    data2 = list(filter(
        lambda x: x['code'] == '32121903',
        ms._get()['rows']
    ))[0]
