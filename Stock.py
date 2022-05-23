import Game
import Player

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
            for i, v in enumerate(Player.Player.players):
                bonus = Player.Player.players[i].stocks[stock] * dividend
                Player.Player.players[i].money += int(bonus)

    def double_stock(stock):
        Stock.stock_value[stock] = 1
        for i, v in enumerate(Player.Player.players):
            Player.Player.players[i].stocks[stock] = Player.Player.players[i].stocks[stock] * 2

    def split_stock(stock):
        Stock.stock_value[stock] = 1
        for i, v in enumerate(Player.Player.players):
            Player.Player.players[i].stocks[stock] = 0

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

        Game.Game.num_players = 0
        Game.Game.curr_player = 0
        Game.Game.max_rounds = 0
        Game.Game.curr_round = 0
        Game.Game.turn = 0

        Player.Player.players = []