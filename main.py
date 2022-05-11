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
            # command=lambda: [print(Stock.stock_value["Gold"])]
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


#!after choosing stock,new labelframe goes on top with combobox and 2 buttons [ok, back].
#!combobox displays number of possible amounts to buy from 1 to max amount possible based on current player money.
#!after choosing stock amount and pressing ok, last frame appears with button labelled [are you sure?]
#!once stock has been purchased, use switch_to function to do a fresh load of page, just like Pass button does to update all displayed data
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
            text=Player.current_player_name(),
            bg="green"
        ).grid(column=1)

        #Create number of player frames based on number of players chosen in newgame page
        self.player_grid = []
        for num in range(Game.num_players):
            widget = tk.LabelFrame(
                master=self,
                text=f"{Player.players[num].name}:",
                bg="green"
            )
            self.player_grid.append(widget)

        #display all player frames on page that was just created above
        for num in range(Game.num_players):
            if num == 0:
                self.player_grid[0].grid(row=3, column=0, sticky="nsew")
            if num == 1:
                self.player_grid[1].grid(row=3, column=2, sticky='nsew')
            if num == 2:
                self.player_grid[2].grid(row=4, column=1, sticky='nsew')
            if num == 3:
                self.player_grid[3].grid(row=2, column=1, sticky='nsew')
            if num == 4:
                self.player_grid[4].grid(row=2, column=0, sticky='nsew')
            if num == 5:
                self.player_grid[5].grid(row=2, column=2, sticky='nsew')
            if num == 6:
                self.player_grid[6].grid(row=4, column=0, sticky='nsew')
            if num == 7:
                self.player_grid[7].grid(row=4, column=2, sticky='nsew')
        
        #Create all content to populate player frames
        for num in range(Game.num_players):
            tk.Label(
                master=self.player_grid[num],
                text=f"Money: {Player.players[num].money}",
                bg="green"
            ).grid(row=0, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Gold: {Player.players[num].stocks['Gold']}",
                bg="green"
            ).grid(row=1, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Silver: {Player.players[num].stocks['Silver']}",
                bg="green"
            ).grid(row=2, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Oil: {Player.players[num].stocks['Oil']}",
                bg="green"
            ).grid(row=3, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Bonds: {Player.players[num].stocks['Bonds']}",
                bg="green"
            ).grid(row=1, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Grain: {Player.players[num].stocks['Grain']}",
                bg="green"
            ).grid(row=2, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Industrial: {Player.players[num].stocks['Industrial']}",
                bg="green"
            ).grid(row=3, column=1, sticky='w')

        action_frame = tk.Frame(
            master=self,
            bg="blue"
        )
        action_frame.grid_rowconfigure(0, weight=1)
        action_frame.grid_rowconfigure(1, weight=1)
        action_frame.grid_rowconfigure(2, weight=1)
        action_frame.grid_columnconfigure(0, weight=1)
        action_frame.grid(row=3, column=1, sticky="nsew")
        ttk.Button(
            master=action_frame,
            text="Buy",
            command=lambda: buy_frame.grid(row=3, column=1, sticky='nsew')
        ).grid(row=0, column=0)
        ttk.Button(
            master=action_frame,
            text="Sell"
            # command=
        ).grid(row=1, column=0)
        ttk.Button(
            master=action_frame,
            text="Pass",
            command=lambda: [Game.next_player(), self.parent.switch_to(target=GameSetup(parent=self.parent))]
        ).grid(row=2, column=0)


        self.chosen_stock=""

        def set_chosen_stock(stock):
            self.chosen_stock = stock

        buy_frame = tk.Frame(
            master=self,
            bg="yellow"
        )
        buy_frame.grid_columnconfigure(0, weight=1)
        buy_frame.grid_columnconfigure(1, weight=1)
        buy_frame.grid_rowconfigure(0, weight=1)
        buy_frame.grid_rowconfigure(1, weight=1)
        buy_frame.grid_rowconfigure(2, weight=1)
        ttk.Button(
            master=buy_frame,
            text="Gold",
            state=Game.set_button_state("Buy", "Gold"),
            command=lambda:[set_chosen_stock("Gold"), buy_num_frame.grid(row=3, column=1, sticky='nsew')]
        ).grid(row=0,column=0)
        ttk.Button(
            master=buy_frame,
            text="Silver",
            state=Game.set_button_state("Buy", "Silver"),
            command=lambda:buy_num_frame.grid(row=3, column=1, sticky='nsew')
        ).grid(row=1,column=0)
        ttk.Button(
            master=buy_frame,
            text="Oil",
            state=Game.set_button_state("Buy", "Oil"),
            command=lambda:buy_num_frame.grid(row=3, column=1, sticky='nsew')
        ).grid(row=2,column=0)
        ttk.Button(
            master=buy_frame,
            text="Bonds",
            state=Game.set_button_state("Buy", "Bonds"),
            command=lambda:buy_num_frame.grid(row=3, column=1, sticky='nsew')
        ).grid(row=0,column=1)
        ttk.Button(
            master=buy_frame,
            text="Grain",
            state=Game.set_button_state("Buy", "Grain"),
            command=lambda:buy_num_frame.grid(row=3, column=1, sticky='nsew')
        ).grid(row=1,column=1)
        ttk.Button(
            master=buy_frame,
            text="Industrial",
            state=Game.set_button_state("Buy", "Industrial"),
            command=lambda:buy_num_frame.grid(row=3, column=1, sticky='nsew')
        ).grid(row=2,column=1)
        ttk.Button(
            master=buy_frame,
            text="Back",
            command=lambda:buy_frame.grid_forget()
        ).grid(row=3, column=0, columnspan=2, sticky="nsew")

        self.buy_amount = tk.IntVar()
        
        def buy_amount(amount):
            set_buy_amount = amount
            return set_buy_amount

        buy_num_frame = tk.Frame(
            master=self,
            bg='brown'
        )
        ttk.Combobox(
            master=buy_num_frame,
            textvariable=self.buy_amount,
            state='readonly',
            values=lambda:[i for i in range(Player.max_buy(self.chosen_stock))]
        ).grid(row=0, column=0, sticky='ew')
        tk.Button(
            master=buy_num_frame,
            text="Ok",
            command=[Player.buy_stock(self.chosen_stock, buy_amount(self.buy_amount.get()))]
        )


        sell_frame = tk.Frame(
            master=self,
            bg="red"
        )

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

    def current_player_name():
        return Player.players[Game.curr_player].name

    def can_buy(stock):
        if Player.players[Game.curr_player].money >= Stock.stock_value[stock]:
            return True
        else:
            return False

    def can_sell(stock):
        if Player.players[Game.curr_player].stocks[stock] > 0:
            return True
        else:
            return False

    def max_buy(stock):
        max_buy = Player.players[Game.curr_player].money // Stock.stock_value[stock]
        return max_buy

    def buy_stock(stock, amount):
        Player.players[Game.curr_player].money -= amount * Stock.stock_value[stock]
        Player.players[Game.curr_player].stocks[stock] += amount

    def sell_stock(self):
        pass

#!Create list to store historical values of each stock for matplotlib in main game
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

    def next_player():
        if Game.curr_player == Game.num_players-1:
            Game.curr_player = 0
        else:
            Game.curr_player += 1

    def set_button_state(action, stock):
        """Set tkinter button state based on if player
        can buy or sell the currently chosen stock
        action: ['Buy', 'Sell']
        stock: ['Gold','Silver','Oil','Bonds','Grain','Industrial']"""
        if action == "Buy":
            if Player.can_buy(stock) == True:
                return tk.NORMAL
            elif Player.can_buy(stock) == False:
                return tk.DISABLED
        elif action == "Sell":
            if Player.can_sell(stock) == True:
                return tk.NORMAL
            elif Player.can_sell(stock) == False:
                return tk.DISABLED

def main():
    return MainWindow().mainloop()


if __name__ == '__main__':
    sys.exit(main())
