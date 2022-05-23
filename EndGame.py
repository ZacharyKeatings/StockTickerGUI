import tkinter as tk
from tkinter import ttk
import main
import MainMenu
import Player
import Game
import Stock

class EndGame(tk.Frame):
    def __init__(self, parent: main.MainWindow):
        tk.Frame.__init__(self, master=parent, bg=main.BGCOLOUR)
        self.parent = parent
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(1, weight=1)

        def final_results():
            #!Rank all players from first to last based on total money.
            #!In Label at top of results_frame, have {Name} won! in big text
            pass

        def end_loop():
            stock_keys = list(Player.Player.players[Game.Game.curr_player].stocks.keys())
            if Game.Game.curr_player <= Game.Game.num_players:
                #sell off shares, show value of each stock
                for index, name in enumerate(stock_keys):
                    quantity = Player.Player.max_sell(name) 
                    Player.Player.sell_stock(name, quantity)
                    tk.Label(
                        master=results_frame,
                        text=f"Value of {name} shares: {int(Stock.Stock.get_value(name, quantity))}",
                        bg=main.BGCOLOUR
                    ).grid(row=index, column=1, sticky="snew")
                #display curr_players money in tk.Label
                tk.Label(
                    master=results_frame,
                    text=f"{Player.Player.current_player_name()} has ${Player.Player.players[Game.Game.curr_player].money}",
                    bg=main.BGCOLOUR
                ).grid(row=6, column=1, sticky='ew')

                if Game.Game.curr_player < Game.Game.num_players-1:
                    ttk.Button(
                        master=results_frame,
                        text="Next player",
                        command=lambda: [Player.Player.next_player(), self.parent.switch_to(target=EndGame(parent=self.parent))]
                    ).grid(row=7, column=1, sticky='sew')
                elif Game.Game.curr_player == Game.Game.num_players-1:
                    ttk.Button(
                        master=results_frame,
                        text="See final results",
                        command=lambda:[final_results()]
                    ).grid(row=7, column=1, sticky="sew")

                
        tk.Label(
            master=self,
            text="End Game",
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

        results_frame = tk.LabelFrame(
            master=self,
            text="Actions:",
            bg=main.BGCOLOUR
        )
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_columnconfigure(1, weight=1)
        results_frame.grid_columnconfigure(2, weight=1)
        results_frame.grid(row=2, rowspan=4, column=1, sticky="nsew")

        end_loop()

        ttk.Button(
            master=self,
            text="Main Menu",
            command=lambda: self.parent.switch_to(target=MainMenu.MainMenu(parent=self.parent))
        ).grid(row=5, column=0, columnspan=3, sticky="sew")
        ttk.Button(
            master=self,
            text="Quit",
            command=exit
        ).grid(row=6, column=0, columnspan=3, sticky="sew")