import sys
import tkinter as tk


class MainWindow(tk.Tk):
    """
    This is your main window
    """
    def __init__(self):
        # any arguments you would pass to
        # window = tk.Tk() go here. This call
        # does the set up necessary for a Tk object
        tk.Tk.__init__(self)
        self.title("Stock Ticker")
        self.geometry("600x400")
        self.iconbitmap("./images/icon.ico")
        MainMenu(parent = self).pack(fill="both", expand="true")

    def switch_to_main_menu(self):
        self.clear()
        MainMenu(parent = self).pack(fill="both", expand="true")

    def switch_to_about_page(self):
        self.clear()
        AboutPage(parent = self).pack(fill="both", expand="true")

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

class MainMenu(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master = parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        
        tk.Label(
            master = self, 
            text="this is the main menu"           
        ).grid(row=0, column=0, columnspan=2, sticky="new")
        tk.Button(
            master = self, 
            text="About",
            command = self.parent.switch_to_about_page
        ).grid(row=1, column=0, columnspan=2, sticky="sew")
        tk.Button(
            master = self, 
            text="Quit", 
            command=lambda : exit()
        ).grid(row=2, column=0, columnspan=2, sticky='sew')

class AboutPage(tk.Frame):
 
    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master = parent, bg="blue")
        self.parent = parent
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)

        tk.Label(
            master = self, 
            text="About Stock Ticker", 
            bg="purple"
        ).grid(row=0, column=0, sticky='new')
        tk.Label(
            master = self, 
            text="The object of the game is to buy and sell stocks,\n and by so doing accumulate a greater amount of \n money than the other players. The winner is decided\n by setting a time limit at the start of the game, \n and is the person having the greatest amount of money\n when time elapses, after selling his stocks back to \nthe Broker at their final market value."
        ).grid(row=1, column=0, sticky='new')
        tk.Button(
            master = self, 
            text="Main Menu", 
            command = self.parent.switch_to_main_menu
        ).grid(row=2, column=0, columnspan=2, sticky="sew")
        tk.Button(
            master = self, 
            text="Quit", 
            command=lambda : exit()
        ).grid(row=3, column=0, columnspan=2, sticky="sew")

def main():
    return MainWindow().mainloop()

if __name__ == '__main__':
    sys.exit(main())