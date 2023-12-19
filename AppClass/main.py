import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Assign information to the window
        self.title("HardWareHouse")
        self.geometry("1920x1080")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Open the window
        self

app = App()
app.mainloop()