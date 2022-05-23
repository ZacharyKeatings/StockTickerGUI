import Game
import Stock

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
        return Player.players[Game.Game.curr_player].name

    def next_player():
        Game.Game.curr_player += 1

    def can_buy(stock):
        if Player.players[Game.Game.curr_player].money >= Stock.Stock.stock_value[stock] * 500:
            return True
        else:
            return False

    def can_sell(stock):
        if Player.players[Game.Game.curr_player].stocks[stock] > 0:
            return True
        else:
            return False

    def max_buy(stock):
        max_buy = Player.players[Game.Game.curr_player].money // Stock.Stock.stock_value[stock]
        return int(max_buy)

    def max_sell(stock):
        max_sell = Player.players[Game.Game.curr_player].stocks[stock]
        return max_sell

    def buy_stock(stock, amount):
        Player.players[Game.Game.curr_player].money -= amount * Stock.Stock.stock_value[stock]
        Player.players[Game.Game.curr_player].stocks[stock] += amount

    def sell_stock(stock, amount):
        Player.players[Game.Game.curr_player].money += amount * Stock.Stock.stock_value[stock]
        Player.players[Game.Game.curr_player].stocks[stock] -= amount