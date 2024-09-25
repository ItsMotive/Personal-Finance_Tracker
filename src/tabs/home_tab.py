import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from DB_Setup.Database_Table_Creation_Script import createTables


# Used for getting window size
def get_window_size(root):
    root.update_idletasks()  # Ensure the window has been drawn and sized
    width = root.winfo_width()
    height = root.winfo_height()
    print(f"Current window size: {width}x{height}")


def createHomeTab(notebook: ttk.Notebook, root: tk.Tk) -> None:

    home_tab = ttk.Frame(notebook)

    home_icon = ImageTk.PhotoImage(
        Image.open("assets/icons/database.png").resize((20, 20))
    )

    home_tab.home_icon = home_icon

    notebook.add(home_tab, text="Home")
    notebook.tab(home_tab, image=home_icon, compound="left")

    home_tab.grid_rowconfigure(0, weight=0)  # Top Row (Title Label)
    home_tab.grid_rowconfigure(1, weight=0)  # (DB Setup Button)
    home_tab.grid_columnconfigure(0, weight=1)  # Centers elements in the center

    # Home Page Welcome Message
    title_label = tk.Label(
        home_tab,
        text="Welcome to your Personal Finance Tracker",
        font=("Arial", 12),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
        padx=20,
        pady=10,
        relief="flat",
    )
    title_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

    # DB Setup button
    display_db_setup_button = tk.Button(
        home_tab,
        text="Setup PostgreSQL Database",
        command=lambda: createTables(),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_db_setup_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # button = tk.Button(
    #     home_tab, text="Get Window Size", command=lambda: get_window_size(root)
    # )
    # button.grid(row=2, column=0, padx=20, pady=20, sticky="n")
