from tkinter.messagebox import askokcancel
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton,\
    CTkOptionMenu

class App(CTk):

    def __init__(self, img_path:str=""):
        super().__init__()

        self.title("CityBox: QR Generator")
        self.geometry("500x400")

        self._img_path = img_path

        self._start()

    def _start(self):
        self.idlabel = CTkLabel(self, text="Введите пожалуйста ID бригады", anchor="center")
        self.idlabel.pack(pady=(20, 10))

        self.identer = CTkEntry(self, width=200)
        self.identer.place(relx=0.5, rely=0.5, anchor="center")

        self.idok = CTkButton(self, text="ОК", command=self._switch)
        self.idok.place(relx=0.5, rely=0.5, anchor="center", y=30)

    def _switch(self):
        self.idlabel.destroy()
        self.identer.destroy()
        self.idok.destroy()

        self.exit_label = CTkLabel(self, text="Нажимать при окончании работы!")
        self.exit_job = CTkButton(self, text="Выход", width=120, command=self._restart)

        self.color_label = CTkLabel(self, text="Выберите цвет")
        self.color_menu = CTkOptionMenu(self, values=["Розовый", "Синий", "Красный"])

        self.size_label = CTkLabel(self, text="Введите размер")
        self.size_menu = CTkEntry(
            self)
        self.okbut = CTkButton(self, text="Подтвердить")

        self.exit_label.pack(anchor='nw', pady=10)
        self.exit_job.pack(anchor='nw', padx=10)
        self.color_label.pack(pady=10)
        self.color_menu.pack(pady=10)
        self.size_label.pack(pady=10)
        self.size_menu.pack(pady=10)
        self.okbut.pack(pady=10)

    def _restart(self):
        pass


if __name__ == "__main__":
    App().mainloop()

