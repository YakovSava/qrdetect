from customtkinter import CTk, CTkImage, CTkFrame

class App(CTk):

    def __init__(self, img_path:str=""):
        super().__init__()

        self.title("CityBox: QR Generator")
        self.geometry("700x450")

        self._img_path = img_path

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

