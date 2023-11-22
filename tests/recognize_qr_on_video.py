import cv2
cap = cv2.VideoCapture(0)

# инициализируем детектор QRCode cv2
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # обнаружить и декодировать
    data, bbox, _ = detector.detectAndDecode(img)
    # проверяем, есть ли на изображении QRCode
    if bbox is not None:
        # отображаем изображение с линиями
        if data:
            print("[+] QR Code detected, data:", data)
    # отобразить результат
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()