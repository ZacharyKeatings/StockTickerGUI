import tkinter as tk
import shelve
import main
import Player
import Stock

class Game:
    num_players = 0
    curr_player = 0
    max_rounds = 0
    curr_round = 0
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

    def set_button_state(action, stock):
        """Set tkinter button state based on if player
        can buy or sell the currently chosen stock
        action: ['Buy', 'Sell']
        stock: ['Gold','Silver','Oil','Bonds','Grain','Industrial']"""
        if action == "Buy":
            if Player.Player.can_buy(stock) == True:
                return tk.NORMAL
            elif Player.Player.can_buy(stock) == False:
                return tk.DISABLED
        elif action == "Sell":
            if Player.Player.can_sell(stock) == True:
                return tk.NORMAL
            elif Player.Player.can_sell(stock) == False:
                return tk.DISABLED

    def can_buy_any():
        current_prices = []
        stock_name = list(Stock.Stock.stock_value)
        for stock in range(len(Stock.Stock.stock_value)):
            stock_price = Stock.Stock.stock_value[stock_name[stock]]
            current_prices.append(stock_price)
        if Player.Player.players[Game.curr_player].money < (min(current_prices) * 500):
            return tk.DISABLED
        else:
            return tk.NORMAL

    def can_sell_any():
        """Sets state of action_frame 'Sell' buttons"""
        current_shares = []
        stock_name = list(Player.Player.players[Game.curr_player].stocks)
        for value in range(len(Player.Player.players[Game.curr_player].stocks)):
            stock_price = Player.Player.players[Game.curr_player].stocks[stock_name[value]]
            current_shares.append(stock_price)
        if max(current_shares) == 0:
            return tk.DISABLED
        else:
            return tk.NORMAL

    def set_player_frames(self, left, right):
        #Create number of player frames based on number of players chosen in newgame page
            self.player_grid = []
            for num in range(Game.num_players):
                if num % 2 == 0:
                    widget = tk.LabelFrame(
                        master=left,
                        text=f"{Player.Player.players[num].name}:",
                        bg=main.BGCOLOUR
                    )
                else:
                    widget = tk.LabelFrame(
                        master=right,
                        text=f"{Player.Player.players[num].name}:",
                        bg=main.BGCOLOUR
                    )
                self.player_grid.append(widget)

            #display all player frames on page that was just created above
            for num in range(Game.num_players):
                if num == 0:
                    self.player_grid[0].grid(row=0, sticky="nsew")
                if num == 1:
                    self.player_grid[1].grid(row=0, sticky='nsew')
                if num == 2:
                    self.player_grid[2].grid(row=1, sticky='nsew')
                if num == 3:
                    self.player_grid[3].grid(row=1, sticky='nsew')
                if num == 4:
                    self.player_grid[4].grid(row=2, sticky='nsew')
                if num == 5:
                    self.player_grid[5].grid(row=2, sticky='nsew')
                if num == 6:
                    self.player_grid[6].grid(row=3, sticky='nsew')
                if num == 7:
                    self.player_grid[7].grid(row=3, sticky='nsew')
            
            #Create all content to populate player frames
            for num in range(Game.num_players):
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

    def save(filename):
        '''save current state to BAK/DAT/DIR file. Can name a save file. Called from MainGame.
        Use shelve to save data.
        Data saved includes: Stock.stock_values, Player.players, Game.curr_round, 
        Game.max_rounds, Game.curr_player, Game.turn, Game.num_players'''
        with shelve.open(filename) as save_file:
            save_file['stocks'] = Stock.Stock.stock_value
            save_file['players'] = Player.Player.players
            save_file['curr_round'] = Game.curr_round
            save_file['max_rounds'] = Game.max_rounds
            save_file['curr_player'] = Game.curr_player
            save_file['num_players'] = Game.num_players

    def load(filename):
        '''Load game from .txt file. Called from MainMenu. Switches to LoadPage.
        Use shelve to load data.
        Data loaded includes: Stock.stock_values, Player.players, Game.curr_round, 
        Game.max_rounds, Game.curr_player, Game.turn, Game.num_players'''
        with shelve.open(filename) as save_file:
            Stock.Stock.stock_value = save_file['stocks']
            Player.Player.players = save_file['players']
            Game.curr_round = save_file['curr_round']
            Game.max_rounds = save_file['max_rounds']
            Game.curr_player = save_file['curr_player']
            Game.num_players = save_file['num_players']
