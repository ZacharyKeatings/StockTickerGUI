import tkinter as tk
from tkinter import *
from tkinter.ttk import *
# C:/Users/zacha/Envs/StockTickerGUI/Scripts/Activate.ps1 - venv location

#Root window
WIDTH = 600
HEIGHT = 400
root = tk.Tk()
root.title("Stock Ticker")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.iconbitmap('./images/icon.ico')

#1. main menu - start game button, about page button, exit button ***(add save and highscore list organized by rounds played)***

#2. about page - label with game description

#3. exit - exit() command to close window, bring up confirmation prompt window

# start game (setup):
    #4. choose number of players - label, input box
    #5. choose player names - label, input box
    #6. choose rounds - label, input box
        #7. setup round - game screen, 3 frames: player stats, graph, player options
        #8. game screen - 4 frames: player stats, graph, dice roll, player options
            #9. game finished screen - 3 frames: winner, all players ranked, buttons: main menu, 

def frameChange(frame_to_destroy, frame_to_create):
    frame_to_destroy.pack_forget()
    frame_to_create.pack()

main_frame = Frame(root)
main_frame.pack(fill="both")

about_frame = Frame(root)

main_title = Label(main_frame, text="this is the main page")
about_button = Button(main_frame, text="about", command=lambda : frameChange(main_frame, about_frame))
main_title.pack()
about_button.pack()

about_title = Label(about_frame, text="This is the about page")
main_menu_button = Button(about_frame, text="main menu", command=lambda : frameChange(about_frame, main_frame))
about_title.pack()
main_menu_button.pack()

root.mainloop()