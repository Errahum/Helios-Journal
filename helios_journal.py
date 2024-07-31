# Module: main
# Description:
# This module provides a main menu to interact with OpenAI services
# -----------------------------------------------------------------------------

import tkinter as tk

from src.ui.calendar_interface import CalendarApp


def main_heliosjournal():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()


if __name__ == "__main__":
    main_heliosjournal()
