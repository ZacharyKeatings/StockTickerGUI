import tkinter as tk
from tkinter import ttk
import main
import GameSetup
import NewGame
import Player
import Game

class PlayerNamePage(tk.Frame):

    def __init__(self, parent: main.MainWindow):
        tk.Frame.__init__(self, master=parent, bg=main.BGCOLOUR)
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.p1_name = tk.StringVar()
        self.p2_name = tk.StringVar()
        self.p3_name = tk.StringVar()
        self.p4_name = tk.StringVar()
        self.p5_name = tk.StringVar()
        self.p6_name = tk.StringVar()
        self.p7_name = tk.StringVar()
        self.p8_name = tk.StringVar()

        self.name_list = [self.p1_name, self.p2_name, self.p3_name, self.p4_name, 
                          self.p5_name, self.p6_name, self.p7_name, self.p8_name]

        tk.Label(
            master=self,
            text="Pick your names",
            bg=main.BGCOLOUR
        ).grid(row=0, column=1, sticky='new')

        blank_name_label = tk.Label(
            master=self,
            text="All players must be given a name!",
            bg=main.BGCOLOUR,
            fg="red"
        )

        def check_empty_name():
            #Check that names are empty. If they are, display message "Name cannot be blank". If they are filled in, run set names and switch to gamesetup.
            name_check = True
            for player_name in range(Game.Game.num_players):
                player = self.name_list[player_name].get()
                if player == "":
                    name_check = False
            if name_check is False:
                blank_name_label.grid(row=1, column=1, sticky="snew")
            else:
                set_names()
                self.parent.switch_to(target=GameSetup.GameSetup(parent=self.parent))

        def set_names():
            # Player.Player.players.clear()
            for player_name in range(Game.Game.num_players):
                player = Player.Player(name=self.name_list[player_name].get())
                Player.Player.players.append(player)

        # create all 8 player widgets, but only pack based on num_players
        for num in range(Game.Game.num_players):
            self.grid_rowconfigure(num + 2, weight=1)
            tk.Label(master=self, text=f"Player {num + 1}:", bg=main.BGCOLOUR).grid(row=num + 2, column=1, sticky="nw")
            tk.Entry(master=self, textvariable=self.name_list[num]).grid(row=num + 2, column=1, sticky="ne")
            ttk.Button(master=self, text="Submit",
                       command=check_empty_name
                      ).grid(row=10, column=1, sticky="new")

        ttk.Button(
            master=self,
            text="Back",
            command=lambda: self.parent.switch_to(target=NewGame.NewGame(parent=self.parent))
        ).grid(row=11, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=12, column=0, columnspan=3, sticky="sew")