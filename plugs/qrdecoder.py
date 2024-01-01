import cv2


class Decoder:

    def __init__(self):
        self._cap = cv2.VideoCapture(0)
        self._detector = cv2.QRCodeDetector()

    def decode(self) -> tuple:
        _, img = self._cap.read()
        data, bbox, _ = self._detector.detectAndDecode(img)
        cv2.imwrite('temp.jpg', img)
        if bbox is not None:
            print(data)
            return 'temp.jpg', data
        else:
            return 'temp.jpg', False

    def __del__(self):
        self._cap.release()
        cv2.destroyAllWindows()
