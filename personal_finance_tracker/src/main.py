import tkinter as tk
from tkinter import ttk

import os
import sys

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.visualization.graph import generateExpenseAndIncomeGraph, graphOptions
from src.constants import EXPENSE_TABLE_HEADERS, EXPENSE_TABLE_LABEL, INCOME_TABLE_HEADERS, INCOME_TABLE_LABEL, MODIFY_INCOME_TABLE_HEADERS, SAVINGS_TABLE_HEADERS, SAVINGS_TABLE_LABEL
from src.database.SQL_Queries import SELECT_EXPENSE_QUERY, SELECT_INCOME_QUERY, SELECT_SAVINGS_QUERY
from src.database.db_operations import addExpenseCallback, addIncomeCallback, addSavingsCallback, grabAllDatabaseData, updateIncomeCallback
from src.gui.GUIs import createEditableTable, createTableGUI, inputDataToTable

def main():
    # Create the main application window

    root = tk.Tk()

    # Setting Title of Application

    root.title("Personal Finance Tracker")

    # Setting Application Window Size

    root.geometry("400x200")

    # Load the icon

    icon_path = os.path.join("assets/icons", "app_icon.ico")
    root.iconbitmap(icon_path)

    # Configure the main window grid

    root.grid_rowconfigure(0, weight=0)  # Top empty space
    root.grid_rowconfigure(1, weight=0)  # Content area (Notebook)
    root.grid_rowconfigure(2, weight=1)  # Content area (Notebook)
    root.grid_rowconfigure(3, weight=0)  # Bottom empty space
    root.grid_columnconfigure(0, weight=1)  # Center horizontally

    # Create a Frame and add it to the window

    frame = ttk.Frame(root)
    frame.grid(row=1, column=0, padx=25, pady=5, sticky="nsew")

    # Configure the frame grid to expand horizontally

    frame.grid_rowconfigure(0, weight=1)  # Row for the Notebook to expand
    frame.grid_columnconfigure(0, weight=1)  # Center horizontally and allow expansion

    # Create a Notebook (tabbed interface)

    notebook = ttk.Notebook(frame)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Create frames for each tab content

    main_tab = ttk.Frame(notebook)
    income_tab = ttk.Frame(notebook)
    expense_tab = ttk.Frame(notebook)
    savings_tab = ttk.Frame(notebook)
    report_tab = ttk.Frame(notebook)

    # Add frames to notebook as tabs

    notebook.add(main_tab, text="Home")
    notebook.add(income_tab, text="Income")
    notebook.add(expense_tab, text="Expense")
    notebook.add(savings_tab, text="Saving")
    notebook.add(report_tab, text="Reports")

    # Configure each tab frame to center its contents

    for tab in [income_tab, expense_tab, savings_tab, report_tab]:
        tab.grid_rowconfigure(0, weight=0)  # Top row for buttons
        tab.grid_rowconfigure(1, weight=0)  # Row for additional buttons
        tab.grid_rowconfigure(2, weight=1)  # Row for additional buttons
        tab.grid_columnconfigure(0, weight=1)  # Center horizontally
    # # ----------------------- Main Tab ----------------------- #

    # Home Page Welcome Message

    title_label = tk.Label(
        main_tab,
        text="Welcome to your Personal Finance Tracker",
        font=("Arial", 12),
        fg="black",
        padx=20,
        pady=10,
        relief="flat",
    )
    title_label.pack(padx=20, pady=20)

    # # ----------------------- Income Tab ----------------------- #

    # Display Income Table button
    display_income_table_button = tk.Button(
        income_tab, text="Display Income Table", command=lambda: createTableGUI(root, "Income Table", lambda: grabAllDatabaseData(SELECT_INCOME_QUERY), INCOME_TABLE_HEADERS)
    )
    display_income_table_button.grid(row=0, column=0, padx=5, pady=5, sticky="n")

    # Display Income Input button
    display_income_input_button = tk.Button(
        income_tab, text="Add Income Entry", command=lambda: inputDataToTable(root, INCOME_TABLE_LABEL, "Income Entry Form", addIncomeCallback)
    )
    display_income_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Income Report button
    display_income_graph_button = tk.Button(
        income_tab,
        text="View Income Report",
        command=lambda: graphOptions(root, "income"),
    )
    display_income_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # Display Income Manual Input button
    display_income_input_button = tk.Button(
        income_tab, text="Update Income Table", command=lambda: createEditableTable(root, grabAllDatabaseData(SELECT_INCOME_QUERY), MODIFY_INCOME_TABLE_HEADERS, updateIncomeCallback)
    )
    display_income_input_button.grid(row=3, column=0, padx=5, pady=5, sticky="n")

    # ----------------------- Expense Tab ----------------------- #

    # Display Expense Table button

    display_expense_table_button = tk.Button(
        expense_tab, text="Display Expense Table", command=lambda: createTableGUI(root, "Expense Table", lambda: grabAllDatabaseData(SELECT_EXPENSE_QUERY), EXPENSE_TABLE_HEADERS)
    )
    display_expense_table_button.grid(row=0, column=0, padx=5, pady=5, sticky="n")

    # Display Expense Input button

    display_expense_input_button = tk.Button(
        expense_tab, text="Add Expense Entry", command=lambda: inputDataToTable(root, EXPENSE_TABLE_LABEL, "Expense Entry Form", addExpenseCallback)
    )
    display_expense_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Expense Report button

    display_expense_graph_button = tk.Button(
        expense_tab,
        text="View Expense Report",
        command=lambda: graphOptions(root, "expense"),
    )
    display_expense_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # ----------------------- Savings Tab ----------------------- #

    # Display Savings Table button

    display_savings_table_button = tk.Button(
        savings_tab, text="Display Savings Table", command=lambda: createTableGUI(root, "Income Table", lambda: grabAllDatabaseData(SELECT_SAVINGS_QUERY), SAVINGS_TABLE_HEADERS)
    )
    display_savings_table_button.grid(row=0, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Input button

    display_savings_input_button = tk.Button(
        savings_tab, text="Add Savings Entry", command=lambda: inputDataToTable(root, SAVINGS_TABLE_LABEL, "Savings Entry Form", addSavingsCallback)
    )
    display_savings_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Report button

    display_savings_graph_button = tk.Button(
        savings_tab, text="View Savings Report", command=lambda: print("WIP")
    )
    display_savings_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # ----------------------- Reports Tab ----------------------- #

    # Display Comparison Table button

    display_income_expense_comparison_button = tk.Button(
        report_tab,
        text="Display Income vs Expense Report",
        command=lambda: generateExpenseAndIncomeGraph(),
    )
    display_income_expense_comparison_button.grid(
        row=0, column=0, padx=5, pady=5, sticky="n"
    )

    # ----------------------- Other ----------------------- #

    # Bind closing event of the main window to close all windows
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    # Run the application

    root.mainloop()


# Call the main function to start the application

if __name__ == "__main__":
    main()
