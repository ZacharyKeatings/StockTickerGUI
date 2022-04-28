import tkinter as tk
from tkinter import *
# C:/Users/zacha/Envs/StockTickerGUI/Scripts/Activate.ps1 - venv location

#Root window
WIDTH = 600
HEIGHT = 400
root = Tk()
root.title("Stock Ticker")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.iconbitmap('./images/icon.ico')

def show_frame(frame):
    frame.pack(expand=1, fill="both")
    #frame.tkraise()

def hide_frame(frame):
    frame.pack_forget()
    #frame.lower()

#Frames
main_frame = Frame(root, bg="green")
about_frame = Frame(root, bg="blue")
init_game_frame = Frame(root, bg="yellow")
num_players_frame = Frame(init_game_frame, bg="red")
name_players_frame = Frame(init_game_frame, bg="purple")
num_rounds_frame = Frame(init_game_frame, bg="orange")
game_frame = Frame(root, bg="brown")
setup_game_frame = Frame(root, bg="white")
endgame_frame = Frame(root, bg="pink")

main_frame.pack(expand=1, fill="both")

main_title = Label(main_frame, text="this is the main page")
about_button = Button(main_frame, text="about", command=lambda : [show_frame(about_frame), hide_frame(main_frame)])
main_title.pack()
about_button.pack()

about_title = Label(about_frame, text="This is the about page")
main_menu_button = Button(about_frame, text="main menu", command=lambda : [show_frame(main_frame), hide_frame(about_frame)])
about_title.pack()
main_menu_button.pack()

root.mainloop()