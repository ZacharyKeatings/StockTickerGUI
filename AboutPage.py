import tkinter as tk
from tkinter import ttk
import main
import MainMenu

class AboutPage(tk.Frame):

    def __init__(self, parent: main.MainWindow):
        tk.Frame.__init__(self, master=parent, bg=main.BGCOLOUR)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        tk.Label(
            master=self,
            text="About Stock Ticker",
            bg=main.BGCOLOUR,
            font=("Arial", 50)
        ).grid(row=0, column=0, sticky='new')
        tk.Label(
            master=self,
            text="The object of the game is to buy and sell stocks,\n and by so doing accumulate a greater amount of \n money than the other players. The winner is decided\n by setting a time limit at the start of the game, \n and is the person having the greatest amount of money\n when time elapses, after selling his stocks back to \nthe Broker at their final market value.",
            bg=main.BGCOLOUR,
            font=("Arial", 12)
        ).grid(row=1, column=0, sticky='new')
        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu.MainMenu(parent=self.parent))
        ).grid(row=2, column=0, columnspan=2, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=3, column=0, columnspan=2, sticky="sew")