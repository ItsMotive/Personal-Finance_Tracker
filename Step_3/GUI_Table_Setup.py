import tkinter as tk
from tkinter import ttk
import psycopg2 # type: ignore
from psycopg2 import sql # type: ignore
import pandas as pd

import sys
import os

# Add the parent directory of Step_2 to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Step_2.Constants import SELECT_INCOME_QUERY, SELECT_EXPENSE_QUERY, SELECT_SAVINGS_QUERY
from Step_2.Database import DB_Connection

# ---------------------------- Display Table GUI ---------------------------- #

def incomeTableGUI():
    # Create the main window
    root = tk.Tk()
    root.title("Income Table")

    # Create a Treeview widget
    tree = ttk.Treeview(root)

    # Insert data
    row_entries = grabIncomeTableData()

    # Define the columns
    tree["columns"] = ("Income Name", "Income Type", "Income Amount", "Income Date")

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
    tree.column("Income Name", anchor=tk.W, width=120)
    tree.column("Income Type", anchor=tk.W, width=100)
    tree.column("Income Amount", anchor=tk.W, width=120)
    tree.column("Income Date", anchor=tk.W, width=120)

    # Create headings
    tree.heading("Income Name", text="Name", anchor=tk.W)
    tree.heading("Income Type", text="Type", anchor=tk.W)
    tree.heading("Income Amount", text="Amount", anchor=tk.W)
    tree.heading("Income Date", text="Date", anchor=tk.W)

    # Insert Row Data
    for row_entry in row_entries:
        tree.insert("", tk.END, values=(row_entry))

    # Add the Treeview to the window
    tree.pack(pady=10, padx=10)

    # Start the Tkinter event loop
    root.mainloop()

def expenseTableGUI():
    # Create the main window
    root = tk.Tk()
    root.title("Expense Table")

    # Create a Treeview widget
    tree = ttk.Treeview(root)

    # Insert data
    row_entries = grabExpenseTableData()

    # Define the columns
    tree["columns"] = ("Expense Name", "Expense Type", "Expense Amount", "Expense Date")

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
    tree.column("Expense Name", anchor=tk.W, width=120)
    tree.column("Expense Type", anchor=tk.W, width=100)
    tree.column("Expense Amount", anchor=tk.W, width=120)
    tree.column("Expense Date", anchor=tk.W, width=120)

    # Create headings
    tree.heading("Expense Name", text="Name", anchor=tk.W)
    tree.heading("Expense Type", text="Type", anchor=tk.W)
    tree.heading("Expense Amount", text="Amount", anchor=tk.W)
    tree.heading("Expense Date", text="Date", anchor=tk.W)

    # Insert Row Data
    for row_entry in row_entries:
        tree.insert("", tk.END, values=(row_entry))

    # Add the Treeview to the window
    tree.pack(pady=10, padx=10)

    # Start the Tkinter event loop
    root.mainloop()

def savingsTableGUI():
    # Create the main window
    root = tk.Tk()
    root.title("Savings Goals Table")

    # Create a Treeview widget
    tree = ttk.Treeview(root)

    # Insert data
    row_entries = grabSavingTableData()

    # Define the columns
    tree["columns"] = ("Goal Name", "Goal Type", "Goal Amount", "Goal Start Date", "Goal End Date")

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
    tree.column("Goal Name", anchor=tk.W, width=120)
    tree.column("Goal Type", anchor=tk.W, width=100)
    tree.column("Goal Amount", anchor=tk.W, width=120)
    tree.column("Goal Start Date", anchor=tk.W, width=120)
    tree.column("Goal End Date", anchor=tk.W, width=120)

    # Create headings
    tree.heading("Goal Name", text="Name", anchor=tk.W)
    tree.heading("Goal Type", text="Type", anchor=tk.W)
    tree.heading("Goal Amount", text="Amount", anchor=tk.W)
    tree.heading("Goal Start Date", text="Start Date", anchor=tk.W)
    tree.heading("Goal End Date", text="End Date", anchor=tk.W)

    # Insert Row Data
    for row_entry in row_entries:
        tree.insert("", tk.END, values=(row_entry))

    # Add the Treeview to the window
    tree.pack(pady=10, padx=10)

    # Start the Tkinter event loop
    root.mainloop()

# ---------------------------- Grab Table Data ---------------------------- #

def grabIncomeTableData() -> list:
    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")
        
        # Execute a query to select data from the table
        cur.execute(SELECT_INCOME_QUERY)

        # Fetch all rows from the executed query
        rows = cur.fetchall()

    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

        return rows

def grabExpenseTableData() -> list:
    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")
        
        # Execute a query to select data from the table
        cur.execute(SELECT_EXPENSE_QUERY)

        # Fetch all rows from the executed query
        rows = cur.fetchall()

    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

        return rows

def grabSavingTableData() -> list:
    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")
        
        # Execute a query to select data from the table
        cur.execute(SELECT_SAVINGS_QUERY)

        # Fetch all rows from the executed query
        rows = cur.fetchall()

    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

        return rows
