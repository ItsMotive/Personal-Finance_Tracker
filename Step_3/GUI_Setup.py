import tkinter as tk

import sys
import os

from GUI_Table_Setup import incomeTableGUI, expenseTableGUI, savingsTableGUI

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

    # Application Title Message
    label = tk.Label(root, text="Welcome to your Personal Finance Tracker!")
    label.pack(pady=20)

    # Display Income Table button
    display_income_table_button = tk.Button(root, text="Display Income Table", command=lambda: incomeTableGUI())
    display_income_table_button.pack(pady=10)

    # Display Expense Table button
    display_expense_table_button = tk.Button(root, text="Display Expense Table", command=lambda: expenseTableGUI())
    display_expense_table_button.pack(pady=10)

    # Display Savings Table button
    display_savings_table_button = tk.Button(root, text="Display Savings Table", command=lambda: savingsTableGUI())
    display_savings_table_button.pack(pady=10)

    root.mainloop()

generateGUI()