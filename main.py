# main.py
import tkinter as tk
from gui import GroceryApp

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()
