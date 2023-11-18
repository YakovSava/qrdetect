import cv2

img = cv2.imread("qr_code.png")
detector = cv2.QRCodeDetector()

# обнаружить и декодировать
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # отображаем изображение с линиями
    # длина ограничивающей рамки
    n_lines = len (bbox)
    for i in range(n_lines):
        # рисуем все линии
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
