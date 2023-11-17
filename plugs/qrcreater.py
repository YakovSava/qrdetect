from typing import Any
from qrcode import make

class QRCodeGenerator:

    def __init__(self, back_img:str=None):
        if not back_img:
            self._img = False
        else:
            if isinstance(back_img, str):
                self._img = True
                self._back_img = back_img
            else:
                raise

    def make_qr(self, data:Any=None, filename:str=None) -> str:
        if (data is None) or (filename is None):
            raise
        else:
            ...