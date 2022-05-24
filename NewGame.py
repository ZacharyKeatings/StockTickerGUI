import tkinter as tk
from tkinter import ttk
import main
import Game
import PlayerNamePage
import MainMenu

class NewGame(tk.Frame):

    def __init__(self, parent: main.MainWindow):
        tk.Frame.__init__(self, master=parent, bg=main.BGCOLOUR)
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.player_range = [i for i in range(2, 9)]
        self.round_range = [i for i in range(1, 101)]

        self.num_players = tk.IntVar()
        self.num_rounds = tk.IntVar()

        tk.Label(
            master=self,
            text="New game",
            bg=main.BGCOLOUR
        ).grid(row=0, column=1, sticky='new')
        tk.Label(
            master=self,
            text="Please choose the number of players:",
            bg=main.BGCOLOUR
        ).grid(row=1, column=1, sticky='n')
        players = ttk.Combobox(
            master=self,
            textvariable=self.num_players,
            state="readonly",
            values=self.player_range
        )
        players.grid(row=2, column=1, sticky='n')
        players.current(0)
        tk.Label(
            master=self,
            text="Please choose the number of rounds:",
            bg=main.BGCOLOUR
        ).grid(row=3, column=1, sticky='n')
        rounds = ttk.Combobox(
            master=self,
            textvariable=self.num_rounds,
            state="readonly",
            values=self.round_range
        )
        rounds.grid(row=4, column=1, sticky='n')
        rounds.current(0)
        ttk.Button(
            master=self,
            text="Submit",
            command=lambda: [Game.Game.set_players(self.num_players.get()), Game.Game.set_rounds(self.num_rounds.get()),
                             self.parent.switch_to(target=PlayerNamePage.PlayerNamePage(parent=self.parent))]
        ).grid(row=5, column=1, sticky="new")
        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu.MainMenu(parent=self.parent))
        ).grid(row=6, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=7, column=0, columnspan=3, sticky="sew")