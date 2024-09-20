from collections import defaultdict
from datetime import datetime
import tkinter as tk
from tkinter import Toplevel, ttk
import tkinter
from matplotlib import pyplot as plt

import os
import sys

# Add the parent directory of Step_2 to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database.SQL_Queries import SELECT_EXPENSE_QUERY, SELECT_INCOME_QUERY
from src.database.db_operations import grabAllDatabaseData
from src.visualization.Graphs import pieGraph, barGraph

# ---------------------------- Table Functions ---------------------------- #

def generateGraph(graph_type: str, root: tk.Tk, data_query: str, title_prefix: str, pie_title: str, bar_title: str):
    # Grab data from the database using the provided query
    data = grabAllDatabaseData(data_query)

    # Dictionary to store the sums
    sums = {}

    if "pie" in graph_type.lower():
        for array in data:
            # Getting the category (Income Type or Expense Type)
            key = array[1]  

            # Getting the amount (Income Amount or Expense Amount)
            value = array[2]  

            # Update the dictionary with sums
            if key in sums:
                sums[key] += value
            else:
                sums[key] = value

        # Generate the pie graph
        pieGraph(sums, pie_title)

    elif "bar" in graph_type.lower():
        # Get the current year
        current_year = datetime.now().strftime('%Y')

        for array in data:
            # Getting the date and format it to 'YYYY-MM'
            key = array[3].strftime('%Y-%m')

            # Getting the amount (Income Amount or Expense Amount)
            value = array[2]

            # Check if the key is from the current year
            if key.startswith(current_year):
                # Update the dictionary with sums
                if key in sums:
                    sums[key] += value
                else:
                    sums[key] = value

        # Convert the dictionary items to a list and sort by date
        sorted_items = sorted(sums.items(), key=lambda item: datetime.strptime(item[0], '%Y-%m'))
        sums = dict(sorted_items)

        # Generate the bar graph
        barGraph(sums, f'{bar_title} for {current_year}', f'{title_prefix} Totals', f'{title_prefix} Month')


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
    data = grabAllDatabaseData(SELECT_INCOME_QUERY)

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
    data = grabAllDatabaseData(SELECT_EXPENSE_QUERY)

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
        barGraph(sums, f'Expense Bar Graph for {current_year}', "Expense Month", "Expense Totals")

# Need to look into (WIP)
def generateExpenseAndIncomeGraph():
    
    income_data = grabAllDatabaseData(SELECT_INCOME_QUERY)
    expense_data = grabAllDatabaseData(SELECT_EXPENSE_QUERY)

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
