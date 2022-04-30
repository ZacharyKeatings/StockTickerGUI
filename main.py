import sys
import tkinter as tk


class MainWindow(tk.Tk):
    """
    This is your main window
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Stock Ticker")
        self.geometry("600x400")
        self.iconbitmap("./images/icon.ico")
        MainMenu(parent = self).pack(fill="both", expand="true")

    def switch_to_main_menu(self):
        self.clear()
        MainMenu(parent = self).pack(fill="both", expand="true")

    def switch_to_new_game(self):
        self.clear()
        NewGame(parent = self).pack(fill="both", expand="true") 

    def switch_to_about_page(self):
        self.clear()
        AboutPage(parent = self).pack(fill="both", expand="true")

    def switch_to_load_game(self):
        self.clear()
        AboutPage(parent = self).pack(fill="both", expand="true") ######### 

    def switch_to_highscores(self):
        self.clear()
        AboutPage(parent = self).pack(fill="both", expand="true") #########

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

class MainMenu(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master = parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        tk.Label(
            master = self, 
            text="STOCK TICKER",
            bg="green",
            font=("Arial", 50)     
        ).grid(row=0, column=0, columnspan=2, sticky="new")
        tk.Button(
            master = self, 
            text="New Game",
            command = self.parent.switch_to_new_game
        ).grid(row=1, column=0, columnspan=2, sticky="sew")
        tk.Button(
            master = self, 
            text="About",
            command = self.parent.switch_to_about_page
        ).grid(row=2, column=0, columnspan=2, sticky="sew")
        tk.Button(
            master = self, 
            text="Load Game",
            command = self.parent.switch_to_load_game, 
            state = tk.DISABLED
        ).grid(row=3, column=0, columnspan=2, sticky="sew")
        tk.Button(
            master = self, 
            text="Highscores",
            command = self.parent.switch_to_highscores, 
            state = tk.DISABLED
        ).grid(row=4, column=0, columnspan=2, sticky="sew")
        tk.Button(
            master = self, 
            text="Quit", 
            command=lambda : exit()
        ).grid(row=5, column=0, columnspan=2, sticky='sew')

class NewGame(tk.Frame):
 
    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master = parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


        tk.Label(
            master = self, 
            text="New game", 
            bg="green" 
        ).grid(row=0, column=1, sticky='new')
        tk.Label(
            master = self, 
            text="Please choose the number of players:", 
            bg="green"
        ).grid(row=1, column=1, sticky='nw')
        tk.Entry(
            master = self, 
            text="test text"
        ).grid(row=1, column=1, sticky='ne')
        tk.Button(
            master = self, 
            text="Main Menu", 
            command = self.parent.switch_to_main_menu
        ).grid(row=2, column=0, columnspan=3, sticky="sew")
        tk.Button(
            master = self, 
            text="Quit", 
            command=lambda : exit()
        ).grid(row=3, column=0, columnspan=3, sticky="sew")

class AboutPage(tk.Frame):
 
    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master = parent, bg="green")
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        tk.Label(
            master = self, 
            text="About Stock Ticker", 
            bg="green",
            font=("Arial", 50) 
        ).grid(row=0, column=0, sticky='new')
        tk.Label(
            master = self, 
            text="The object of the game is to buy and sell stocks,\n and by so doing accumulate a greater amount of \n money than the other players. The winner is decided\n by setting a time limit at the start of the game, \n and is the person having the greatest amount of money\n when time elapses, after selling his stocks back to \nthe Broker at their final market value.",
            bg="green",
            font=("Arial", 12) 
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