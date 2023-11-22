import qrcode
from PIL import Image

# Создание QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Добавление данных в QR-код
data = "I_love_you" # Karina I love you
qr.add_data(data)
qr.make(fit=True)

# Генерация изображения QR-кода
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img = qr_img.convert("RGBA")

# Загрузка изображения для центрального размещения
center_image = Image.open("test2.png")

# Центрирование изображения
qr_width, qr_height = qr_img.size
center_width, center_height = center_image.size
center_x = int((qr_width - center_width) / 2)
center_y = int((qr_height - center_height) / 2)

# Вставка изображения в центр QR-кода
qr_img.paste(center_image, (center_x, center_y), center_image)

# Сохранение сгенерированного QR-кода с центральным изображением
qr_img.save("qr_code.png")
