import tkinter as tk

import sys
import os

from GUI_Table_Setup import (
    incomeTableGUI, expenseTableGUI, savingsTableGUI,
    incomeInputDataGUI
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
    root.geometry("400x300")

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Application Title Message
    label = tk.Label(root, text="Welcome to your Personal Finance Tracker!")
    label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

    # Display Income Table button
    display_income_table_button = tk.Button(root, text="Display Income Table", command=lambda: incomeTableGUI())
    display_income_table_button.grid(row=1, column=0, pady=10, padx=5)

    # Display Income Table button
    display_income_table_button = tk.Button(root, text="Add Income Entry", command=lambda: incomeInputDataGUI())
    display_income_table_button.grid(row=1, column=1, pady=10, padx=5)

    # Display Expense Table button
    display_expense_table_button = tk.Button(root, text="Display Expense Table", command=lambda: expenseTableGUI())
    display_expense_table_button.grid(row=2, column=0, pady=10, padx=5)

    # Display Savings Table button
    display_savings_table_button = tk.Button(root, text="Display Savings Table", command=lambda: savingsTableGUI())
    display_savings_table_button.grid(row=3, column=0, pady=10, padx=5)

    root.mainloop()
