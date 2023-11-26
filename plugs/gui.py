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
        pass


if __name__ == "__main__":
    App().mainloop()

