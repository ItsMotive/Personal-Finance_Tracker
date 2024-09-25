import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.constants import INCOME_TABLE_HEADERS, MODIFY_INCOME_TABLE_HEADERS
from src.database.SQL_Queries import SELECT_INCOME_QUERY
from src.database.db_operations import (
    addIncomeCallback,
    grabAllDatabaseData,
    updateIncomeCallback,
)
from src.gui.income_gui import createIncomeGraphOptions, createIncomeInputGUI
from src.gui.util_gui import createEditableTable, createTableGUI


def createIncomeTab(notebook: ttk.Notebook, root: tk.Tk) -> None:

    income_tab = ttk.Frame(notebook)

    income_icon = ImageTk.PhotoImage(
        Image.open("assets/icons/wallet.png").resize((20, 20))
    )

    income_tab.income_icon = income_icon

    notebook.add(income_tab, text="Income")
    notebook.tab(income_tab, image=income_icon, compound="left")

    income_tab.grid_columnconfigure(0, weight=1)  # Centers elements in the center

    # Display Income Table button
    display_income_table_button = tk.Button(
        income_tab,
        text="Display Income Table",
        command=lambda: createTableGUI(
            root,
            "Income Table",
            lambda: grabAllDatabaseData(SELECT_INCOME_QUERY),
            INCOME_TABLE_HEADERS,
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_table_button.grid(row=0, column=0, padx=5, pady=(20, 5), sticky="n")

    # Display Income Input button
    display_income_input_button = tk.Button(
        income_tab,
        text="Add Income Entry",
        command=lambda: createIncomeInputGUI(root, addIncomeCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Income Report button
    display_income_graph_button = tk.Button(
        income_tab,
        text="View Income Report",
        command=lambda: createIncomeGraphOptions(root),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # Display Income Manual Input button
    display_income_update_button = tk.Button(
        income_tab,
        text="Update Income Table",
        command=lambda: createEditableTable(
            root,
            grabAllDatabaseData(SELECT_INCOME_QUERY),
            MODIFY_INCOME_TABLE_HEADERS,
            updateIncomeCallback,
            "Income",
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_update_button.grid(row=3, column=0, padx=5, pady=(5, 20), sticky="n")
