from tkinter.messagebox import askokcancel, showerror
from toml import loads
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton,\
    CTkOptionMenu, CTkFrame, CTkImage
from PIL import Image
from qrdecoder import Decoder

class AppConfig:

    def __init__(self):
        self._config_filename = "appconf.ini"

    def _load(self):
        with open(self._config_filename, 'r', encoding='utf-8') as file:
            self.conf = loads(file.read())

    def __getattr__(self, itemname:str):
        self._load()
        return self.conf.get(itemname)

_config = AppConfig()

class AppCreate(CTk):

    def __init__(self):
        super().__init__()

        self.title("CityBox: QR Generator")
        self.geometry("500x400")

        self._start()

    def _start(self):
        self.idlabel = CTkLabel(self, text="Введите пожалуйста ID бригады", anchor="center")
        self.idlabel.pack(pady=(20, 10))

        self.identer = CTkEntry(self, width=200)
        self.identer.place(relx=0.5, rely=0.5, anchor="center")

        self.idok = CTkButton(self, text="ОК", command=self._check_brigades)
        self.idok.place(relx=0.5, rely=0.5, anchor="center", y=30)

    def _check_brigades(self):
        if self.identer.get() not in _config.brigades:
            showerror("Ошибка!", "ID бригады неверен")
        else:
            self._switch()

    def _send(self):
        if not self.size_menu.get().isnumeric():
            showerror("Ошибка!", "Введите только цифры!")
            return
        showerror("Заглушка", f"Ну типа отправлено\nЦвет: {self.color_menu.get()}\nРазмер: {self.size_menu.get()}")

    def _switch(self):
        self.idlabel.destroy()
        self.identer.destroy()
        self.idok.destroy()

        self.exit_label = CTkLabel(self, text="Нажимать при окончании работы!")
        self.exit_job = CTkButton(self, text="Выход", width=120, command=self._restart)

        self.color_label = CTkLabel(self, text="Выберите цвет")
        self.color_menu = CTkOptionMenu(self, values=_config.colors)

        self.size_label = CTkLabel(self, text="Введите размер")
        self.size_menu = CTkEntry(
            self)
        self.okbut = CTkButton(self, text="Подтвердить", command=self._send)

        self.exit_label.pack(anchor='nw', pady=10)
        self.exit_job.pack(anchor='nw', padx=10)
        self.color_label.pack(pady=10)
        self.color_menu.pack(pady=10)
        self.size_label.pack(pady=10)
        self.size_menu.pack(pady=10)
        self.okbut.pack(pady=10)

    def _restart(self):
        self.exit_label.destroy()
        self.exit_job.destroy()
        self.color_label.destroy()
        self.color_menu.destroy()
        self.size_label.destroy()
        self.size_menu.destroy()
        self.okbut.destroy()

        if askokcancel("QR Generator: question", "Вы уверены?"):
            self._start()
        else:
            self._switch()



class AppScan(CTk):

    def __init__(self, decoder:Decoder=Decoder()):
        super().__init__()

        self.dec = decoder

        self.title("CityBox: QR Scaner")
        self.geometry("500x400")

        self._login_window()

    def _login_window(self):

        self.login_label = CTkLabel(master=self, text="Пожалуйста, войдите в систему")
        self.login_label.pack(pady=10)

        self.username_entry = CTkEntry(master=self, placeholder_text="Введите ID бригады")
        self.username_entry.pack(pady=10)

        self.login_button = CTkButton(master=self, text="Войти", command=self._authorize)
        self.login_button.pack(pady=20)

    def _authorize(self):
        if self.username_entry.get() not in _config.brigades:
            showerror('Ошибка!', 'Такого ID не существует')
        else:
            self._open_photo_window()

    def _quit_from_frame(self):
        if askokcancel('Подтверждение', 'Вы точно хотите выйти?'):
            self.exit_button.destroy()
            self._photo_element.destroy()
            self.photo_description.destroy()

            self._login_window()
        else:
            self._open_photo_window()

    def _open_photo_window(self):
        self.login_label.destroy()
        self.username_entry.destroy()
        self.login_button.destroy()

        self.exit_button = CTkButton(master=self, text="Выйти", command=self._quit_from_frame)
        self.exit_button.pack(anchor='nw', pady=20)

        self._photo_element = CTkLabel(master=self,
                                       image=CTkImage(light_image=Image.open('white.jpg'),
                                                      dark_image=Image.open('white.jpg'),
                                                      size=(150, 100)),
                                       text='')
        self._photo_element.pack(pady=10)

        self.photo_description = CTkLabel(master=self, text="Здесь будет описание фото")
        self.photo_description.pack(pady=10)

        self._update_photo()

        self.after(1000, self._update_photo)

    def _update_photo(self):
        img, data = self.dec.decode()
        if data:
            self.photo_description.configure(require_redraw=True, text=data)
        else:
            self.photo_description.configure(require_redraw=True, text="Не распознано")
        self._photo_element.configure(require_redraw=True, image=CTkImage(light_image=Image.open(img),
                                                                          dark_image=Image.open(img),
                                                                          size=(150, 100)))


if __name__ == "__main__":
    AppScan().mainloop()

