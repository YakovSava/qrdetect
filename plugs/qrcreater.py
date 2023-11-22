from hashlib import sha1
from typing import Any
from qrcode import QRCode, constants
from PIL import Image

class QRCodeGenerator:

    def __init__(self,
            back_img:str=None,
            qr_model:QRCode=None
        ):
        if not back_img:
            raise
        else:
            self._center_image = Image.open(back_img)
        if qr_model is None:
            self._qr_model = QRCode(
                version=1,
                error_correction=constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
        else:
            self._qr_model = qr_model

    def _made_filename(self, data:Any) -> str:
        return sha1(data.encode()).hexdigest()

    def make_qr(self, data:Any=None) -> str:
        data = str(data)
        filename = self._made_filename(data)

        self._qr_model.add_data(data)
        self._qr_model.make(fit=True)

        qr_img = self._qr_model.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.convert("RGBA")

        qr_width, qr_height = qr_img.size
        center_width, center_height = self._center_image.size
        center_x = int((qr_width - center_width) / 2)
        center_y = int((qr_height - center_height) / 2)
        qr_img.paste(self._center_image, (center_x, center_y), self._center_image)

        qr_img.save(filename+".png")
        return filename