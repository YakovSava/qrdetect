from barcode import get
from barcode.writer import ImageWriter

ean_code = '4605393003315'

ean = get('ean13', ean_code, writer=ImageWriter())

filename = ean.save('test_code')