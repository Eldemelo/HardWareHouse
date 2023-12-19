import customtkinter
import pyodbc

# Define homePage frame for GUI
class homePage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, padx=10, pady=10, sticky="NSWE")

        # Detects if database does not exist and initializes a new one
        databaseExists = True
        if databaseExists != True:
            self.initializeDatabase()
        return
               

    # Function to intialize the database
    def initializeDatabase(self):
        print("test")
        return