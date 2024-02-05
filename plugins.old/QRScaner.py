from tkinter.messagebox import askokcancel, showerror
from threading import Thread
from time import sleep
from toml import loads
from typing import Callable
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image
from qrdecoder import Decoder

class AppScan(CTk):

    def __init__(self, decoder: Decoder=Decoder()):
        super().__init__()

        self.dec = decoder

        self.title("CityBox: QR Scaner")
        self.geometry("600x500")

        self._login_window()

        self._run = True
        self._th = False

    def _login_window(self):

        self.login_label = CTkLabel(
            master=self, text="Пожалуйста, войдите в систему")
        self.login_label.pack(pady=10)

        self.username_entry = CTkEntry(
            master=self, placeholder_text="Введите ID бригады")
        self.username_entry.pack(pady=10)

        self.login_button = CTkButton(
            master=self, text="Войти", command=self._authorize)
        self.login_button.pack(pady=20)

    def _authorize(self):
        if self.username_entry.get() not in _config.brigades:
            showerror('CityBox: Ошибка!', 'Такого ID не существует')
        else:
            self._open_photo_window()

    def _quit_from_frame(self):
        self._run = False
        if askokcancel('CityBox: Подтверждение', 'Вы точно хотите выйти?'):
            self.exit_button.destroy()
            self._photo_element.destroy()
            self.photo_description.destroy()

            self._login_window()
        else:
            self._open_photo_window()

    def _stop_check(self):
        self._run = False

    def _open_photo_window(self):
        self.login_label.destroy()
        self.username_entry.destroy()
        self.login_button.destroy()

        self.exit_button = CTkButton(
            master=self, text="Выйти", command=self._quit_from_frame)
        self.exit_button.pack(anchor='nw', pady=20)

        # self.stop_button = CTkButton(master=self, text="Тестово остановить процесс", command=self._stop_check)
        # self.stop_button.pack(anchor='nw', pady=20)

        self._photo_element = CTkLabel(master=self,
                                       image=CTkImage(light_image=Image.open('white.jpg'),
                                                      dark_image=Image.open(
                                                          'white.jpg'),
                                                      size=(150, 100)),
                                       text='')
        self._photo_element.pack(pady=10)

        self.photo_description = CTkLabel(
            master=self, text="Здесь будет описание фото")
        self.photo_description.pack(pady=10)

        self._update_photo()

        if not self._th:
            self._th = Thread(target=self._update_after,
                              args=(lambda: self._run, 1,))
            self._th.start()

    def _update_after(self, func: Callable, sec: float):
        while True:
            sleep(sec)
            self._update_photo()
            if not func():
                break

    def _update_photo(self):
        img, data = self.dec.decode()
        if data:
            self.photo_description.configure(require_redraw=True, text=data)
        else:
            self.photo_description.configure(
                require_redraw=True, text="Не распознано")
        self._photo_element.configure(require_redraw=True, image=CTkImage(light_image=Image.open(img),
                                                                          dark_image=Image.open(
                                                                              img),
                                                                          size=(150, 100)))
