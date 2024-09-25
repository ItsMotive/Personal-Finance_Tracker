import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.database.db_operations import addSavingsCallback
from src.gui.savings_gui import createSavingsInputGUI


def createSavingsTab(notebook: ttk.Notebook, root: tk.Tk):

    savings_tab = ttk.Frame(notebook)

    savings_icon = ImageTk.PhotoImage(
        Image.open("assets/icons/piggybank.png").resize((20, 20))
    )

    savings_tab.expense_icon = savings_icon

    notebook.add(savings_tab, text="Savings")
    notebook.tab(savings_tab, image=savings_icon, compound="left")

    savings_tab.grid_columnconfigure(0, weight=1)  # Centers elements in the center

    # Display Savings Input button
    display_savings_goal_input_button = tk.Button(
        savings_tab,
        text="Add Savings Entry",
        command=lambda: createSavingsInputGUI(root, addSavingsCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_goal_input_button.grid(
        row=0, column=0, padx=5, pady=(20, 5), sticky="n"
    )
