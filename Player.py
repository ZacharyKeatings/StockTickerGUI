import Game
import Stock

class Player:
    players = []

    def __init__(self, name):
        self.name = name
        self.money = 5000
        self.stocks = {
            "Gold": 1000,
            "Silver": 1000,
            "Oil": 1000,
            "Bonds": 1000,
            "Grain": 1000,
            "Industrial": 1000
        }

    def create_player():
        new_player = Player()
        Player.players.append(new_player)

    def current_player_name():
        return Player.players[Game.Game.curr_player].name

    def next_player():
        Game.Game.curr_player += 1

    def can_buy(stock):
        if int(Player.players[Game.Game.curr_player].money) >= int(Stock.Stock.stock_value[stock] * 500):
            return True
        else:
            return False

    def can_buy_any():
        #iterate through all stocks, checking for can_buy status. if any are True, return True, else False.
        buy = False
        for index, stock_name in enumerate(Stock.Stock.stock_value):
            if Player.can_buy(stock_name):
                buy = True
        return buy

    def can_sell(stock):
        if int(Player.players[Game.Game.curr_player].stocks[stock]) > 0:
            return True
        else:
            return False

    def any_holding(stock):
        any_has = False
        if Stock.Stock.stock_value[stock] >= 1:
            for i in range(Game.Game.num_players):
                if int(Player.players[i].stocks[stock]) > 0:
                    any_has = True
        return any_has

    def can_sell_any():
        sell = False
        for index, stock_name in enumerate(Stock.Stock.stock_value):
            if Player.can_sell(stock_name):
                sell = True
        return sell

    def max_buy(stock):
        max_buy = Player.players[Game.Game.curr_player].money // Stock.Stock.stock_value[stock]
        return int(max_buy)

    def max_sell(stock):
        max_sell = Player.players[Game.Game.curr_player].stocks[stock]
        return int(max_sell)

    def buy_stock(stock, amount):
        Player.players[Game.Game.curr_player].money -= amount * Stock.Stock.stock_value[stock]
        Player.players[Game.Game.curr_player].money = int(Player.players[Game.Game.curr_player].money)
        Player.players[Game.Game.curr_player].stocks[stock] += amount
        Player.players[Game.Game.curr_player].stocks[stock] = int(Player.players[Game.Game.curr_player].stocks[stock])

    def sell_stock(stock, amount):
        Player.players[Game.Game.curr_player].money += amount * Stock.Stock.stock_value[stock]
        Player.players[Game.Game.curr_player].money = int(Player.players[Game.Game.curr_player].money)
        Player.players[Game.Game.curr_player].stocks[stock] -= amount
        Player.players[Game.Game.curr_player].stocks[stock] = int(Player.players[Game.Game.curr_player].stocks[stock])