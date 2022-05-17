# StockTickerGUI
A graphical version of Stock Ticker

## Stock Ticker

The object of the game is to buy and sell stocks, and by so doing accumulate a greater amount of money than the other self. The winner is decided by setting a time limit at the start of the game, and is the person having the greatest amount of money when time elapses, after selling his stocks back to the Broker at their final market value.

#### Features:

* Can choose number of self and number of rounds.
* Players can be given custom names.
* Players can buy and sell stocks.
* Dice get rolled at beginning of each player's turn.
* Stock values change based on dice roll.
* Stocks can pay dividends, double, and split.
* Graph updates with current stock value each turn.
* Rounds get tracked and results screen displays player scores.
* About page with short description of game.
* The 'Quit' button closes the program.

#### Project Status:

This is an ongoing project which will be updated as I learn more about Tkinter.
This is a GUI version of the console-based Stock Ticker which can be found in the [Stock-Ticker repo](https://github.com/ZacharyKeatings/Stock-Ticker).

#### To-Do:

* Main Game Page: Add notification bar
* Main Game Page: Add option to save game
* Main Game Page: Add button to roll the dice -> Create dice roll animation to go with it
* Main Game Page/End Game Page: Change all float values to int
* Main Game Page: Add current stock value to every stock in graph
* Main Game Page: Set static graph values
* Main Game Page: Set unique colour for each stock
* Main Game Page: Create line at 1 for easier readability of which stocks payout and which don't
* Main Menu: Add option to load game
* Main Menu: Add highscore list organized by number of rounds played
* End Game Page.final_results: Rank all players based on amount of money 
* General: Add networking option to allow self to play remotely together
* General: Add bots?

#### Things To Fix:

* Player name page: Names can be left blank
* Game Setup Page: Sell num frame does not display
* Main Game Page: Buy num frame does not display
* Main Game Page: Sell num frame does not display
* Overall design needs improvement
* About page: Needs improvement
* Gameplay: After pressing 'Ok' on buy/sell, go to set [buy/sell] frame instead of action_frame

#### Inspiration:

This is based on the now out of print board game, Stock Ticker, published by Copp Clark Publishing Company.
