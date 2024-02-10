from tkinter.messagebox import askokcancel, showerror
from toml import loads
from typing import Callable, TYPE_CHECKING
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton,\
    CTkOptionMenu, StringVar, NORMAL, DISABLED

if TYPE_CHECKING:
    from .barcode import Barcode

def _set_state_for_all_widgets(widget_list, state):
    for widget in widget_list:
        widget.configure(state=state)

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
        self.idlabel.bind('<Return>', self._check_brigades)

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

class UnderAppScanner(CTk):
    def __init__(self, on_close_callback):
        super().__init__()

        self.on_close_callback = on_close_callback

        self.barcode = None

        self.title("CityBox: ожидание сканирования")
        self.geometry("200x150")  # Размер окна

        self._scan()

        self.protocol("WM_DELETE_WINDOW", self._exit)

    def _scan(self):
        self.enter = CTkEntry(self, placeholder_text='Отсканируйте код')
        self.enter.pack(pady=20, padx=20)
        self.enter.bind('<Return>', self._write_scan)

    def _write_scan(self, not_used_data):
        self.barcode = self.enter.get()
        self._exit()

    def _exit(self):
        if self.on_close_callback:
            self.on_close_callback(self.barcode)  # Отправляем результат назад в AppScaner
        self.destroy()

class AppScaner(CTk):

    def __init__(self, send_func:Callable):
        super().__init__()

        self._send = send_func
        self._widgets = []
        self._temp_barcode = None

        self.title("CityBox: управление списанием")
        self.geometry("400x300")  # Размер окна

        self._start()

    def _sending(self):
        status = self.status_menu.get()
        if status == 'Произведено':
            stat = 1
        elif status == 'Списано':
            stat = -1
        else:
            showerror('Ошибка', 'Укажите, товар произведён или списан!')
            return
        if self._temp_barcode is None:
            showerror('Ошибка', 'Отсканируйте штрих-код!')
            return
        self._send(stat, self._temp_barcode)
        self._temp_barcode = None

    def _init_scan_code(self):
        _set_state_for_all_widgets(self._widgets, DISABLED)

        def on_scan_close(scanned_barcode):
            _set_state_for_all_widgets(self._widgets, NORMAL)
            self._temp_barcode = scanned_barcode

        scanner = UnderAppScanner(on_close_callback=on_scan_close)
        scanner.grab_set()  # делаем модальным
        scanner.mainloop()

    def _start(self):
        self.idlabel = CTkLabel(
            self, text="Введите пожалуйста ID бригады", anchor="center")
        self.idlabel.pack(pady=(20, 10))
        self.idlabel.bind('<Enter>', self._check_brigades)

        self.identer = CTkEntry(self, width=200)
        self.identer.place(relx=0.5, rely=0.5, anchor="center")

        self.idok = CTkButton(self, text="ОК", command=self._check_brigades)
        self.idok.place(relx=0.5, rely=0.5, anchor="center", y=30)

    def _check_brigades(self):
        if self.identer.get() not in _config.brigades:
            showerror("CityBox: Ошибка!", "ID бригады неверен")
        else:
            self._scaner()

    def _scaner(self):
        self.idlabel.destroy()
        self.identer.destroy()
        self.idok.destroy()

        self.scan_button = CTkButton(self, text="Отсканировать код", command=self._init_scan_code)
        self.scan_button.pack(pady=20)

        self.status_var = StringVar()

        self.status_menu = CTkOptionMenu(self, variable=self.status_var, values=["Произведено", "Списано"])
        self.status_var.set("Выберите статус")
        self.status_menu.pack(pady=20)

        self.login_button = CTkButton(self, text="Отправить", command=self._sending)
        self.login_button.pack(pady=20)

        self._widgets.extend([self.scan_button, self.status_menu, self.login_button])

# Запуск приложения
if __name__ == "__main__":
    def send(*args, **kwargs):
        print(args, **kwargs)

    app = AppScaner(send)
    #app = UnderAppScanner()

    app.mainloop()