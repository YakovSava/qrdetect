from tkinter.messagebox import askokcancel, showerror
from toml import loads
from typing import Callable
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton,\
    CTkOptionMenu

class AppConfig:

    def __init__(self):
        self._config_filename = "appconf.ini"

    def _load(self):
        with open(self._config_filename, 'r', encoding='utf-8') as file:
            self.conf = loads(file.read())

    def __getattr__(self, itemname: str):
        self._load()
        return self.conf.get(itemname)


_config = AppConfig()


class AppCreate(CTk):

    def __init__(self, func: Callable):
        super().__init__()

        self.title("CityBox: QR Generator")
        self.geometry("600x500")
        self._start()

        self._fnc = func

    def _start(self):
        self.idlabel = CTkLabel(
            self, text="Введите пожалуйста ID бригады", anchor="center")
        self.idlabel.pack(pady=(20, 10))

        self.identer = CTkEntry(self, width=200)
        self.identer.place(relx=0.5, rely=0.5, anchor="center")

        self.idok = CTkButton(self, text="ОК", command=self._check_brigades)
        self.idok.place(relx=0.5, rely=0.5, anchor="center", y=30)

    def _check_brigades(self):
        if self.identer.get() not in _config.brigades:
            showerror("CityBox: Ошибка!", "ID бригады неверен")
        else:
            self._switch()

    def _send(self):
        if not self.size_menu.get().isnumeric():
            showerror("CityBox: Ошибка!", "Введите только цифры!")
            return
        self._fnc(
            color=self.color_menu.get(),
            size=self.size_menu.get()
        )

    def _switch(self):
        self.idlabel.destroy()
        self.identer.destroy()
        self.idok.destroy()

        self.exit_label = CTkLabel(self, text="Нажимать при окончании работы!")
        self.exit_job = CTkButton(
            self, text="Выход", width=120, command=self._restart)

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

        if askokcancel("CityBox: Подтверждение", "Вы уверены?"):
            self._start()
        else:
            self._switch()
