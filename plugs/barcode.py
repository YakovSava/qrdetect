from barcode import get
from barcode.writer import ImageWriter, BaseWriter

class Barcode:

    def __init__(self, writer:BaseWriter=ImageWriter()):
        self._writer = writer

    def render(self, barcode:str, filename:str=None):
        if filename:
            filename = f'barcode{barcode}'
        return get('ean13', barcode, writer=self._writer).save(filename)