import tkinter as tk

import sys
import os

from GUI_Table_Setup import (
    graphOptions, incomeTableGUI, expenseTableGUI, savingsTableGUI,
    incomeInputDataGUI, expenseInputDataGUI, savingsInputDataGUI,
    generateExpenseAndIncomeGraph
)

# # Add the parent directory of Step_2 to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from Step_2.Database import displayIncomeTable, displayExpenseTable, displaySavingsTable

def generateGUI():
    # Creates Main Application Window
    root = tk.Tk()

    # Setting Title of Application
    root.title("Personal Finance Tracker")

    # Setting Application Window Size
    root.geometry("600x300")

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)

# --------------------- Main Window Info --------------------- #

    # Application Title Message
    label = tk.Label(root, text="Welcome to your Personal Finance Tracker!")
    label.grid(row=0, column=0, columnspan=4, pady=20, sticky="n")

    # Table Display Header
    header_table_display_label = tk.Label(root, text="Table Displays")
    header_table_display_label.grid(row=1, column=0, pady=10, padx=5)

    # Table Entry Header
    header_table_entry_label = tk.Label(root, text="Table Entries")
    header_table_entry_label.grid(row=1, column=1, pady=10, padx=5)

    # Reports Header
    header_table_entry_label = tk.Label(root, text="Reports")
    header_table_entry_label.grid(row=1, column=2, pady=10, padx=5)

    # Comparison Graph Header
    header_table_entry_label = tk.Label(root, text="Comparisons")
    header_table_entry_label.grid(row=1, column=3, pady=10, padx=5)

    # --------------------- Income Info --------------------- #

    # Display Income Table button
    display_income_table_button = tk.Button(root, text="Display Income Table", command=lambda: incomeTableGUI(root))
    display_income_table_button.grid(row=2, column=0, pady=10, padx=5)

    # Display Income Input button
    display_income_input_button = tk.Button(root, text="Add Income Entry", command=lambda: incomeInputDataGUI(root))
    display_income_input_button.grid(row=2, column=1, pady=10, padx=5)

    # Display Income Report button
    display_income_graph_button = tk.Button(root, text="View Income Report", command=lambda: graphOptions(root, "income"))
    display_income_graph_button.grid(row=2, column=2, pady=10, padx=5)

    # --------------------- Expense Info --------------------- #

    # Display Expense Table button
    display_expense_table_button = tk.Button(root, text="Display Expense Table", command=lambda: expenseTableGUI(root))
    display_expense_table_button.grid(row=3, column=0, pady=10, padx=5)

    # Display Expense Input button
    display_expense_input_button = tk.Button(root, text="Add Expense Entry", command=lambda: expenseInputDataGUI(root))
    display_expense_input_button.grid(row=3, column=1, pady=10, padx=5)

    # Display Expense Report button
    display_expense_graph_button = tk.Button(root, text="View Expense Report", command=lambda: graphOptions(root, "expense"))
    display_expense_graph_button.grid(row=3, column=2, pady=10, padx=5)

    # --------------------- Savings Info --------------------- #

    # Display Savings Table button
    display_savings_table_button = tk.Button(root, text="Display Savings Table", command=lambda: savingsTableGUI(root))
    display_savings_table_button.grid(row=4, column=0, pady=10, padx=5)

    # Display Savings Input button
    display_savings_input_button = tk.Button(root, text="Add Savings Entry", command=lambda: savingsInputDataGUI(root))
    display_savings_input_button.grid(row=4, column=1, pady=10, padx=5)

    # Display Savings Report button
    display_savings_graph_button = tk.Button(root, text="View Savings Report", command=lambda: print("WIP"))
    display_savings_graph_button.grid(row=4, column=2, pady=10, padx=5)

    # --------------------- Comparison Info --------------------- #

    # Display Comparison Table button
    display_savings_table_button = tk.Button(root, text="Display Income vs Expense Report", command=lambda: generateExpenseAndIncomeGraph())
    display_savings_table_button.grid(row=2, column=3, pady=10, padx=5)

    # --------------------- Other --------------------- #

    # Bind closing event of the main window to close all windows
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    root.mainloop()
