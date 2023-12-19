import customtkinter
import home

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Assign information to the window
        self.title("HardWareHouse")
        self.geometry("1280x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Open the Home Frame
        self.homeFrame = home.homePage(self)

app = App()
app.mainloop()