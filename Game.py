import Player
import Stock
import tkinter as tk

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