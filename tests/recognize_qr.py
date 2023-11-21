import cv2

img = cv2.imread("qr_code.png")
detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    print(f"QRCode data:\n{data}")

    n_lines = len(bbox)
    for i in range(n_lines):

        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
