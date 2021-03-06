import tkinter as tk
from tkinter import ttk
import main
import MainMenu
import Game
import EndGame
import Player
import Dice
import Stock
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainGame(tk.Frame):
    def __init__(self, parent: main.MainWindow):
        tk.Frame.__init__(self, master=parent, bg=main.BGCOLOUR)
        self.parent = parent
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.stocks = list(Stock.Stock.stock_value.keys())
        self.values = list(Stock.Stock.stock_value.values())

        #Stock Graph Frame
        stock_graph_frame = tk.LabelFrame(
            master=self,
            text="Stock Prices:",
            bg=main.BGCOLOUR
        )
        stock_graph_frame.grid(row=2, column=1, rowspan=3, sticky="snew")
        
        # create a figure
        figure = plt.figure(facecolor=main.BGCOLOUR)

        # create FigureCanvasTkAgg object
        canvas = FigureCanvasTkAgg(figure, stock_graph_frame)
        canvas = canvas.get_tk_widget()
        canvas.pack(fill="both", expand=1)

        # create axes
        axes = figure.add_subplot()
        
        # create the barchart
        graph = axes.bar(self.stocks, self.values, color=['gold', 'silver', 'burlywood', 'lightseagreen', 'navajowhite', 'lightpink'], edgecolor="black")
        axes.bar_label(graph, label_type="edge")
        axes.set_facecolor(main.BGCOLOUR)
        axes.set_ylabel('Current Value')
        axes.axhline(y=1,linewidth=1, color='red')
        plt.yticks([0, 0.5, 1, 1.5, 2], [0, 0.5, 1, 1.5, 2])

        def clear_frames(frame):
            for widgets in frame.winfo_children():
                widgets.destroy()

        def set_notification_frame(stock, amount):
            #if no players hold current stock, don't call
            notification_frame = tk.LabelFrame(
                    master=self,
                    text="Dividend Payouts:",
                    bg=main.BGCOLOUR
                )
            notification_frame.grid(row=2, column=1, rowspan=4, sticky="snew")
            notification_frame.grid_rowconfigure(9, weight=1)
            notification_frame.grid_columnconfigure(0, weight=1)
            notification_frame.grid_columnconfigure(1, weight=1)
            notification_frame.grid_columnconfigure(2, weight=1)
            Stock.Stock.dividend(stock, amount, notification_frame)
            ttk.Button(
                master=notification_frame,
                text="Ok",
                command=lambda: [notification_frame.grid_forget(), set_action_frame()]
            ).grid(row=9, column=1, sticky="sew")

        def end_turn():
            #Move to next player
            Game.Game.next_player()

            #round
            clear_frames(round_frame)
            set_round_frame()

            #action
            clear_frames(action_frame)
            set_action_frame()

            #dice_role
            clear_frames(dice_roll_frame)
            set_dice_frame()

            #player_grid
            clear_frames(left_stats_frame)
            clear_frames(right_stats_frame)
            Game.Game.set_player_frames(self, left_stats_frame, right_stats_frame)

            #curr_player
            clear_frames(curr_player_frame)
            set_curr_player_frame()

            #stock_graph
            create_bar()

            finish_game()

        def finish_game():
            if Game.Game.curr_round > Game.Game.max_rounds:
                Game.Game.curr_player = 0
                self.parent.switch_to(target=EndGame.EndGame(parent=self.parent))

        #Page Title
        tk.Label(
            master=self,
            text="Stock Ticker",
            bg=main.BGCOLOUR
        ).grid(row=0, column=0, columnspan=3, sticky='new')

        curr_player_frame = tk.LabelFrame(
            master=self,
            text="Current Player:",
            bg=main.BGCOLOUR
        )
        curr_player_frame.grid(row=1, column=0, sticky="new")

        round_frame = tk.LabelFrame(
            master=self,
            text="Round:",
            bg=main.BGCOLOUR
            )
        round_frame.grid(row=1, column=2, sticky="snew")

        dice_roll_frame = tk.LabelFrame(
            master=self,
            text="Dice Roll:",
            bg=main.BGCOLOUR
            )
        dice_roll_frame.grid(row=1, column=1, sticky="snew")

        left_stats_frame = tk.Frame(
            master=self,
            bg=main.BGCOLOUR
        )
        left_stats_frame.grid(row=2, column=0, rowspan=4, sticky='snew')

        right_stats_frame = tk.Frame(
            master=self,
            bg=main.BGCOLOUR
        )
        right_stats_frame.grid(row=2, column=2, rowspan=4, sticky='snew')

        action_frame = tk.LabelFrame(
            master=self,
            text="Actions:",
            bg=main.BGCOLOUR
        )
        action_frame.grid_rowconfigure(0, weight=1)
        action_frame.grid_rowconfigure(1, weight=1)
        action_frame.grid_rowconfigure(2, weight=1)
        action_frame.grid_columnconfigure(0, weight=1)
        action_frame.grid(row=5, column=1, sticky="nsew")

        buy_frame = tk.LabelFrame(
            master=self,
            text="Buy a stock:",
            bg=main.BGCOLOUR
        )
        buy_frame.grid_columnconfigure(0, weight=1)
        buy_frame.grid_columnconfigure(1, weight=1)
        buy_frame.grid_rowconfigure(0, weight=1)
        buy_frame.grid_rowconfigure(1, weight=1)
        buy_frame.grid_rowconfigure(2, weight=1)
        buy_frame.grid_rowconfigure(3, weight=1)

        buy_num_frame = tk.LabelFrame(
            master=self,
            text="Choose amount:",
            bg=main.BGCOLOUR
        )
        buy_num_frame.grid_rowconfigure(0, weight=1)
        buy_num_frame.grid_rowconfigure(1, weight=1)
        buy_num_frame.grid_rowconfigure(2, weight=1)
        buy_num_frame.grid_rowconfigure(3, weight=1)
        buy_num_frame.grid_columnconfigure(0, weight=1)

        sell_frame = tk.LabelFrame(
            master=self,
            text="Sell a stock:",
            bg=main.BGCOLOUR
        )
        sell_frame.grid_columnconfigure(0, weight=1)
        sell_frame.grid_columnconfigure(1, weight=1)
        sell_frame.grid_rowconfigure(0, weight=1)
        sell_frame.grid_rowconfigure(1, weight=1)
        sell_frame.grid_rowconfigure(2, weight=1)
        sell_frame.grid_rowconfigure(3, weight=1)

        sell_num_frame = tk.LabelFrame(
            master=self,
            text="Choose amount:",
            bg=main.BGCOLOUR
        )
        sell_num_frame.grid_rowconfigure(0, weight=1)
        sell_num_frame.grid_rowconfigure(1, weight=1)
        sell_num_frame.grid_rowconfigure(2, weight=1)
        sell_num_frame.grid_rowconfigure(3, weight=1)
        sell_num_frame.grid_columnconfigure(0, weight=1)
        
        def set_curr_player_frame():
            tk.Label(
                master=curr_player_frame,
                text=Player.Player.current_player_name(),
                bg=main.BGCOLOUR
            ).grid(sticky="snew")

        def set_dice_frame():
            if Game.Game.turn == 0:
                stock, action, amount = Dice.Dice.roll()
                tk.Label(
                    master=dice_roll_frame,
                    text=f"{stock} {action} {amount}",
                    bg=main.BGCOLOUR
                ).grid(row=0, column=0, sticky="snew")
                if action == "Dividend":
                    if Player.Player.any_holding(stock):
                        set_notification_frame(stock, amount)

        def set_round_frame():
            tk.Label(
                master=round_frame,
                text=f"{Game.Game.curr_round} / {Game.Game.max_rounds}",
                bg=main.BGCOLOUR
            ).grid(sticky="snew")

        def create_bar():
            for child in axes.get_children():
                if isinstance(child, matplotlib.text.Annotation):
                    child.remove()
            stocks = list(Stock.Stock.stock_value.keys())
            values = list(Stock.Stock.stock_value.values())
            graph[0].set_height(values[0])
            graph[1].set_height(values[1])
            graph[2].set_height(values[2])
            graph[3].set_height(values[3])
            graph[4].set_height(values[4])
            graph[5].set_height(values[5])
            axes.bar_label(graph, label_type="edge")
            figure.canvas.draw()

        def set_action_frame():
            action_frame.grid(row=5, column=1, sticky="nsew")
            buy_state = Game.Game.can_buy_any()
            ttk.Button(
                master=action_frame,
                text="Buy",
                command=lambda: [action_frame.grid_forget(), set_buy_frame()],
                state=buy_state
            ).grid(row=0, column=0)
            sell_state = Game.Game.can_sell_any()
            ttk.Button(
                master=action_frame,
                text="Sell",
                command=lambda: [action_frame.grid_forget(), set_sell_frame()],
                state=sell_state                
            ).grid(row=1, column=0)
            ttk.Button(
                master=action_frame,
                text="End Turn",
                command=end_turn
            ).grid(row=2, column=0)

        set_round_frame()

        set_action_frame()

        set_dice_frame()

        Game.Game.set_player_frames(self, left_stats_frame, right_stats_frame)

        set_curr_player_frame()

        create_bar()

        def set_buy_frame():
            buy_frame.grid(row=5, column=1, sticky='nsew')
            tk.Label(
                    master=buy_frame,
                    text=f"Which stock do you wish to buy?",
                    bg=main.BGCOLOUR
                ).grid(row=0, column=0, columnspan=2)
            ttk.Button(
                master=buy_frame,
                text="Gold",
                state=Game.Game.set_button_state("Buy", "Gold"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Gold")]
            ).grid(row=1,column=0)
            ttk.Button(
                master=buy_frame,
                text="Silver",
                state=Game.Game.set_button_state("Buy", "Silver"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Silver")]
            ).grid(row=2,column=0)
            ttk.Button(
                master=buy_frame,
                text="Oil",
                state=Game.Game.set_button_state("Buy", "Oil"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Oil")]
            ).grid(row=3,column=0)
            ttk.Button(
                master=buy_frame,
                text="Bonds",
                state=Game.Game.set_button_state("Buy", "Bonds"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Bonds")]
            ).grid(row=1,column=1)
            ttk.Button(
                master=buy_frame,
                text="Grain",
                state=Game.Game.set_button_state("Buy", "Grain"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Grain")]
            ).grid(row=2,column=1)
            ttk.Button(
                master=buy_frame,
                text="Industrial",
                state=Game.Game.set_button_state("Buy", "Industrial"),
                command=lambda:[buy_frame.grid_forget(), set_buy_num_frame("Industrial")]
            ).grid(row=3,column=1)
            ttk.Button(
                master=buy_frame,
                text="Back",
                command=lambda:[buy_frame.grid_forget(), set_action_frame()]
            ).grid(row=4, column=0, columnspan=2, sticky="nsew")
            
        def set_buy_num_frame(stock):
            buy_num_frame.grid(row=5, column=1, sticky='nsew')
            set_buy_amount = tk.IntVar()
            buy_range = [i for i in range(500, Player.Player.max_buy(stock)+1, 500)]

            tk.Label(
                master=buy_num_frame,
                text=f"How many shares of {stock} do you wish to buy?",
                bg=main.BGCOLOUR
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
                command=lambda:[Game.Game.set_turn(), Player.Player.buy_stock(stock, set_buy_amount.get()), clear_frames(left_stats_frame), clear_frames(right_stats_frame), Game.Game.set_player_frames(self, left_stats_frame, right_stats_frame), set_action_state("Buy")]
            ).grid(row=2, column=0)
            ttk.Button(
                master=buy_num_frame,
                text="Back",
                command=lambda:[buy_num_frame.grid_forget(), set_buy_frame()]
            ).grid(row=3, column=0)

        def set_sell_frame():
            sell_frame.grid(row=5, column=1, sticky='nsew')
            tk.Label(
                    master=sell_frame,
                    text=f"Which stock do you wish to sell?",
                    bg=main.BGCOLOUR
                ).grid(row=0, column=0, columnspan=2)
            ttk.Button(
                master=sell_frame,
                text="Gold",
                state=Game.Game.set_button_state("Sell", "Gold"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Gold")]
            ).grid(row=1,column=0)
            ttk.Button(
                master=sell_frame,
                text="Silver",
                state=Game.Game.set_button_state("Sell", "Silver"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Silver")]
            ).grid(row=2,column=0)
            ttk.Button(
                master=sell_frame,
                text="Oil",
                state=Game.Game.set_button_state("Sell", "Oil"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Oil")]
            ).grid(row=3,column=0)
            ttk.Button(
                master=sell_frame,
                text="Bonds",
                state=Game.Game.set_button_state("Sell", "Bonds"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Bonds")]
            ).grid(row=1,column=1)
            ttk.Button(
                master=sell_frame,
                text="Grain",
                state=Game.Game.set_button_state("Sell", "Grain"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Grain")]
            ).grid(row=2,column=1)
            ttk.Button(
                master=sell_frame,
                text="Industrial",
                state=Game.Game.set_button_state("Sell", "Industrial"),
                command=lambda:[sell_frame.grid_forget(), set_sell_num_frame("Industrial")]
            ).grid(row=3,column=1)
            ttk.Button(
                master=sell_frame,
                text="Back",
                command=lambda:[sell_frame.grid_forget(), set_action_frame()]
            ).grid(row=4, column=0, columnspan=2, sticky="nsew")
            
        def set_sell_num_frame(stock):
            sell_num_frame.grid(row=5, column=1, sticky='nsew')
            set_sell_amount = tk.IntVar()
            sell_range = [i for i in range(500, Player.Player.max_sell(stock)+1, 500)]

            tk.Label(
                master=sell_num_frame,
                text=f"How many shares of {stock} do you wish to sell?",
                bg=main.BGCOLOUR
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
                command=lambda:[Game.Game.set_turn(), Player.Player.sell_stock(stock, set_sell_amount.get()), clear_frames(left_stats_frame), clear_frames(right_stats_frame), Game.Game.set_player_frames(self, left_stats_frame, right_stats_frame), set_action_state("Sell")]
            ).grid(row=2, column=0)
            ttk.Button(
                master=sell_num_frame,
                text="Back",
                command=lambda:[clear_frames(sell_num_frame), sell_num_frame.grid_forget(), set_sell_frame()]
            ).grid(row=3, column=0)
            
        def set_action_state(action):
            '''action is menu player is currently in.'''
            if action == "Sell":
                if Player.Player.can_sell_any():
                    sell_frame.grid_forget()
                    set_sell_frame()
                else:
                    sell_frame.grid_forget()
                    sell_num_frame.grid_forget()
                    set_action_frame()
            elif action == "Buy":
                if Player.Player.can_buy_any():
                    buy_num_frame.grid_forget()
                    set_buy_frame()
                else:
                    buy_num_frame.grid_forget()
                    buy_frame.grid_forget()
                    set_action_frame()

        def loadgame():
            import shelve
            with shelve.open('game') as file:
                print(file)
                print(f"{file['stocks']=}")
                print(f"{file['players'][0].name=}")
                print(f"{file['curr_round']=}")
                print(f"{file['max_rounds']=}")
                print(f"{file['curr_player']=}")
                print(f"{file['num_players']=}")

        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu.MainMenu(parent=self.parent))
        ).grid(row=7, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=8, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Save Game",
            command=lambda: [Game.Game.save('game'), loadgame()]
        ).grid(row=9, column=0, columnspan=3, sticky="sew")