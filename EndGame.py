import tkinter as tk
from tkinter import ttk
import operator
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
            final_frame = tk.LabelFrame(
                master=self,
                text="Final Scores:",
                bg=main.BGCOLOUR
            )
            final_frame.grid_columnconfigure(0, weight=1)
            final_frame.grid_columnconfigure(1, weight=1)
            final_frame.grid_columnconfigure(2, weight=1)
            final_frame.grid(row=2, rowspan=3, column=1, sticky="nsew")

            ranking = {}
            for i, c in enumerate(Player.Player.players):
                money = Player.Player.players[i].money
                name = Player.Player.players[i].name
                player_value = {name : money}
                ranking.update(player_value)

            sorted_ranking = dict(sorted(ranking.items(), key=operator.itemgetter(1), reverse=True))
            winner = []
            for index, name in enumerate(sorted_ranking):
                if index == 0:
                    winner.append(name)
                    winner.append(sorted_ranking[name])
                tk.Label(
                    master=final_frame,
                    text=f"{index+1}. {name} has ${sorted_ranking[name]}",
                    bg=main.BGCOLOUR
                ).grid(row=index+1, column=1, sticky='new')

            tk.Label(
                master=final_frame,
                text=f"{winner[0]} is the WINNER!!!",
                bg=main.BGCOLOUR
            ).grid(row=0, column=1, sticky='new')

        def end_loop():
            #!Fix float to int
            stock_keys = list(Player.Player.players[Game.Game.curr_player].stocks.keys())
            if Game.Game.curr_player <= Game.Game.num_players:
                #sell off shares, show value of each stock
                for index, name in enumerate(stock_keys):
                    quantity = Player.Player.max_sell(name) 
                    Player.Player.sell_stock(name, quantity)
                    tk.Label(
                        master=results_frame,
                        text=f"Value of {name} shares: ${Stock.Stock.get_value(name, quantity)}",
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

        results_frame = tk.LabelFrame(
            master=self,
            text="Results:",
            bg=main.BGCOLOUR
        )
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_columnconfigure(1, weight=1)
        results_frame.grid_columnconfigure(2, weight=1)
        results_frame.grid(row=2, column=1, sticky="nsew")

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

        end_loop()

        Game.Game.set_player_frames(self, left_stats_frame, right_stats_frame)

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