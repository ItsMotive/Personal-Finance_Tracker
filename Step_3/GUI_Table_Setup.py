from collections import defaultdict
from datetime import datetime
import tkinter as tk
from tkinter import Toplevel, ttk
import tkinter
from matplotlib import pyplot as plt
import numpy as np
import psycopg2
from psycopg2 import sql
import pandas as pd

import sys
import os

from Graphs import pieGraph, barGraph

# Add the parent directory of Step_2 to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Step_2.Constants import SELECT_INCOME_QUERY, SELECT_EXPENSE_QUERY, SELECT_SAVINGS_QUERY
from Step_2.Database import DB_Connection, addIncomeGUI, addExpenseGUI, addSavingsGoalGUI

# ---------------------------- Display Table GUI ---------------------------- #

def incomeTableGUI(root: tkinter.Tk) -> None:
    # Create the main window
    income_window = Toplevel(root)
    income_window.title("Income Table")

    # Create a Treeview widget
    tree = ttk.Treeview(income_window)

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

    # # Create headings
    # tree.heading("Income Name", text="Name", anchor=tk.W)
    # tree.heading("Income Type", text="Type", anchor=tk.W)
    # tree.heading("Income Amount", text="Amount", anchor=tk.W)
    # tree.heading("Income Date", text="Date", anchor=tk.W)

    # Create headings with sorting functionality
    for col in tree["columns"]:
        tree.heading(col, text=col, anchor=tk.W, command=lambda _col=col: sort_column(tree, _col, False))

    # Insert Row Data
    for row_entry in row_entries:
        tree.insert("", tk.END, values=(row_entry))

    # Add the Treeview to the window
    tree.pack(pady=10, padx=10)

def expenseTableGUI(root: tkinter.Tk) -> None:
    # Create the main window
    expense_window = Toplevel(root)
    expense_window.title("Expense Table")

    # Create a Treeview widget
    tree = ttk.Treeview(expense_window)

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

    # # Create headings
    # tree.heading("Expense Name", text="Name", anchor=tk.W)
    # tree.heading("Expense Type", text="Type", anchor=tk.W)
    # tree.heading("Expense Amount", text="Amount", anchor=tk.W)
    # tree.heading("Expense Date", text="Date", anchor=tk.W)

    # Create headings with sorting functionality
    for col in tree["columns"]:
        tree.heading(col, text=col, anchor=tk.W, command=lambda _col=col: sort_column(tree, _col, False))

    # Insert Row Data
    for row_entry in row_entries:
        tree.insert("", tk.END, values=(row_entry))

    # Add the Treeview to the window
    tree.pack(pady=10, padx=10)

def savingsTableGUI(root: tkinter.Tk) -> None:
    # Create the main window
    savings_window = Toplevel(root)
    savings_window.title("Savings Goals Table")

    # Create a Treeview widget
    tree = ttk.Treeview(savings_window)

    # Insert data
    row_entries = grabSavingTableData()

    # Define the columns
    tree["columns"] = ("Goal Name", "Goal Type", "Goal Amount", "Goal Start Date", "Goal End Date", "Active")

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
    tree.column("Goal Name", anchor=tk.W, width=120)
    tree.column("Goal Type", anchor=tk.W, width=100)
    tree.column("Goal Amount", anchor=tk.W, width=120)
    tree.column("Goal Start Date", anchor=tk.W, width=120)
    tree.column("Goal End Date", anchor=tk.W, width=120)
    tree.column("Active", anchor=tk.W, width=120)

    # # Create headings
    # tree.heading("Goal Name", text="Name", anchor=tk.W)
    # tree.heading("Goal Type", text="Type", anchor=tk.W)
    # tree.heading("Goal Amount", text="Amount", anchor=tk.W)
    # tree.heading("Goal Start Date", text="Start Date", anchor=tk.W)
    # tree.heading("Goal End Date", text="End Date", anchor=tk.W)

    # Create headings with sorting functionality
    for col in tree["columns"]:
        tree.heading(col, text=col, anchor=tk.W, command=lambda _col=col: sort_column(tree, _col, False))

    # Insert Row Data
    for row_entry in row_entries:
        tree.insert("", tk.END, values=(row_entry))

    # Add the Treeview to the window
    tree.pack(pady=10, padx=10)


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


# ---------------------------- Input Data into Table ---------------------------- #

def incomeInputDataGUI(root: tkinter.Tk) -> None:
    # Create the main window
    income_input_window = Toplevel(root)
    
    # Create Title for GUI Application
    income_input_window.title("Adding Income")

    # Create the Label and Entry widgets using grid layout for Income Name
    income_name_label = tk.Label(income_input_window, text="Enter Income Name:")
    income_name_label.grid(row=0, column=0, padx=10, pady=10)

    income_name_box = tk.Entry(income_input_window, width=40)
    income_name_box.grid(row=0, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Income Type
    income_type_label = tk.Label(income_input_window, text="Enter Income Type:")
    income_type_label.grid(row=1, column=0, padx=10, pady=10)

    income_type_box = tk.Entry(income_input_window, width=40)
    income_type_box.grid(row=1, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Income Amount
    income_amount_label = tk.Label(income_input_window, text="Enter Income Amount:")
    income_amount_label.grid(row=2, column=0, padx=10, pady=10)

    income_amount_box = tk.Entry(income_input_window, width=40)
    income_amount_box.grid(row=2, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Income Date
    income_date_label = tk.Label(income_input_window, text="Enter Income Date (MM/DD/YYYY) (*Leave blank for today): ")
    income_date_label.grid(row=3, column=0, padx=10, pady=10)

    income_date_box = tk.Entry(income_input_window, width=40)
    income_date_box.grid(row=3, column=1, padx=10, pady=10)

    def submit_income():
        # Get the text from the input box
        income_name_input = income_name_box.get()
        income_type_input = income_type_box.get()
        income_amount_input = income_amount_box.get()
        income_date_input = income_date_box.get()

        if income_date_input == '':
            income_date_input = datetime.now().strftime("%m/%d/%Y")

        # Display the text in a label
        if income_name_input == '':
            result_label.config(text="Income Name is required!")

        elif income_type_input == '':
            result_label.config(text="Income Type is required!")

        elif income_amount_input == '':
            result_label.config(text="Income Amount is required!")

        else:
            addIncomeGUI(income_name_input, income_type_input, income_amount_input, income_date_input)
            result_label.config(text=f"Submission Successful! \n Income Name: {income_name_input} \n Income Type: {income_type_input} \n Income Amount: {income_amount_input} \n Income Date: {income_date_input}")

    # Create a Submit button widget
    submit_button = tk.Button(income_input_window, text="Submit", command=submit_income)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Create a Submit label widget to display the result
    result_label = tk.Label(income_input_window, text="Input will be displayed here")
    result_label.grid(row=5, column=0, columnspan=2, pady=10)

def expenseInputDataGUI(root: tkinter.Tk) -> None:
    # Create the main window
    root = Toplevel(root)
    
    # Create Title for GUI Application
    root.title("Adding Expense")

    # Create the Label and Entry widgets using grid layout for Expense Name
    expense_name_label = tk.Label(root, text="Enter Expense Name:")
    expense_name_label.grid(row=0, column=0, padx=10, pady=10)

    expense_name_box = tk.Entry(root, width=40)
    expense_name_box.grid(row=0, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Expense Type
    expense_type_label = tk.Label(root, text="Enter Expense Type:")
    expense_type_label.grid(row=1, column=0, padx=10, pady=10)

    expense_type_box = tk.Entry(root, width=40)
    expense_type_box.grid(row=1, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Expense Amount
    expense_amount_label = tk.Label(root, text="Enter Expense Amount:")
    expense_amount_label.grid(row=2, column=0, padx=10, pady=10)

    expense_amount_box = tk.Entry(root, width=40)
    expense_amount_box.grid(row=2, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Expense Date
    expense_date_label = tk.Label(root, text="Enter Expense Date (MM/DD/YYYY) (*Leave blank for today): ")
    expense_date_label.grid(row=3, column=0, padx=10, pady=10)

    expense_date_box = tk.Entry(root, width=40)
    expense_date_box.grid(row=3, column=1, padx=10, pady=10)

    def submit_expense():
        # Get the text from the input box
        expense_name_input = expense_name_box.get()
        expense_type_input = expense_type_box.get()
        expense_amount_input = expense_amount_box.get()
        expense_date_input = expense_date_box.get()

        if expense_date_input == '':
            expense_date_input = datetime.now().strftime("%m/%d/%Y")

        # Display the text in a label
        if expense_name_input == '':
            result_label.config(text="Expense Name is required!")

        elif expense_type_input == '':
            result_label.config(text="Expense Type is required!")

        elif expense_amount_input == '':
            result_label.config(text="Expense Amount is required!")

        else:
            addExpenseGUI(expense_name_input, expense_type_input, expense_amount_input, expense_date_input)
            result_label.config(text=f"Submission Successful! \n Expense Name: {expense_name_input} \n Expense Type: {expense_type_input} \n Expense Amount: {expense_amount_input} \n Expense Date: {expense_date_input}")

    # Create a Submit button widget
    submit_button = tk.Button(root, text="Submit", command=submit_expense)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Create a Submit label widget to display the result
    result_label = tk.Label(root, text="Input will be displayed here")
    result_label.grid(row=5, column=0, columnspan=2, pady=10)

def savingsInputDataGUI(root: tkinter.Tk) -> None:
    # Create the main window
    root = Toplevel(root)
    
    # Create Title for GUI Application
    root.title("Adding Savings Goal")

    # Create the Label and Entry widgets using grid layout for Savings Name
    expense_name_label = tk.Label(root, text="Enter Savings Name:")
    expense_name_label.grid(row=0, column=0, padx=10, pady=10)

    savings_name_box = tk.Entry(root, width=40)
    savings_name_box.grid(row=0, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Savings Type
    expense_type_label = tk.Label(root, text="Enter Savings Type:")
    expense_type_label.grid(row=1, column=0, padx=10, pady=10)

    savings_type_box = tk.Entry(root, width=40)
    savings_type_box.grid(row=1, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Savings Amount
    expense_amount_label = tk.Label(root, text="Enter Savings Amount:")
    expense_amount_label.grid(row=2, column=0, padx=10, pady=10)

    savings_amount_box = tk.Entry(root, width=40)
    savings_amount_box.grid(row=2, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Savings Start Date
    expense_date_label = tk.Label(root, text="Enter Savings Start Date (MM/DD/YYYY) (*Leave blank for today): ")
    expense_date_label.grid(row=3, column=0, padx=10, pady=10)

    savings_start_date_box = tk.Entry(root, width=40)
    savings_start_date_box.grid(row=3, column=1, padx=10, pady=10)

    # Create the Label and Entry widgets using grid layout for Savings End Date
    expense_date_label = tk.Label(root, text="Enter Savings End Date (MM/DD/YYYY) (*Leave blank for today): ")
    expense_date_label.grid(row=4, column=0, padx=10, pady=10)

    savings_end_date_box = tk.Entry(root, width=40)
    savings_end_date_box.grid(row=4, column=1, padx=10, pady=10)

    def submit_expense():
        # Get the text from the input box
        savings_name_input = savings_name_box.get()
        savings_type_input = savings_type_box.get()
        savings_amount_input = savings_amount_box.get()
        savings_start_date_input = savings_start_date_box.get()
        savings_end_date_input = savings_end_date_box.get()

        if savings_start_date_input == '':
            savings_start_date_input = datetime.now().strftime("%m/%d/%Y")

        if savings_end_date_input == '':
            savings_end_date_input = datetime.now().strftime("%m/%d/%Y")

        # Display the text in a label
        if savings_name_input == '':
            result_label.config(text="Savings Name is required!")

        elif savings_type_input == '':
            result_label.config(text="Savings Type is required!")

        elif savings_amount_input == '':
            result_label.config(text="Savings Amount is required!")

        else:
            addSavingsGoalGUI(savings_name_input, savings_type_input, savings_amount_input, savings_start_date_input, savings_end_date_input)
            result_label.config(text=f"Submission Successful! \n Savings Name: {savings_name_input} \n Savings Type: {savings_type_input} \n Savings Amount: {savings_amount_input} \n Savings Start Date: {savings_start_date_input}, \n Savings End Date: {savings_end_date_input}")

    # Create a Submit button widget
    submit_button = tk.Button(root, text="Submit", command=submit_expense)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Create a Submit label widget to display the result
    result_label = tk.Label(root, text="Input will be displayed here")
    result_label.grid(row=6, column=0, columnspan=2, pady=10)

# ---------------------------- Table Functions ---------------------------- #

def sort_column(tree, col, reverse):

    # Get all the rows (children) in the Treeview
    rows = tree.get_children('')

    # Extract the value in the selected column for each row
    row_data = []
    for child in rows:
        cell_value = tree.set(child, col)
        row_data.append((cell_value, child))

    # Define the key function for sorting
    def sort_key(item):
        value = item[0]
        if "amount" in col.lower():
            try:
                return float(value)
            
            except ValueError:
                return float('inf')  # Handle conversion errors
            
        elif "date" in col.lower():
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            
            except ValueError:
                return datetime.max  # Handle conversion errors
            
        else:
            return value.lower() if isinstance(value, str) else value

    # Sort the extracted data based on the column value
    sorted_data = sorted(row_data, key=sort_key, reverse=reverse)

    # Rearrange the sorted data in the Treeview
    for index, (val, item) in enumerate(sorted_data):
        tree.move(item, '', index)

    # Reverse the sorting order for next click
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

def convert_type(value, col):
    
    # Define the column-specific data types
    if col == "Income Amount":
        try:
            return float(value)
        
        # or handle the error as appropriate
        except ValueError:
            return float('inf')  
        
    elif col == "Income Date":
        try:
            return datetime.strptime(value, "%Y-%m-%d")
        
        # or handle the error as appropriate
        except ValueError:
            return datetime.max  

    # For string columns, return the value as is    
    else:
        return value  
    

def graphOptions(root: tkinter.Tk, type: str):

    if type == "income":

        # Create the new Toplevel window
        graph_options_window = Toplevel(root)
        graph_options_window.title("Select Graph Type")
        graph_options_window.geometry("200x200")

        # Define options for the dropdown
        options = ["Pie (Percentage Comparison)", "Bar Graph "]

        # Create a Tkinter variable to store the selected value
        selected_value = tk.StringVar(graph_options_window)

        # Default Pie Graph
        selected_value.set(options[0])

        # Create the dropdown menu with the correct parent window
        dropdown = ttk.OptionMenu(graph_options_window, selected_value, options[0], *options)
        dropdown.pack(pady=20)

        # Create a button to trigger an action when an option is selected
        select_button = tk.Button(graph_options_window, text="Select Graph", command=lambda: generateIncomeGraph(str(selected_value.get()), root))
        select_button.pack(pady=10)

    elif type == "expense":

        # Create the new Toplevel window
        graph_options_window = Toplevel(root)
        graph_options_window.title("Select Graph Type")
        graph_options_window.geometry("200x200")

        # Define options for the dropdown
        options = ["Pie (Percentage Comparison)", "Bar Graph "]

        # Create a Tkinter variable to store the selected value
        selected_value = tk.StringVar(graph_options_window)

        # Default Pie Graph
        selected_value.set(options[0])

        # Create the dropdown menu with the correct parent window
        dropdown = ttk.OptionMenu(graph_options_window, selected_value, options[0], *options)
        dropdown.pack(pady=20)

        # Create a button to trigger an action when an option is selected
        select_button = tk.Button(graph_options_window, text="Select Graph", command=lambda: generateExpenseGraph(str(selected_value.get()), root))
        select_button.pack(pady=10)

def generateIncomeGraph(graph_type: str, root: tkinter.Tk):
    data = grabIncomeTableData()

    # Dictionary to store the sums
    sums = {}

    if "pie" in graph_type.lower():
        for array in data:

            # Getting Income Type
            key = array[1]  

            # Getting the Income Amount
            value = array[2]  

            # Check if the key is already in the dictionary
            if key in sums:

                # If the Income Type is present, add the Income Amount
                sums[key] += value

            else:

                # Else, create an initial value for Income Type
                sums[key] = value

        pieGraph(sums, "Income Pie Graph")

    elif "bar" in graph_type.lower():

        # Get the current year
        current_year = datetime.now().strftime('%Y')

        for array in data:

            # Getting Income Date and format it to 'YYYY-MM'
            key = array[3].strftime('%Y-%m')

            # Getting the Income Amount
            value = array[2]

            # Check if the key is from the current year
            if key.startswith(current_year):
                # Check if the key is already in the dictionary
                if key in sums:
                    # If the Income Type is present, add the Income Amount
                    sums[key] += value
                else:
                    # Else, create an initial value for Income Type
                    sums[key] = value

        # Convert the dictionary items to a list and sort by date
        sorted_items = sorted(sums.items(), key=lambda item: datetime.strptime(item[0], '%Y-%m'))

        # Convert the sorted list of tuples back into a dictionary
        sums = dict(sorted_items)

        # Call the function to generate the bar graph
        barGraph(sums, f'Income Bar Graph for {current_year}', "Income Totals", "Income Month")

def generateExpenseGraph(graph_type: str, root: tkinter.Tk):
    data = grabExpenseTableData()

    # Dictionary to store the sums
    sums = {}

    if "pie" in graph_type.lower():
        for array in data:

            # Getting Income Type
            key = array[1]  

            # Getting the Income Amount
            value = array[2]  

            # Check if the key is already in the dictionary
            if key in sums:

                # If the Income Type is present, add the Income Amount
                sums[key] += value

            else:

                # Else, create an initial value for Income Type
                sums[key] = value

        pieGraph(sums, "Expense Pie Graph")

    elif "bar" in graph_type.lower():

        # Get the current year
        current_year = datetime.now().strftime('%Y')

        for array in data:

            # Getting Income Date and format it to 'YYYY-MM'
            key = array[3].strftime('%Y-%m')

            # Getting the Income Amount
            value = array[2]

            # Check if the key is from the current year
            if key.startswith(current_year):
                # Check if the key is already in the dictionary
                if key in sums:
                    # If the Income Type is present, add the Income Amount
                    sums[key] += value
                else:
                    # Else, create an initial value for Income Type
                    sums[key] = value

        # Convert the dictionary items to a list and sort by date
        sorted_items = sorted(sums.items(), key=lambda item: datetime.strptime(item[0], '%Y-%m'))

        # Convert the sorted list of tuples back into a dictionary
        sums = dict(sorted_items)

        # Call the function to generate the bar graph
        barGraph(sums, f'Expense Bar Graph for {current_year}', "Expense Totals", "Expense Month")

# Need to look into (WIP)
def generateExpenseAndIncomeGraph():
    
    income_data = grabIncomeTableData()
    expense_data = grabExpenseTableData()

    # Initialize dictionaries to hold income and expense sums by month
    income_by_month = defaultdict(float)
    expense_by_month = defaultdict(float)

    # Process income data
    for category, subcategory, amount, date in income_data:
        month = date.strftime('%Y-%m')
        income_by_month[month] += float(amount)

    # Process expense data
    for category, subcategory, amount, date in expense_data:
        month = date.strftime('%Y-%m')
        expense_by_month[month] += float(amount)

    # Get all unique months
    months = sorted(set(income_by_month.keys()).union(set(expense_by_month.keys())))

    # Create lists of income and expense values corresponding to the months
    income_values = [income_by_month[month] for month in months]
    expense_values = [expense_by_month[month] for month in months]

    # Set the positions and width for the bars
    bar_width = 0.4
    positions = range(len(months))

    # Calculate the differences between income and expense
    differences = [income_by_month[month] - expense_by_month[month] for month in months]

    # Plot income and expense bars
    plt.figure(figsize=(14, 7))  # Increase figure size to accommodate legend
    bars1 = plt.bar(positions, income_values, width=bar_width, label='Income', color='blue', align='center')
    bars2 = plt.bar([p + bar_width for p in positions], expense_values, width=bar_width, label='Expenses', color='red', align='center')

    # Add labels above each bar
    for bar in bars1:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', va='bottom', ha='center', color='black', fontsize=10)

    for bar in bars2:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', va='bottom', ha='center', color='black', fontsize=10)

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Monthly Income and Expenses')

    # Create custom legend handles for differences
    handles = []
    labels = []

    # Handles and labels for Income and Expenses
    handles.append(plt.Line2D([0], [0], color='blue', lw=4))
    handles.append(plt.Line2D([0], [0], color='red', lw=4))
    labels.append('Income')
    labels.append('Expenses')

    # Add custom handles and labels for differences
    for i, month in enumerate(months):
        diff_label = f'{month}: Diff - {differences[i]:.2f}'
        handles.append(plt.Line2D([0], [0], color='gray', lw=2))  # Dummy handle
        labels.append(diff_label)

    # Create the legend
    plt.legend(handles=handles, labels=labels, loc='upper left', bbox_to_anchor=(1, 1))

    # Set x-axis ticks
    plt.xticks([p + bar_width / 2 for p in positions], months)

    # Show the plot
    plt.tight_layout()  # Adjust layout to fit legend
    plt.show()
