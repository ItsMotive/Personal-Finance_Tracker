import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.constants import MODIFY_SAVINGS_TABLE_HEADERS, SAVINGS_TABLE_HEADERS
from src.database.SQL_Queries import SELECT_SAVINGS_ENTRIES_QUERY
from src.database.db_operations import (
    addSavingsCallback,
    grabAllDatabaseData,
    updateSavingsCallback,
)
from src.gui.savings_gui import createSavingsInputGUI
from src.gui.util_gui import createEditableTable, createTableGUI


def createSavingsTab(notebook: ttk.Notebook, root: tk.Tk):

    savings_tab = ttk.Frame(notebook)

    savings_icon = ImageTk.PhotoImage(
        Image.open("assets/icons/piggybank.png").resize((20, 20))
    )

    savings_tab.savings_icon = savings_icon

    notebook.add(savings_tab, text="Savings")
    notebook.tab(savings_tab, image=savings_icon, compound="left")

    savings_tab.grid_columnconfigure(0, weight=1)  # Centers elements in the center

    # Display Savings Table button
    display_savings_table_button = tk.Button(
        savings_tab,
        text="Display Savings Table",
        command=lambda: createTableGUI(
            root,
            "Income Table",
            lambda: grabAllDatabaseData(SELECT_SAVINGS_ENTRIES_QUERY),
            SAVINGS_TABLE_HEADERS,
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_table_button.grid(row=0, column=0, padx=5, pady=(20, 5), sticky="n")

    # Display Savings Input button
    display_savings_goal_input_button = tk.Button(
        savings_tab,
        text="Add Savings Entry",
        command=lambda: createSavingsInputGUI(root, addSavingsCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_goal_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Goal Manual Input button
    display_savings_update_button = tk.Button(
        savings_tab,
        text="Update Savings Table",
        command=lambda: createEditableTable(
            root,
            grabAllDatabaseData(SELECT_SAVINGS_ENTRIES_QUERY),
            MODIFY_SAVINGS_TABLE_HEADERS,
            updateSavingsCallback,
            "Savings",
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_update_button.grid(
        row=2, column=0, padx=5, pady=(5, 20), sticky="n"
    )
