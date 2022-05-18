import sys
import tkinter as tk
from tkinter import ttk
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

BGCOLOUR = "gray"

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
        tk.Frame.__init__(self, master=parent, bg=BGCOLOUR)
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        tk.Label(
            master=self,
            text="STOCK TICKER",
            bg=BGCOLOUR,
            font=("Arial", 50)
        ).grid(row=0, column=0, columnspan=2, sticky="new")
        ttk.Button(
            master=self,
            text="New Game",
            command=lambda: [Stock.reset_values(), self.parent.switch_to(target=NewGame(parent=self.parent))]
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


class AboutPage(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg=BGCOLOUR)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        tk.Label(
            master=self,
            text="About Stock Ticker",
            bg=BGCOLOUR,
            font=("Arial", 50)
        ).grid(row=0, column=0, sticky='new')
        tk.Label(
            master=self,
            text="The object of the game is to buy and sell stocks,\n and by so doing accumulate a greater amount of \n money than the other players. The winner is decided\n by setting a time limit at the start of the game, \n and is the person having the greatest amount of money\n when time elapses, after selling his stocks back to \nthe Broker at their final market value.",
            bg=BGCOLOUR,
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
        tk.Frame.__init__(self, master=parent, bg=BGCOLOUR)
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
            bg=BGCOLOUR
        ).grid(row=0, column=1, sticky='new')
        tk.Label(
            master=self,
            text="Please choose the number of players:",
            bg=BGCOLOUR
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
            bg=BGCOLOUR
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
        tk.Frame.__init__(self, master=parent, bg=BGCOLOUR)
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
            tk.Label(master=self, text=f"Player {num + 1}:", bg=BGCOLOUR).grid(row=num + 1, column=1, sticky="w")
            tk.Entry(master=self, textvariable=self.name_list[num]).grid(row=num + 1, column=1, sticky="e")
            ttk.Button(master=self, text="Submit",
                       command=lambda: [set_names(), self.parent.switch_to(target=GameSetup(parent=self.parent))]
                      ).grid(row=9, column=1, sticky="new")

        tk.Label(
            master=self,
            text="Pick your names",
            bg=BGCOLOUR
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


class GameSetup(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg=BGCOLOUR)
        self.parent = parent
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)

        def finish_setup():
            if Game.curr_player == Game.num_players-1:
                Game.next_player()
                self.parent.switch_to(target=MainGame(parent=self.parent))
            else:
                Game.next_player()
                self.parent.switch_to(target=GameSetup(parent=self.parent))

        tk.Label(
            master=self,
            text="Game Setup round",
            bg=BGCOLOUR
        ).grid(row=0, column=0, columnspan=3, sticky='new')
        cur_player = tk.LabelFrame(
            master=self,
            text="Current Player:",
            bg=BGCOLOUR
        )
        cur_player.grid(row=1, column=1, sticky="new")

        tk.Label(
            master=cur_player,
            text=Player.current_player_name(),
            bg=BGCOLOUR
        ).grid(row=1, column=1, sticky='snew')

        #Create number of player frames based on number of players chosen in newgame page
        self.player_grid = []
        for num in range(Game.num_players):
            widget = tk.LabelFrame(
                master=self,
                text=f"{Player.players[num].name}:",
                bg=BGCOLOUR
            )
            self.player_grid.append(widget)

        #display all player frames on page that was just created above
        for num in range(Game.num_players):
            if num == 0:
                self.player_grid[0].grid(row=2, column=0, sticky="nsew")
            if num == 1:
                self.player_grid[1].grid(row=2, column=2, sticky='nsew')
            if num == 2:
                self.player_grid[2].grid(row=3, column=0, sticky='nsew')
            if num == 3:
                self.player_grid[3].grid(row=3, column=2, sticky='nsew')
            if num == 4:
                self.player_grid[4].grid(row=4, column=0, sticky='nsew')
            if num == 5:
                self.player_grid[5].grid(row=4, column=2, sticky='nsew')
            if num == 6:
                self.player_grid[6].grid(row=5, column=0, sticky='nsew')
            if num == 7:
                self.player_grid[7].grid(row=5, column=2, sticky='nsew')
        
        #Create all content to populate player frames
        for num in range(Game.num_players):
            tk.Label(
                master=self.player_grid[num],
                text=f"Money: {Player.players[num].money}",
                bg=BGCOLOUR
            ).grid(row=0, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Gold: {Player.players[num].stocks['Gold']}",
                bg=BGCOLOUR
            ).grid(row=1, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Silver: {Player.players[num].stocks['Silver']}",
                bg=BGCOLOUR
            ).grid(row=2, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Oil: {Player.players[num].stocks['Oil']}",
                bg=BGCOLOUR
            ).grid(row=3, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Bonds: {Player.players[num].stocks['Bonds']}",
                bg=BGCOLOUR
            ).grid(row=1, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Grain: {Player.players[num].stocks['Grain']}",
                bg=BGCOLOUR
            ).grid(row=2, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Industrial: {Player.players[num].stocks['Industrial']}",
                bg=BGCOLOUR
            ).grid(row=3, column=1, sticky='w')

        def set_action_frame():
            action_frame = tk.LabelFrame(
                master=self,
                text="Actions:",
                bg=BGCOLOUR
            )
            action_frame.grid_rowconfigure(0, weight=1)
            action_frame.grid_rowconfigure(1, weight=1)
            action_frame.grid_rowconfigure(2, weight=1)
            action_frame.grid_columnconfigure(0, weight=1)
            action_frame.grid(row=2, rowspan=4, column=1, sticky="nsew")
            buy_state = Game.can_buy_any()
            ttk.Button(
                master=action_frame,
                text="Buy",
                command=lambda: [action_frame.grid_forget(), set_buy_frame()],
                state=buy_state
            ).grid(row=0, column=0)
            sell_state = Game.can_sell_any()
            ttk.Button(
                master=action_frame,
                text="Sell",
                command=lambda: [action_frame.grid_forget(), set_sell_frame()],
                state=sell_state
            ).grid(row=1, column=0)
            ttk.Button(
                master=action_frame,
                text="End Turn",
                command=lambda: [finish_setup()]
            ).grid(row=2, column=0)

        set_action_frame()

        def set_buy_frame():

            buy_frame = tk.LabelFrame(
                master=self,
                text="Buy a stock:",
                bg=BGCOLOUR
            )
            buy_frame.grid_columnconfigure(0, weight=1)
            buy_frame.grid_columnconfigure(1, weight=1)
            buy_frame.grid_rowconfigure(0, weight=1)
            buy_frame.grid_rowconfigure(1, weight=1)
            buy_frame.grid_rowconfigure(2, weight=1)
            buy_frame.grid_rowconfigure(3, weight=1)
            buy_frame.grid(row=2, rowspan=4, column=1, sticky='nsew')
            tk.Label(
                    master=buy_frame,
                    text=f"Which stock do you wish to buy?",
                    bg=BGCOLOUR
            ).grid(row=0, column=0, columnspan=2)
            ttk.Button(
                master=buy_frame,
                text="Gold",
                state=Game.set_button_state("Buy", "Gold"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Gold")]
            ).grid(row=1,column=0)
            ttk.Button(
                master=buy_frame,
                text="Silver",
                state=Game.set_button_state("Buy", "Silver"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Silver")]
            ).grid(row=2,column=0)
            ttk.Button(
                master=buy_frame,
                text="Oil",
                state=Game.set_button_state("Buy", "Oil"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Oil")]
            ).grid(row=3,column=0)
            ttk.Button(
                master=buy_frame,
                text="Bonds",
                state=Game.set_button_state("Buy", "Bonds"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Bonds")]
            ).grid(row=1,column=1)
            ttk.Button(
                master=buy_frame,
                text="Grain",
                state=Game.set_button_state("Buy", "Grain"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Grain")]
            ).grid(row=2,column=1)
            ttk.Button(
                master=buy_frame,
                text="Industrial",
                state=Game.set_button_state("Buy", "Industrial"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Industrial")]
            ).grid(row=3,column=1)
            ttk.Button(
                master=buy_frame,
                text="Back",
                command=lambda:[buy_frame.grid_forget(), set_action_frame()]
            ).grid(row=4, column=0, columnspan=2, sticky="nsew")
            
        def set_buy_num_frame(stock):

            set_buy_amount = tk.IntVar()
            buy_range = [i for i in range(500, Player.max_buy(stock)+1, 500)]

            buy_num_frame = tk.LabelFrame(
                master=self,
                text="Choose amount:",
                bg=BGCOLOUR
            )
            buy_num_frame.grid_rowconfigure(0, weight=1)
            buy_num_frame.grid_rowconfigure(1, weight=1)
            buy_num_frame.grid_rowconfigure(2, weight=1)
            buy_num_frame.grid_rowconfigure(3, weight=1)
            buy_num_frame.grid_columnconfigure(0, weight=1)
            buy_num_frame.grid(row=2, rowspan=4, column=1, sticky='nsew')
            tk.Label(
                master=buy_num_frame,
                text=f"How many shares of {stock} do you wish to buy?",
                bg=BGCOLOUR
            ).grid(row=0, column=0)
            buy_combobox = ttk.Combobox(
                master=buy_num_frame,
                textvariable=set_buy_amount,
                state='readonly',
                values=buy_range
            )
            buy_combobox.grid(row=1, column=0)
            buy_combobox.current(0)
            ttk.Button(
                master=buy_num_frame,
                text="Ok",
                command=lambda:[Player.buy_stock(stock, set_buy_amount.get()), self.parent.switch_to(target=GameSetup(parent=self.parent))]
            ).grid(row=2, column=0)
            ttk.Button(
                master=buy_num_frame,
                text="Back",
                command=lambda:[buy_num_frame.grid_forget(), set_buy_frame()]
            ).grid(row=3, column=0)

        def set_sell_frame():

            sell_frame = tk.LabelFrame(
                master=self,
                text="Sell a stock:",
                bg=BGCOLOUR
            )
            sell_frame.grid_columnconfigure(0, weight=1)
            sell_frame.grid_columnconfigure(1, weight=1)
            sell_frame.grid_rowconfigure(0, weight=1)
            sell_frame.grid_rowconfigure(1, weight=1)
            sell_frame.grid_rowconfigure(2, weight=1)
            sell_frame.grid_rowconfigure(3, weight=1)
            sell_frame.grid(row=2, rowspan=4, column=1, sticky='nsew')
            tk.Label(
                    master=sell_frame,
                    text=f"Which stock do you wish to sell?",
                    bg=BGCOLOUR
                ).grid(row=0, column=0, columnspan=2)
            ttk.Button(
                master=sell_frame,
                text="Gold",
                state=Game.set_button_state("Sell", "Gold"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Gold")]
            ).grid(row=1,column=0)
            ttk.Button(
                master=sell_frame,
                text="Silver",
                state=Game.set_button_state("Sell", "Silver"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Silver")]
            ).grid(row=2,column=0)
            ttk.Button(
                master=sell_frame,
                text="Oil",
                state=Game.set_button_state("Sell", "Oil"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Oil")]
            ).grid(row=3,column=0)
            ttk.Button(
                master=sell_frame,
                text="Bonds",
                state=Game.set_button_state("Sell", "Bonds"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Bonds")]
            ).grid(row=1,column=1)
            ttk.Button(
                master=sell_frame,
                text="Grain",
                state=Game.set_button_state("Sell", "Grain"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Grain")]
            ).grid(row=2,column=1)
            ttk.Button(
                master=sell_frame,
                text="Industrial",
                state=Game.set_button_state("Sell", "Industrial"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Industrial")]
            ).grid(row=3,column=1)
            ttk.Button(
                master=sell_frame,
                text="Back",
                command=lambda:[sell_frame.grid_forget(), set_action_frame()]
            ).grid(row=4, column=0, columnspan=2, sticky="nsew")
            
        def set_sell_num_frame(stock):

            set_sell_amount = tk.IntVar()
            sell_range = [i for i in range(500, Player.max_sell(stock)+1, 500)]

            sell_num_frame = tk.LabelFrame(
                master=self,
                text="Choose amount:",
                bg=BGCOLOUR
            )
            sell_num_frame.grid_rowconfigure(0, weight=1)
            sell_num_frame.grid_rowconfigure(1, weight=1)
            sell_num_frame.grid_rowconfigure(2, weight=1)
            sell_num_frame.grid_rowconfigure(3, weight=1)
            sell_num_frame.grid_columnconfigure(0, weight=1)
            sell_num_frame.grid(row=2, rowspan=4, column=1, sticky='nsew')
            tk.Label(
                master=sell_num_frame,
                text=f"How many shares of {stock} do you wish to sell?",
                bg=BGCOLOUR
            ).grid(row=0, column=0)
            sell_combobox = ttk.Combobox(
                master=sell_num_frame,
                textvariable=set_sell_amount,
                state='readonly',
                values=sell_range
            )
            sell_combobox.grid(row=1, column=0)
            sell_combobox.current(0)
            ttk.Button(
                master=sell_num_frame,
                text="Ok",
                command=lambda:[Player.sell_stock(stock, set_sell_amount.get()), self.parent.switch_to(target=GameSetup(parent=self.parent))]
            ).grid(row=2, column=0)
            ttk.Button(
                master=sell_num_frame,
                text="Back",
                command=lambda:[sell_num_frame.grid_forget(), set_sell_frame()]
            ).grid(row=3, column=0)
            
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


class MainGame(tk.Frame):

    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg=BGCOLOUR)
        self.parent = parent
        # self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)

        def finish_game():
            if Game.curr_round > Game.max_rounds:
                Game.curr_player = 0
                self.parent.switch_to(target=EndGame(parent=self.parent))
            else:
                self.parent.switch_to(target=MainGame(parent=self.parent))

        tk.Label(
            master=self,
            text="Stock Ticker",
            bg=BGCOLOUR
        ).grid(row=0, column=0, columnspan=3, sticky='new')
        cur_player = tk.LabelFrame(
            master=self,
            text="Current Player:",
            bg=BGCOLOUR
        )
        cur_player.grid(row=1, column=0, sticky="new")

        tk.Label(
            master=cur_player,
            text=Player.current_player_name(),
            bg=BGCOLOUR
        ).grid(row=0, column=0, sticky="snew")

        #dice roll frame
        dice_roll_frame = tk.LabelFrame(
                master=self,
                text="Dice Roll:",
                bg=BGCOLOUR
            )
        dice_roll_frame.grid(row=1, column=1, sticky="snew")

        if Game.turn == 0:
            stock, action, amount = Dice.roll()
            tk.Label(
                master=dice_roll_frame,
                text=f"{stock} {action} {amount}",
                bg=BGCOLOUR
            ).grid(row=0, column=0, sticky="snew")       

        #round frame
        round_frame = tk.LabelFrame(
                master=self,
                text="Round:",
                bg=BGCOLOUR
            )
        round_frame.grid(row=1, column=2, sticky="snew")
        tk.Label(
            master=round_frame,
            text=f"{Game.curr_round} / {Game.max_rounds}",
            bg=BGCOLOUR
        ).grid(row=0, column=0, sticky="snew")

        #Stock Graph Frame
        stock_graph_frame = tk.LabelFrame(
                master=self,
                text="Stock Prices:",
                bg=BGCOLOUR
            )
        stock_graph_frame.grid(row=2, column=1, rowspan=3, sticky="snew")

        def graph():
            stocks = list(Stock.stock_value.keys())
            values = list(Stock.stock_value.values())

            # create a figure
            figure = Figure()

            # create FigureCanvasTkAgg object
            figure_canvas = FigureCanvasTkAgg(figure, stock_graph_frame)

            # create axes
            axes = figure.add_subplot()
            
            # create the barchart
            graph = axes.bar(stocks, values, color=['gold', 'silver', 'black', 'lightseagreen', 'navajowhite', 'lightpink'], edgecolor="black")
            axes.bar_label(graph, label_type="edge")

            axes.set_ylabel('Current Value')
            # axes.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

            figure_canvas.get_tk_widget().pack(fill="both", expand=1)

        graph()

        #Create number of player frames based on number of players chosen in newgame page
        self.player_grid = []
        for num in range(Game.num_players):
            widget = tk.LabelFrame(
                master=self,
                text=f"{Player.players[num].name}:",
                bg=BGCOLOUR
            )
            self.player_grid.append(widget)

        #display all player frames on page that was just created above
        for num in range(Game.num_players):
            if num == 0:
                self.player_grid[0].grid(row=2, column=0, sticky="nsew")
            if num == 1:
                self.player_grid[1].grid(row=2, column=2, sticky='nsew')
            if num == 2:
                self.player_grid[2].grid(row=3, column=0, sticky='nsew')
            if num == 3:
                self.player_grid[3].grid(row=3, column=2, sticky='nsew')
            if num == 4:
                self.player_grid[4].grid(row=4, column=0, sticky='nsew')
            if num == 5:
                self.player_grid[5].grid(row=4, column=2, sticky='nsew')
            if num == 6:
                self.player_grid[6].grid(row=5, column=0, sticky='nsew')
            if num == 7:
                self.player_grid[7].grid(row=5, column=2, sticky='nsew')
        
        #Create all content to populate player frames
        for num in range(Game.num_players):
            tk.Label(
                master=self.player_grid[num],
                text=f"Money: {int(Player.players[num].money)}",
                bg=BGCOLOUR
            ).grid(row=0, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Gold: {Player.players[num].stocks['Gold']}",
                bg=BGCOLOUR
            ).grid(row=1, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Silver: {Player.players[num].stocks['Silver']}",
                bg=BGCOLOUR
            ).grid(row=2, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Oil: {Player.players[num].stocks['Oil']}",
                bg=BGCOLOUR
            ).grid(row=3, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Bonds: {Player.players[num].stocks['Bonds']}",
                bg=BGCOLOUR
            ).grid(row=1, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Grain: {Player.players[num].stocks['Grain']}",
                bg=BGCOLOUR
            ).grid(row=2, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Industrial: {Player.players[num].stocks['Industrial']}",
                bg=BGCOLOUR
            ).grid(row=3, column=1, sticky='w')

        def set_action_frame():
            action_frame = tk.LabelFrame(
                master=self,
                text="Actions:",
                bg=BGCOLOUR
            )
            action_frame.grid_rowconfigure(0, weight=1)
            action_frame.grid_rowconfigure(1, weight=1)
            action_frame.grid_rowconfigure(2, weight=1)
            action_frame.grid_columnconfigure(0, weight=1)
            action_frame.grid(row=5, column=1, sticky="nsew")
            buy_state = Game.can_buy_any()
            ttk.Button(
                master=action_frame,
                text="Buy",
                command=lambda: [action_frame.grid_forget(), set_buy_frame()],
                state=buy_state
            ).grid(row=0, column=0)
            sell_state = Game.can_sell_any()
            ttk.Button(
                master=action_frame,
                text="Sell",
                command=lambda: [action_frame.grid_forget(), set_sell_frame()],
                state=sell_state                
            ).grid(row=1, column=0)
            ttk.Button(
                master=action_frame,
                text="End Turn",
                command=lambda: [Game.next_player(), finish_game()]
            ).grid(row=2, column=0)

        set_action_frame()

        def set_buy_frame():

            buy_frame = tk.LabelFrame(
                master=self,
                text="Buy a stock:",
                bg=BGCOLOUR
            )
            buy_frame.grid_columnconfigure(0, weight=1)
            buy_frame.grid_columnconfigure(1, weight=1)
            buy_frame.grid_rowconfigure(0, weight=1)
            buy_frame.grid_rowconfigure(1, weight=1)
            buy_frame.grid_rowconfigure(2, weight=1)
            buy_frame.grid_rowconfigure(3, weight=1)
            buy_frame.grid(row=5, column=1, sticky='nsew')
            tk.Label(
                    master=buy_frame,
                    text=f"Which stock do you wish to buy?",
                    bg=BGCOLOUR
                ).grid(row=0, column=0, columnspan=2)
            ttk.Button(
                master=buy_frame,
                text="Gold",
                state=Game.set_button_state("Buy", "Gold"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Gold")]
            ).grid(row=1,column=0)
            ttk.Button(
                master=buy_frame,
                text="Silver",
                state=Game.set_button_state("Buy", "Silver"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Silver")]
            ).grid(row=2,column=0)
            ttk.Button(
                master=buy_frame,
                text="Oil",
                state=Game.set_button_state("Buy", "Oil"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Oil")]
            ).grid(row=3,column=0)
            ttk.Button(
                master=buy_frame,
                text="Bonds",
                state=Game.set_button_state("Buy", "Bonds"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Bonds")]
            ).grid(row=1,column=1)
            ttk.Button(
                master=buy_frame,
                text="Grain",
                state=Game.set_button_state("Buy", "Grain"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Grain")]
            ).grid(row=2,column=1)
            ttk.Button(
                master=buy_frame,
                text="Industrial",
                state=Game.set_button_state("Buy", "Industrial"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Industrial")]
            ).grid(row=3,column=1)
            ttk.Button(
                master=buy_frame,
                text="Back",
                command=lambda:[buy_frame.grid_forget(), set_action_frame()]
            ).grid(row=4, column=0, columnspan=2, sticky="nsew")
            
        def set_buy_num_frame(stock):

            set_buy_amount = tk.IntVar()
            buy_range = [i for i in range(500, Player.max_buy(stock)+1, 500)]

            buy_num_frame = tk.LabelFrame(
                master=self,
                text="Choose amount:",
                bg=BGCOLOUR
            )
            buy_num_frame.grid_rowconfigure(0, weight=1)
            buy_num_frame.grid_rowconfigure(1, weight=1)
            buy_num_frame.grid_rowconfigure(2, weight=1)
            buy_num_frame.grid_rowconfigure(3, weight=1)
            buy_num_frame.grid_columnconfigure(0, weight=1)
            buy_num_frame.grid(row=5, column=1, sticky='nsew')
            tk.Label(
                master=buy_num_frame,
                text=f"How much {stock} do you wish to buy?",
                bg=BGCOLOUR
            ).grid(row=0, column=0)
            buy_combobox = ttk.Combobox(
                master=buy_num_frame,
                textvariable=set_buy_amount,
                state='readonly',
                values=buy_range
            )
            buy_combobox.grid(row=1, column=0)
            buy_combobox.current(0)
            ttk.Button(
                master=buy_num_frame,
                text="Ok",
                command=lambda:[Game.set_turn(), Player.buy_stock(stock, set_buy_amount.get()), self.parent.switch_to(target=MainGame(parent=self.parent))]
            ).grid(row=2, column=0)
            ttk.Button(
                master=buy_num_frame,
                text="Back",
                command=lambda:[buy_num_frame.grid_forget(), set_buy_frame()]
            ).grid(row=3, column=0)

        def set_sell_frame():

            sell_frame = tk.LabelFrame(
                master=self,
                text="Sell a stock:",
                bg=BGCOLOUR
            )
            sell_frame.grid_columnconfigure(0, weight=1)
            sell_frame.grid_columnconfigure(1, weight=1)
            sell_frame.grid_rowconfigure(0, weight=1)
            sell_frame.grid_rowconfigure(1, weight=1)
            sell_frame.grid_rowconfigure(2, weight=1)
            sell_frame.grid_rowconfigure(3, weight=1)
            sell_frame.grid(row=5, column=1, sticky='nsew')
            tk.Label(
                    master=sell_frame,
                    text=f"Which stock do you wish to sell?",
                    bg=BGCOLOUR
                ).grid(row=0, column=0, columnspan=2)
            ttk.Button(
                master=sell_frame,
                text="Gold",
                state=Game.set_button_state("Sell", "Gold"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Gold")]
            ).grid(row=1,column=0)
            ttk.Button(
                master=sell_frame,
                text="Silver",
                state=Game.set_button_state("Sell", "Silver"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Silver")]
            ).grid(row=2,column=0)
            ttk.Button(
                master=sell_frame,
                text="Oil",
                state=Game.set_button_state("Sell", "Oil"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Oil")]
            ).grid(row=3,column=0)
            ttk.Button(
                master=sell_frame,
                text="Bonds",
                state=Game.set_button_state("Sell", "Bonds"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Bonds")]
            ).grid(row=1,column=1)
            ttk.Button(
                master=sell_frame,
                text="Grain",
                state=Game.set_button_state("Sell", "Grain"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Grain")]
            ).grid(row=2,column=1)
            ttk.Button(
                master=sell_frame,
                text="Industrial",
                state=Game.set_button_state("Sell", "Industrial"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Industrial")]
            ).grid(row=3,column=1)
            ttk.Button(
                master=sell_frame,
                text="Back",
                command=lambda:[sell_frame.grid_forget(), set_action_frame()]
            ).grid(row=4, column=0, columnspan=2, sticky="nsew")
            
        def set_sell_num_frame(stock):

            set_sell_amount = tk.IntVar()
            sell_range = [i for i in range(500, Player.max_sell(stock)+1, 500)]

            sell_num_frame = tk.LabelFrame(
                master=self,
                text="Choose amount:",
                bg=BGCOLOUR
            )
            sell_num_frame.grid_rowconfigure(0, weight=1)
            sell_num_frame.grid_rowconfigure(1, weight=1)
            sell_num_frame.grid_rowconfigure(2, weight=1)
            sell_num_frame.grid_rowconfigure(3, weight=1)
            sell_num_frame.grid_columnconfigure(0, weight=1)
            sell_num_frame.grid(row=5, column=1, sticky='nsew')
            tk.Label(
                master=sell_num_frame,
                text=f"How much {stock} do you wish to sell?",
                bg=BGCOLOUR
            ).grid(row=0, column=0)
            sell_combobox = ttk.Combobox(
                master=sell_num_frame,
                textvariable=set_sell_amount,
                state='readonly',
                values=sell_range
            )
            sell_combobox.grid(row=1, column=0)
            sell_combobox.current(0)
            ttk.Button(
                master=sell_num_frame,
                text="Ok",
                command=lambda:[Game.set_turn(), Player.sell_stock(stock, set_sell_amount.get()), self.parent.switch_to(target=MainGame(parent=self.parent))]
            ).grid(row=2, column=0)
            ttk.Button(
                master=sell_num_frame,
                text="Back",
                command=lambda:[sell_num_frame.grid_forget(),set_sell_frame()]
            ).grid(row=3, column=0)
            
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


class EndGame(tk.Frame):
    def __init__(self, parent: MainWindow):
        tk.Frame.__init__(self, master=parent, bg=BGCOLOUR)
        self.parent = parent
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        # self.grid_rowconfigure(6, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        def final_results():
            #!Rank all players from first to last based on total money.
            #!In Label at top of results_frame, have {Name} won! in big text
            pass

        def end_loop():
            stock_keys = list(Player.players[Game.curr_player].stocks.keys())
            if Game.curr_player <= Game.num_players:
                #sell off shares, show value of each stock
                for index, name in enumerate(stock_keys):
                    quantity = Player.max_sell(name) 
                    Player.sell_stock(name, quantity)
                    tk.Label(
                        master=results_frame,
                        text=f"Value of {name} shares: {int(Stock.get_value(name, quantity))}",
                        bg=BGCOLOUR
                    ).grid(row=index, column=1, sticky="snew")
                #display curr_players money in tk.Label
                tk.Label(
                    master=results_frame,
                    text=f"{Player.current_player_name()} has ${Player.players[Game.curr_player].money}",
                    bg=BGCOLOUR
                ).grid(row=6, column=1, sticky='ew')

                if Game.curr_player < Game.num_players-1:
                    ttk.Button(
                        master=results_frame,
                        text="Next player",
                        command=lambda: [Player.next_player(), self.parent.switch_to(target=EndGame(parent=self.parent))]
                    ).grid(row=7, column=1, sticky='sew')
                elif Game.curr_player == Game.num_players-1:
                    ttk.Button(
                        master=results_frame,
                        text="See final results",
                        command=lambda:[final_results()]
                    ).grid(row=7, column=1, sticky="sew")

                

        tk.Label(
            master=self,
            text="End Game",
            bg=BGCOLOUR
        ).grid(row=0, column=0, columnspan=3, sticky='new')

        cur_player = tk.LabelFrame(
            master=self,
            text="Current Player:",
            bg=BGCOLOUR
        )
        cur_player.grid(row=1, column=1, sticky="new")

        tk.Label(
            master=cur_player,
            text=Player.current_player_name(),
            bg=BGCOLOUR
        ).grid(row=1, column=1, sticky='snew')

        #Create number of player frames based on number of players chosen in newgame page
        self.player_grid = []
        for num in range(Game.num_players):
            widget = tk.LabelFrame(
                master=self,
                text=f"{Player.players[num].name}:",
                bg=BGCOLOUR
            )
            self.player_grid.append(widget)

        #display all player frames on page that was just created above
        for num in range(Game.num_players):
            if num == 0:
                self.player_grid[0].grid(row=2, column=0, sticky="nsew")
            if num == 1:
                self.player_grid[1].grid(row=2, column=2, sticky='nsew')
            if num == 2:
                self.player_grid[2].grid(row=3, column=0, sticky='nsew')
            if num == 3:
                self.player_grid[3].grid(row=3, column=2, sticky='nsew')
            if num == 4:
                self.player_grid[4].grid(row=4, column=0, sticky='nsew')
            if num == 5:
                self.player_grid[5].grid(row=4, column=2, sticky='nsew')
            if num == 6:
                self.player_grid[6].grid(row=5, column=0, sticky='nsew')
            if num == 7:
                self.player_grid[7].grid(row=5, column=2, sticky='nsew')
        
        #Create all content to populate player frames
        for num in range(Game.num_players):
            tk.Label(
                master=self.player_grid[num],
                text=f"Money: {Player.players[num].money}",
                bg=BGCOLOUR
            ).grid(row=0, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Gold: {Player.players[num].stocks['Gold']}",
                bg=BGCOLOUR
            ).grid(row=1, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Silver: {Player.players[num].stocks['Silver']}",
                bg=BGCOLOUR
            ).grid(row=2, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Oil: {Player.players[num].stocks['Oil']}",
                bg=BGCOLOUR
            ).grid(row=3, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Bonds: {Player.players[num].stocks['Bonds']}",
                bg=BGCOLOUR
            ).grid(row=1, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Grain: {Player.players[num].stocks['Grain']}",
                bg=BGCOLOUR
            ).grid(row=2, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Industrial: {Player.players[num].stocks['Industrial']}",
                bg=BGCOLOUR
            ).grid(row=3, column=1, sticky='w')

        results_frame = tk.LabelFrame(
            master=self,
            text="Actions:",
            bg=BGCOLOUR
        )
        # results_frame.grid_rowconfigure(0, weight=1)
        # results_frame.grid_rowconfigure(1, weight=1)
        # results_frame.grid_rowconfigure(2, weight=1)
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_columnconfigure(1, weight=1)
        results_frame.grid_columnconfigure(2, weight=1)
        results_frame.grid(row=2, rowspan=4, column=1, sticky="nsew")

        end_loop()

        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu(parent=self.parent))
        ).grid(row=5, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=6, column=0, columnspan=3, sticky="sew")

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

    def next_player():
        Game.curr_player += 1

    def can_buy(stock):
        if Player.players[Game.curr_player].money >= Stock.stock_value[stock] * 500:
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
        return int(max_buy)

    def max_sell(stock):
        max_sell = Player.players[Game.curr_player].stocks[stock]
        return max_sell

    def buy_stock(stock, amount):
        Player.players[Game.curr_player].money -= amount * Stock.stock_value[stock]
        Player.players[Game.curr_player].stocks[stock] += amount

    def sell_stock(stock, amount):
        Player.players[Game.curr_player].money += amount * Stock.stock_value[stock]
        Player.players[Game.curr_player].stocks[stock] -= amount


class Stock:

    stock_value = {
        "Gold": 1,
        "Silver": 1,
        "Oil": 1,
        "Bonds": 1,
        "Grain": 1,
        "Industrial": 1
    }

    def increase_value(stock, amount):
        Stock.stock_value[stock] += (amount / 100)
        if Stock.stock_value[stock] > 1.95:
            Stock.double_stock(stock)

    def decrease_value(stock, amount):
        Stock.stock_value[stock] -= (amount / 100)
        if Stock.stock_value[stock] < .05:
            Stock.split_stock(stock)

    def dividend(stock, amount):
        dividend = (amount / 100)
        if Stock.stock_value[stock] >= 1:
            for i, v in enumerate(Player.players):
                bonus = Player.players[i].stocks[stock] * dividend
                Player.players[i].money += int(bonus)

    def double_stock(stock):
        Stock.stock_value[stock] = 1
        for i, v in enumerate(Player.players):
            Player.players[i].stocks[stock] = Player.players[i].stocks[stock] * 2

    def split_stock(stock):
        Stock.stock_value[stock] = 1
        for i, v in enumerate(Player.players):
            Player.players[i].stocks[stock] = 0

    def get_value(stock, amount):
        value = amount * Stock.stock_value[stock]
        return value

    def reset_values():
        Stock.stock_value = {
            "Gold": 1,
            "Silver": 1,
            "Oil": 1,
            "Bonds": 1,
            "Grain": 1,
            "Industrial": 1
        }

        Game.num_players = 0
        Game.curr_player = 0
        Game.max_rounds = 0
        Game.curr_round = 0
        Game.turn = 0

        Player.players = []


class Dice:
    stock = ["Gold", "Silver", "Oil", "Bonds", "Grain", "Industrial"]
    action = ["Up", "Down", "Dividend"]
    amount = [5, 10, 20]

    def roll():
        stock = random.choice(Dice.stock)
        action = random.choice(Dice.action)
        amount = random.choice(Dice.amount)

        if action == Dice.action[0]:
            Stock.increase_value(stock, amount)
            return stock, action, amount
        elif action == Dice.action[1]:
            Stock.decrease_value(stock, amount)
            return stock, action, amount
        else:
            Stock.dividend(stock, amount)
            return stock, action, amount


class Game:
    num_players = 0
    curr_player = 0
    max_rounds = 0
    curr_round = 0
    # move_counter = 0
    turn = 0

    def set_players(players):
        Game.num_players = players

    def set_rounds(rounds):
        Game.max_rounds = rounds

    def next_round():
        Game.curr_round += 1

    def set_turn():
        Game.turn += 1

    def next_player():
        """Changes active player"""
        #If current player is the last player, loop to first player:
        if Game.curr_player == Game.num_players-1:
            Game.next_round()
            Game.curr_player = 0
        #move to next player
        else:
            Game.curr_player += 1
        Game.turn = 0

    # def move_counter():
    #     """Used in MainGame. If == 0, Dice.roll is called.
    #     This enables a player to make multiple buy/sell actions
    #     within a single turn without rerolling the dice each time."""
    #     Game.move_counter += 1

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

    def can_buy_any():
        current_prices = []
        stock_name = list(Stock.stock_value)
        for stock in range(len(Stock.stock_value)):
            stock_price = Stock.stock_value[stock_name[stock]]
            current_prices.append(stock_price)
        if Player.players[Game.curr_player].money < (min(current_prices) * 500):
            return tk.DISABLED
        else:
            return tk.NORMAL

    def can_sell_any():
        """Sets state of action_frame 'Sell' buttons"""
        current_shares = []
        stock_name = list(Player.players[Game.curr_player].stocks)
        for value in range(len(Player.players[Game.curr_player].stocks)):
            stock_price = Player.players[Game.curr_player].stocks[stock_name[value]]
            current_shares.append(stock_price)
        if max(current_shares) == 0:
            return tk.DISABLED
        else:
            return tk.NORMAL


def main():
    return MainWindow().mainloop()


if __name__ == '__main__':
    sys.exit(main())
