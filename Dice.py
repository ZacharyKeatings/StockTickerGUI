import random
import Stock

class Dice:
    stock = ["Gold", "Silver", "Oil", "Bonds", "Grain", "Industrial"]
    action = ["Up", "Down", "Dividend"]
    amount = [5, 10, 20]

    def roll():
        stock = random.choice(Dice.stock)
        action = random.choice(Dice.action)
        amount = random.choice(Dice.amount)

        if action == Dice.action[0]:
            Stock.Stock.increase_value(stock, amount)
            return stock, action, amount
        elif action == Dice.action[1]:
            Stock.Stock.decrease_value(stock, amount)
            return stock, action, amount
        else:
            return stock, action, amount