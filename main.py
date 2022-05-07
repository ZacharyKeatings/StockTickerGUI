import sys
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Stock Ticker")
        self.geometry("800x600")
        self.iconbitmap("./images/icon.ico")
        self.mainmenu = MainMenu(parent=self)
        self.current = self.mainmenu

        self.mainmenu.pack(fill="both", expand="true")

    def switch_to(self, target):
        self.current.pack_forget()
        self.current = target
        self.current.pack(fill="both", expand="true")

class MainMenu(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        def list_players():
            for i in range(len(Player.players)):
                print(Player.players[i].name)

        tk.Label(
            master=self,
            text="STOCK TICKER",
            bg="green",
            font=("Arial", 50)
        ).grid(row=0, column=0, columnspan=2, sticky="new")
        ttk.Button(
            master=self,
            text="New Game",
            command=lambda: self.parent.switch_to(target=NewGame(parent=self.parent))
        ).grid(row=1, column=0, columnspan=2, sticky="sew")
        ttk.Button(
            master=self,
            text="About",
            command=lambda: self.parent.switch_to(target=AboutPage(parent=self.parent))
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
        ttk.Button(
            master=self,
            text="Test Button",
            command=list_players
        ).grid(row=6, column=0, columnspan=2, sticky='sew')

class AboutPage(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg="green")
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        tk.Label(
            master=self,
            text="About Stock Ticker",
            bg="green",
            font=("Arial", 50)
        ).grid(row=0, column=0, sticky='new')
        tk.Label(
            master=self,
            text="The object of the game is to buy and sell stocks,\n and by so doing accumulate a greater amount of \n money than the other players. The winner is decided\n by setting a time limit at the start of the game, \n and is the person having the greatest amount of money\n when time elapses, after selling his stocks back to \nthe Broker at their final market value.",
            bg="green",
            font=("Arial", 12)
        ).grid(row=1, column=0, sticky='new')
        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu(parent=self.parent))
        ).grid(row=2, column=0, columnspan=2, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=3, column=0, columnspan=2, sticky="sew")

class NewGame(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.player_range = [i for i in range(2,9)]
        self.round_range = [i for i in range(1,101)]

        self.num_players = tk.IntVar()
        self.num_rounds = tk.IntVar()

        tk.Label(
            master=self,
            text="New game",
            bg="green"
        ).grid(row=0, column=1, sticky='new')
        tk.Label(
            master=self,
            text="Please choose the number of players:",
            bg="green"
        ).grid(row=1, column=1, sticky='n')
        ttk.Combobox(
            master=self,
            textvariable=self.num_players,
            state="readonly",
            values=self.player_range
        ).grid(row=2, column=1, sticky='n')
        tk.Label(
            master=self,
            text="Please choose the number of rounds:",
            bg="green"
        ).grid(row=3, column=1, sticky='n')
        ttk.Combobox(
            master=self,
            textvariable=self.num_rounds,
            state="readonly",
            values=self.round_range
        ).grid(row=4, column=1, sticky='n')
        ttk.Button(
            master=self,
            text="Submit",
            command=lambda: [Game.set_players(self.num_players.get()), Game.set_rounds(self.num_rounds.get()), self.parent.switch_to(target=PlayerNamePage(parent=self.parent))]
        ).grid(row=5, column=1, sticky="new")
        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu(parent=self.parent))
        ).grid(row=6, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=7, column=0, columnspan=3, sticky="sew")

class PlayerNamePage(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
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

        self.name_list = [self.p1_name, self.p2_name, self.p3_name, self.p4_name, self.p5_name, self.p6_name, self.p7_name, self.p8_name]

        def set_names():
            for player_name in range(Game.num_players):
                player = Player(name=self.name_list[player_name].get())
                Player.players.append(player)

        #create all 8 player widgets, but only pack based on num_players
        for num in range(Game.num_players):
            self.grid_rowconfigure(num + 1, weight=1)
            tk.Label(master=self, text=f"Player {num + 1}:", bg="green").grid(row=num + 1, column=1, sticky="w")
            tk.Entry(master=self, textvariable=self.name_list[num]).grid(row=num + 1, column=1, sticky="e")
            ttk.Button(master=self, text="Submit", command=set_names).grid(row=9, column=1, sticky="new")

        tk.Label(
            master=self,
            text="Pick your names",
            bg="green"
        ).grid(row=0, column=1, sticky='new')

        ttk.Button(
            master=self,
            text="Back",
            command=lambda: self.parent.switch_to(target=NewGame(parent=self.parent))
        ).grid(row=9, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=10, column=0, columnspan=3, sticky="sew")

class Player():
    players = []

    def __init__(self, name):
        self.name = name
        self.money = 5000
        self.stocks = {
            "Gold": 0,
            "Silver": 0,
            "Oil": 0,
            "Bonds": 0,
            "Grain": 0,
            "Industrial": 0
        }

    def create_player(player_name):
        new_player = Player(player_name)
        Player.players.append(new_player)

    def buy_stock(stock):
        pass

    def sell_stock(stock):
        pass

class Stock():
    stock_value = {
        "Gold": 100,
        "Silver": 100,
        "Oil": 100,
        "Bonds": 100,
        "Grain": 100,
        "Industrial": 100
    }

    def increase_value(stock):
        pass

    def decrease_value(stock):
        pass

    def double_stock(stock):
        pass

    def split_stock(stock):
        pass

class Game():
    num_players = 0
    max_rounds = 0

    def set_players(players):
        Game.num_players = players

    def set_rounds(rounds):
        Game.max_rounds = rounds


def main():
    return MainWindow().mainloop()


if __name__ == '__main__':
    sys.exit(main())
