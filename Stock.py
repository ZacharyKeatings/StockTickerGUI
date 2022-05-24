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
        '''Called by Dice.roll()
        Decreases share value by Dice.roll() amount'''
        Stock.stock_value[stock] += (amount / 100)
        if Stock.stock_value[stock] > 1.95:
            Stock.double_stock(stock)

    def decrease_value(stock, amount):
        '''Called by Dice.roll()
        Increases share value by Dice.roll() amount'''
        Stock.stock_value[stock] -= (amount / 100)
        if Stock.stock_value[stock] < .05:
            Stock.split_stock(stock)

    def dividend(stock, amount):
        '''When Dice.roll() action == Dividend,
        payout based on formula:
        player share amount * Dice.roll() amount%'''
        dividend = (amount / 100)
        if Stock.stock_value[stock] >= 1:
            for i, v in enumerate(Player.Player.players):
                bonus = Player.Player.players[i].stocks[stock] * dividend
                Player.Player.players[i].money += int(bonus)
                Player.Player.players[i].money = int(Player.Player.players[i].money)

    def double_stock(stock):
        '''Called when share value hits 2.
        Reset share value to 1.
        Share amount doubled by all invested players.'''
        Stock.stock_value[stock] = 1
        for i, v in enumerate(Player.Player.players):
            Player.Player.players[i].stocks[stock] *= 2
            Player.Player.players[i].stocks[stock] = int(Player.Player.players[i].stocks[stock])

    def split_stock(stock):
        '''Called if share value hits 0.
        Reset share value to 1.
        Remove all shares by all invested players.'''
        Stock.stock_value[stock] = 1
        for i, v in enumerate(Player.Player.players):
            Player.Player.players[i].stocks[stock] = 0

    def get_value(stock, amount):
        '''Used in EndGame to show total value of a stock held by player'''
        value = amount * Stock.stock_value[stock]
        return int(value)

    def reset_values():
        '''Called when new game is started.
        If a game had already been played without closing window,
        data would carry over without being cleared. This ensures
        every game starts equally. '''
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