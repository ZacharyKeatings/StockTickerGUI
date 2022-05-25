import sys
import tkinter as tk
import MainMenu

BGCOLOUR = "blanchedalmond"

class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Stock Ticker")
        self.geometry("1024x768+0+0")
        self.iconbitmap("./images/icon.ico")
        self.mainmenu = MainMenu.MainMenu(parent=self)
        self.current = self.mainmenu

        self.mainmenu.pack(fill="both", expand=1)

    def switch_to(self, target):
        self.current.destroy()
        self.current = target
        self.current.pack(fill="both", expand=1)


def main():
    return MainWindow().mainloop()


if __name__ == '__main__':
    sys.exit(main())
