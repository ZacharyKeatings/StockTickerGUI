import tkinter as tk
from tkinter import ttk
import main
import Stock
import NewGame
import AboutPage

class MainMenu(tk.Frame):

    def __init__(self, parent: main.MainWindow):
        tk.Frame.__init__(self, master=parent, bg=main.BGCOLOUR)
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        tk.Label(
            master=self,
            text="STOCK TICKER",
            bg=main.BGCOLOUR,
            font=("Arial", 50)
        ).grid(row=0, column=0, columnspan=2, sticky="new")
        ttk.Button(
            master=self,
            text="New Game",
            command=lambda: [Stock.Stock.reset_values(), self.parent.switch_to(target=NewGame.NewGame(parent=self.parent))]
        ).grid(row=1, column=0, columnspan=2, sticky="sew")
        ttk.Button(
            master=self,
            text="About",
            command=lambda: self.parent.switch_to(target=AboutPage.AboutPage(parent=self.parent))
        ).grid(row=2, column=0, columnspan=2, sticky="sew")
        ttk.Button(
            master=self,
            text="Load Game",
            # command = self.parent.switch_to_load_game, 
            state=tk.DISABLED
        ).grid(row=3, column=0, columnspan=2, sticky="sew")
        ttk.Button(
            master=self,
            text="Highscores",
            # command = self.parent.switch_to_highscores, 
            state=tk.DISABLED
        ).grid(row=4, column=0, columnspan=2, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=5, column=0, columnspan=2, sticky='sew')