import tkinter as tk
from logging_config import setup_logging
from AutoClickerApp import AutoClickerApp

if __name__ == "__main__":
    setup_logging()
    
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()