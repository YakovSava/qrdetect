import base64
import requests

from time import strftime
from json import loads as loads_json, dumps as dumps_json
from toml import loads as loads_toml, dumps as dumps_toml
from typing import Callable
from pprint import pprint  # A temporary solution
from sys import argv  # A temporary solution
from random import randint  # A temporary solution


class _MoySkladConfigBinder:

    def __init__(self, config_filename: str = 'msconf.toml'):
        self._filename = config_filename
        self.config = {}
        self._reload()

    def _reload(self):
        with open(self._filename, 'r', encoding='utf-8') as file:
            self.config = loads_toml(file.read())

    def edit(self, new_conf: dict = {}):
        with open(self._filename, 'w', encoding='utf-8') as file:
            file.write(dumps_toml(new_conf))
        self._reload()


class MoySklad:

    def __init__(self, token: str = "", test: bool = False, binder: _MoySkladConfigBinder = _MoySkladConfigBinder()):
        self._binder = binder
        self._token = token
        self._headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            "Accept-Encoding": "gzip"
        }
        self._start_url = "https://api.moysklad.ru/api/remap/1.2/"
        self._is_test = test

    def _get(self, method: str = 'entity/assortment'):
        if self._is_test:
            with open('test.json', 'r', encoding='utf-8') as file:
                return loads_json(file.read())
        else:
            resp = requests.get(
                url=self._start_url + method,
                headers=self._headers
            )
            return resp.json()

    def _post(self, method: str = 'entity/assortment', data: dict = {}):
        resp = requests.post(
            url=self._start_url + method,
            headers=self._headers,
            data=dumps_json(data)
        )
        return resp.json()

    def _get_all_lambda(self, data: list = [], lam: Callable = lambda x: x) -> list:
        return list(map(
            lam,
            data
        ))

    def _filter_data(self, data: list = [], lam: Callable = lambda x: x) -> list:
        return list(filter(
            lam,
            data
        ))

    def _fmap(self, x: dict):
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

    def _test_register_product(self):
        '''
        Need this:
        {
            "name": "enter100",
            "externalCode": "34981sawfa42kek",
            "moment": "2016-06-21 16:56:52",
            "applicable": true,
            "sum": 51241240
            "organization": ...
            "store": ...
            "positions": [{
                "quantity": {quantity},
                "price": 0.0,
                "assortment": {
                    "meta": {
                        "href": "https://api.moysklad.ru/api/remap/1.2/entity/product/{product_uuid}",
                        "metadataHref": "https://api.moysklad.ru/api/remap/1.2/entity/product/metadata",
                        "type": "product",
                        "mediaType": "application/json"
                    }
                },
                "overhead": 0
                }]
            }
        '''
        data = self._get(method='entity/enter')
        pprint(data)
        self._binder.config['default']['register'] = str({'store': data['rows'][0]['store'], 'organization': data['rows'][0]['organization']})
        self._binder.edit(self._binder.config)

    def _test_write_downs_product(self):
        ...

    def get_with_barcode(self, barcode: int = 0) -> dict:
        if not barcode:
            return {}
        for item in self._get_normal():
            if item['barcode'] == barcode:
                return item

    def register_product(self, uuid: str = '', quantity: int = 0):
        ...

    def write_downs_product(self, uuid: str = None):
        ...


if __name__ == '__main__':
    ms = MoySklad(token=argv[1], test=False)
    ms._test_register_product()
