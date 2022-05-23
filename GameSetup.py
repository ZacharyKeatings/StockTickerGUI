import tkinter as tk
from tkinter import ttk
import main
import MainMenu
import PlayerNamePage
import Game
import Player
import MainGame

class GameSetup(tk.Frame):

    def __init__(self, parent: main.MainWindow):
        tk.Frame.__init__(self, master=parent, bg=main.BGCOLOUR)
        self.parent = parent
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(1, weight=1)

        def finish_setup():
            if Game.Game.curr_player == Game.Game.num_players-1:
                Game.Game.next_player()
                self.parent.switch_to(target=MainGame.MainGame(parent=self.parent))
            else:
                Game.Game.next_player()
                self.parent.switch_to(target=GameSetup(parent=self.parent))

        tk.Label(
            master=self,
            text="Game Setup round",
            bg=main.BGCOLOUR
        ).grid(row=0, column=0, columnspan=3, sticky='new')
        cur_player = tk.LabelFrame(
            master=self,
            text="Current Player:",
            bg=main.BGCOLOUR
        )
        cur_player.grid(row=1, column=1, sticky="new")

        tk.Label(
            master=cur_player,
            text=Player.Player.current_player_name(),
            bg=main.BGCOLOUR
        ).grid(row=1, column=1, sticky='snew')

        #Create number of player frames based on number of players chosen in newgame page
        self.player_grid = []
        for num in range(Game.Game.num_players):
            widget = tk.LabelFrame(
                master=self,
                text=f"{Player.Player.players[num].name}:",
                bg=main.BGCOLOUR
            )
            self.player_grid.append(widget)

        #display all player frames on page that was just created above
        for num in range(Game.Game.num_players):
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
        for num in range(Game.Game.num_players):
            tk.Label(
                master=self.player_grid[num],
                text=f"Money: {Player.Player.players[num].money}",
                bg=main.BGCOLOUR
            ).grid(row=0, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Gold: {Player.Player.players[num].stocks['Gold']}",
                bg=main.BGCOLOUR
            ).grid(row=1, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Silver: {Player.Player.players[num].stocks['Silver']}",
                bg=main.BGCOLOUR
            ).grid(row=2, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Oil: {Player.Player.players[num].stocks['Oil']}",
                bg=main.BGCOLOUR
            ).grid(row=3, column=0, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Bonds: {Player.Player.players[num].stocks['Bonds']}",
                bg=main.BGCOLOUR
            ).grid(row=1, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Grain: {Player.Player.players[num].stocks['Grain']}",
                bg=main.BGCOLOUR
            ).grid(row=2, column=1, sticky='w')
            tk.Label(
                master=self.player_grid[num],
                text=f"Industrial: {Player.Player.players[num].stocks['Industrial']}",
                bg=main.BGCOLOUR
            ).grid(row=3, column=1, sticky='w')

        def set_action_frame():
            action_frame = tk.LabelFrame(
                master=self,
                text="Actions:",
                bg=main.BGCOLOUR
            )
            action_frame.grid_rowconfigure(0, weight=1)
            action_frame.grid_rowconfigure(1, weight=1)
            action_frame.grid_rowconfigure(2, weight=1)
            action_frame.grid_columnconfigure(0, weight=1)
            action_frame.grid(row=2, rowspan=4, column=1, sticky="nsew")
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
                command=lambda: [finish_setup()]
            ).grid(row=2, column=0)

        set_action_frame()

        def set_buy_frame():

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
            buy_frame.grid(row=2, rowspan=4, column=1, sticky='nsew')
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

            set_buy_amount = tk.IntVar()
            buy_range = [i for i in range(500, Player.Player.max_buy(stock)+1, 500)]

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
            buy_num_frame.grid(row=2, rowspan=4, column=1, sticky='nsew')
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
                command=lambda:[Player.Player.buy_stock(stock, set_buy_amount.get()), self.parent.switch_to(target=GameSetup(parent=self.parent))]
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
                bg=main.BGCOLOUR
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

            set_sell_amount = tk.IntVar()
            sell_range = [i for i in range(500, Player.Player.max_sell(stock)+1, 500)]

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
            sell_num_frame.grid(row=2, rowspan=4, column=1, sticky='nsew')
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
                command=lambda:[Player.Player.sell_stock(stock, set_sell_amount.get()), self.parent.switch_to(target=GameSetup(parent=self.parent))]
            ).grid(row=2, column=0)
            ttk.Button(
                master=sell_num_frame,
                text="Back",
                command=lambda:[sell_num_frame.grid_forget(), set_sell_frame()]
            ).grid(row=3, column=0)
            
        ttk.Button(
            master=self,
            text="Back",
            command=lambda: self.parent.switch_to(target=PlayerNamePage.PlayerNamePage(parent=self.parent))
        ).grid(row=6, column=0, columnspan=3, sticky="sew")
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