# StockTickerGUI
A graphical version of Stock Ticker

## Stock Ticker

The object of the game is to buy and sell stock shares within a set number of rounds. As the game plays, stock values can fluctuate dramatically. At the end of the final round, all shares are sold off at market value, and the player with the most money is declared the winner.

Number of players: 2 - 8

Number of rounds: 1 - 100

#### Features:

* Can choose number of players and number of rounds.
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

* Main Game Page: Add option to save game
* Main Game Page: Add button to roll the dice -> Create dice roll animation to go with it
* Main Menu: Add option to load game
* Main Menu: Add highscore list organized by number of rounds played
* General: Add networking option to allow players to play remotely together
* General: Add bots?

#### Things To Fix:

* Player name page: Names can be left blank
* Final results: Winner is not included in player ranking list
* Main Game: need to destroy many frames instead of stacking on top, causing buggy behaviour after awhile
* Overall design needs improvement
* About page: Needs improvement

#### Inspiration:

This is based on the now out of print board game, Stock Ticker, published by Copp Clark Publishing Company.
