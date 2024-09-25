import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.constants import EXPENSE_TABLE_HEADERS, MODIFY_EXPENSE_TABLE_HEADERS
from src.database.SQL_Queries import SELECT_EXPENSE_QUERY
from src.database.db_operations import (
    addExpenseCallback,
    grabAllDatabaseData,
    updateExpenseCallback,
)
from src.gui.expense_gui import createExpenseGraphOptions, createExpenseInputGUI
from src.gui.util_gui import createEditableTable, createTableGUI


def createExpenseTab(notebook: ttk.Notebook, root: tk.Tk) -> None:

    expense_tab = ttk.Frame(notebook)

    expense_icon = ImageTk.PhotoImage(
        Image.open("assets/icons/receipt.png").resize((20, 20))
    )

    expense_tab.expense_icon = expense_icon

    notebook.add(expense_tab, text="Expense")
    notebook.tab(expense_tab, image=expense_icon, compound="left")

    # expense_tab.grid_rowconfigure(0, weight=1)  # Top Row (Title Label)
    # expense_tab.grid_rowconfigure(1, weight=0)  # (DB Setup Button)
    # expense_tab.grid_rowconfigure(2, weight=0)  # (DB Setup Button)
    # expense_tab.grid_rowconfigure(3, weight=0)  # (DB Setup Button)
    # expense_tab.grid_rowconfigure(4, weight=0)  # (DB Setup Button)
    expense_tab.grid_columnconfigure(0, weight=1)  # Centers elements in the center

    # Display Expense Table button
    display_expense_table_button = tk.Button(
        expense_tab,
        text="Display Expense Table",
        command=lambda: createTableGUI(
            root,
            "Expense Table",
            lambda: grabAllDatabaseData(SELECT_EXPENSE_QUERY),
            EXPENSE_TABLE_HEADERS,
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_table_button.grid(row=0, column=0, padx=5, pady=(20, 5), sticky="n")

    # Display Expense Input button
    display_expense_input_button = tk.Button(
        expense_tab,
        text="Add Expense Entry",
        command=lambda: createExpenseInputGUI(root, addExpenseCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Expense Report button
    display_expense_graph_button = tk.Button(
        expense_tab,
        text="View Expense Report",
        command=lambda: createExpenseGraphOptions(root),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # Display Expense Manual Input button
    display_expense_update_button = tk.Button(
        expense_tab,
        text="Update Expense Table",
        command=lambda: createEditableTable(
            root,
            grabAllDatabaseData(SELECT_EXPENSE_QUERY),
            MODIFY_EXPENSE_TABLE_HEADERS,
            updateExpenseCallback,
            "Expense",
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_update_button.grid(
        row=3, column=0, padx=5, pady=(5, 20), sticky="n"
    )
