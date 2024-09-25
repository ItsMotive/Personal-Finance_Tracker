import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.constants import MODIFY_SAVINGS_TABLE_HEADERS, SAVINGS_TABLE_HEADERS
from src.database.SQL_Queries import SELECT_SAVINGS_QUERY
from src.database.db_operations import (
    addSavingsGoalCallback,
    grabAllDatabaseData,
    updateSavingsGoalCallback,
)
from src.gui.savings_goal_gui import createSavingsGoalInputGUI
from src.gui.util_gui import createEditableTable, createTableGUI


def createSavingGoalsTab(notebook: ttk.Notebook, root: tk.Tk):

    saving_goals_tab = ttk.Frame(notebook)

    saving_goals_icon = ImageTk.PhotoImage(
        Image.open("assets/icons/goal.png").resize((20, 20))
    )

    saving_goals_tab.expense_icon = saving_goals_icon

    notebook.add(saving_goals_tab, text="Saving Goals")
    notebook.tab(saving_goals_tab, image=saving_goals_icon, compound="left")

    saving_goals_tab.grid_columnconfigure(0, weight=1)  # Centers elements in the center

    # Display Savings Goal Table button
    display_savings_goal_table_button = tk.Button(
        saving_goals_tab,
        text="Display Savings Table",
        command=lambda: createTableGUI(
            root,
            "Income Table",
            lambda: grabAllDatabaseData(SELECT_SAVINGS_QUERY),
            SAVINGS_TABLE_HEADERS,
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_goal_table_button.grid(
        row=0, column=0, padx=5, pady=(20, 5), sticky="n"
    )

    # Display Savings Goal Input button
    display_savings_goal_input_button = tk.Button(
        saving_goals_tab,
        text="Add Savings Goal Entry",
        command=lambda: createSavingsGoalInputGUI(root, addSavingsGoalCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_goal_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Report button
    display_savings_graph_button = tk.Button(
        saving_goals_tab,
        text="View Savings Report",
        command=lambda: print("WIP"),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Goal Manual Input button
    display_savings_update_button = tk.Button(
        saving_goals_tab,
        text="Update Savings Goal Table",
        command=lambda: createEditableTable(
            root,
            grabAllDatabaseData(SELECT_SAVINGS_QUERY),
            MODIFY_SAVINGS_TABLE_HEADERS,
            updateSavingsGoalCallback,
            "SavingsGoal",
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_update_button.grid(
        row=3, column=0, padx=5, pady=(5, 20), sticky="n"
    )
