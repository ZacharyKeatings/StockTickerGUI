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

        self.mainmenu.pack(fill="both", expand=1)

    def switch_to(self, target):
        self.current.pack_forget()
        self.current = target
        self.current.pack(fill="both", expand=1)


class MainMenu(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #!Testing purposes only. Remove after completion===
        def list_players():
            for i in range(len(Player.players)):
                print(Player.players[i].name)
        #!=================================================

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

        self.player_range = [i for i in range(2, 9)]
        self.round_range = [i for i in range(1, 101)]

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
            bg="green"
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
            command=lambda: [Game.set_players(self.num_players.get()), Game.set_rounds(self.num_rounds.get()),
                             self.parent.switch_to(target=PlayerNamePage(parent=self.parent))]
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

        self.name_list = [self.p1_name, self.p2_name, self.p3_name, self.p4_name, 
                          self.p5_name, self.p6_name, self.p7_name, self.p8_name]

        def set_names():
            Player.players.clear()
            for player_name in range(Game.num_players):
                player = Player(name=self.name_list[player_name].get())
                Player.players.append(player)

        # create all 8 player widgets, but only pack based on num_players
        for num in range(Game.num_players):
            self.grid_rowconfigure(num + 1, weight=1)
            tk.Label(master=self, text=f"Player {num + 1}:", bg="green").grid(row=num + 1, column=1, sticky="w")
            tk.Entry(master=self, textvariable=self.name_list[num]).grid(row=num + 1, column=1, sticky="e")
            ttk.Button(master=self, text="Submit",
                       command=lambda: [set_names(), self.parent.switch_to(target=GameSetup(parent=self.parent))]
                      ).grid(row=9, column=1, sticky="new")

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


#!create labelframe for [Buy, Sell, Pass] buttons.
#!create labelframes for each player that displays there money and all stock quantities.
#!display current players turn
#!buy button brings new frame on top of buy/sell/pass frame with 7 buttons: the 6 stocks plus back button.
#!after choosing stock,new labelframe goes on top with combobox and 2 buttons [ok, back].
#!combobox displays number of possible amounts to buy from 1 to max amount possible based on current player money.
#!after choosing stock amount and pressing ok, last frame appears with button labelled [are you sure?]
class GameSetup(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg="green")
        self.parent = parent
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        tk.Label(
            master=self,
            text="Game Setup round",
            bg="green"
        ).grid(row=0, column=0, columnspan=3, sticky='new')
        cur_player = tk.LabelFrame(
            master=self,
            text="Current Player:",
            bg="green"
        )
        cur_player.grid(row=1, column=1, sticky="ew")

        tk.Label(
            master=cur_player,
            text=Game.current_player_name(),
            bg="green"
        ).grid(column=1)

        self.player_grid = []
        for num in range(Game.num_players):
            widget = tk.LabelFrame(
                master=self,
                text=f"{Player.players[num].name}:",
                bg="green"
            )
            self.player_grid.append(widget)

        self.player_grid[0].grid(row=3, column=0, sticky="nsew")
        self.player_grid[1].grid(row=3, column=2, sticky='nsew')
        if Game.num_players == 3:
            self.player_grid[2].grid(row=4, column=1, sticky='nsew')
        if Game.num_players == 4:
            self.player_grid[2].grid(row=4, column=1, sticky='nsew')
            self.player_grid[3].grid(row=2, column=1, sticky='nsew')
        if Game.num_players == 5:
            self.player_grid[2].grid(row=4, column=1, sticky='nsew')
            self.player_grid[3].grid(row=2, column=1, sticky='nsew')
            self.player_grid[4].grid(row=2, column=0, sticky='nsew')
        if Game.num_players == 6:
            self.player_grid[2].grid(row=4, column=1, sticky='nsew')
            self.player_grid[3].grid(row=2, column=1, sticky='nsew')
            self.player_grid[4].grid(row=2, column=0, sticky='nsew')
            self.player_grid[5].grid(row=2, column=2, sticky='nsew')
        if Game.num_players == 7:
            self.player_grid[2].grid(row=4, column=1, sticky='nsew')
            self.player_grid[3].grid(row=2, column=1, sticky='nsew')
            self.player_grid[4].grid(row=2, column=0, sticky='nsew')
            self.player_grid[5].grid(row=2, column=2, sticky='nsew')
            self.player_grid[6].grid(row=4, column=0, sticky='nsew')
        if Game.num_players == 8:
            self.player_grid[2].grid(row=4, column=1, sticky='nsew')
            self.player_grid[3].grid(row=2, column=1, sticky='nsew')
            self.player_grid[4].grid(row=2, column=0, sticky='nsew')
            self.player_grid[5].grid(row=2, column=2, sticky='nsew')
            self.player_grid[6].grid(row=4, column=0, sticky='nsew')
            self.player_grid[7].grid(row=4, column=2, sticky='nsew')
        
        for num in range(Game.num_players):
            tk.Label(
                master=self.player_grid[num],
                text=f"Money: {Player.players[num].money}",
                bg="green"
            ).grid(sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Gold: {Player.players[num].stocks['Gold']}",
                bg="green"
            ).grid(sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Silver: {Player.players[num].stocks['Silver']}",
                bg="green"
            ).grid(sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Oil: {Player.players[num].stocks['Oil']}",
                bg="green"
            ).grid(sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Bonds: {Player.players[num].stocks['Bonds']}",
                bg="green"
            ).grid(sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Grain: {Player.players[num].stocks['Grain']}",
                bg="green"
            ).grid(sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Industrial: {Player.players[num].stocks['Industrial']}",
                bg="green"
            ).grid(sticky='w')

        ttk.Button(
            master=self,
            text="Pass",
            command=lambda: [Game.next_player(), self.parent.switch_to(target=GameSetup(parent=self.parent))]
        ).grid(row=3, column=1)

        ttk.Button(
            master=self,
            text="Back",
            command=lambda: self.parent.switch_to(target=PlayerNamePage(parent=self.parent))
        ).grid(row=6, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu(parent=self.parent))
        ).grid(row=7, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=8, column=0, columnspan=3, sticky="sew")


class Player:
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

    def create_player():
        new_player = Player()
        Player.players.append(new_player)

    def buy_stock(self):
        pass

    def sell_stock(self):
        pass


class Stock:
    stock_value = {
        "Gold": 100,
        "Silver": 100,
        "Oil": 100,
        "Bonds": 100,
        "Grain": 100,
        "Industrial": 100
    }

    def increase_value(self):
        pass

    def decrease_value(self):
        pass

    def double_stock(self):
        pass

    def split_stock(self):
        pass


class Game:
    num_players = 0
    curr_player = 0
    max_rounds = 0
    curr_round = 0

    def set_players(players):
        Game.num_players = players

    def set_rounds(rounds):
        Game.max_rounds = rounds

    def current_player_name():
        return Player.players[Game.curr_player].name

    def next_player():
        if Game.curr_player == Game.num_players-1:
            Game.curr_player = 0
        else:
            Game.curr_player += 1

def main():
    return MainWindow().mainloop()


if __name__ == '__main__':
    sys.exit(main())
