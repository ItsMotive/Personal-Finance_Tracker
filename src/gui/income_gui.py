from datetime import datetime
import tkinter as tk
from tkinter import ttk

from src.constants import INCOME_TABLE_LABEL
from src.utils import convertToTwoDecimals, isFloat, isValidDate
from src.visualization.income_graphs import incomeBarGraph, incomePieGraph


def createIncomeGraphOptions(root: tk.Tk):
    # Create the new Toplevel window
    graph_options_window = tk.Toplevel(root)
    graph_options_window.title("Select Graph Type")
    graph_options_window.geometry("200x200")

    # Define options for the dropdown
    options = ["Pie (Percentage Comparison)", "Bar Graph"]

    # Create a Tkinter variable to store the selected value
    selected_value = tk.StringVar(graph_options_window)

    # Default Pie Graph
    selected_value.set(options[0])

    # Create the dropdown menu with the correct parent window
    dropdown = ttk.OptionMenu(
        graph_options_window, selected_value, options[0], *options
    )
    dropdown.pack(pady=20)

    # Function to be triggered when the select button is clicked
    def onSelect():
        choice = selected_value.get()  # Get the current selected option
        if choice == "Pie (Percentage Comparison)":
            # Call function for pie chart
            incomePieGraph(root)  # This function should generate the pie graph
        elif choice == "Bar Graph":
            # Call function for bar graph
            incomeBarGraph(root)  # This function should generate the bar graph
        else:
            print("Unknown option selected")

    # Create a button to trigger an action when an option is selected
    select_button = tk.Button(
        graph_options_window,
        text="Select Graph",
        command=onSelect,  # Use the local function on_select
    )
    select_button.pack(pady=10)


def createIncomeInputGUI(root: tk.Tk, submit_callback: callable) -> None:

    # Create the main window
    input_window = tk.Toplevel(root)

    # Set the title of the window
    input_window.title("Income Entry Form")

    labels = INCOME_TABLE_LABEL

    entries = [tk.StringVar() for _ in labels]

    for i, (label_text, entry_var) in enumerate(zip(labels, entries)):
        label = tk.Label(input_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10)

        # Use `textvariable` to link the Entry widget to the `entry_var`
        entry = tk.Entry(input_window, textvariable=entry_var, width=40)
        entry.grid(row=i, column=1, padx=10, pady=10)

    def submit():

        # Initialize an empty list to store missing field labels
        missing_fields = []

        # Collect data from the entries
        inputs = [entry_var.get() for entry_var in entries]

        # If date is empty, set it to today's date
        if inputs[3] == "":
            inputs[3] = datetime.now().strftime("%m/%d/%Y")

        else:
            if not isValidDate(inputs[3]):
                missing_fields.append(labels[3] + " Must be a valid Date")

        # Validate Amount Input Field
        if not isFloat(inputs[2]):
            missing_fields.append(labels[2] + " Must be a valid Amount")

        else:
            inputs[2] = convertToTwoDecimals(inputs[2])

        # Iterate over the labels and entries together with their index
        for index, (label, entry_var) in enumerate(zip(labels, entries)):

            # Check if the current input is empty and if it's not the last field
            if inputs[index] == "" and index < len(labels) - 1:

                # If both conditions are met, add the label to the missing_fields list
                missing_fields.append(label)

        if missing_fields:
            result_label.config(text=f"{'\n(REQUIRED) '.join(missing_fields)}")
            return

        # Call the provided callback function
        submit_callback(*inputs)

        # Display success message
        result_label.config(
            text=f"Submission Successful! \n {'\n'.join([f'{label}: {input}' for label, input in zip(labels, inputs)])}"
        )

    # Create a Submit button widget
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Create a Submit label widget to display the result
    result_label = tk.Label(input_window, text="Input will be displayed here")
    result_label.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)
