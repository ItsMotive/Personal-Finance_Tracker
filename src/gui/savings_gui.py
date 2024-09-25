from datetime import datetime
import tkinter as tk

from src.constants import SAVINGS_TABLE_LABEL
from src.database.SQL_Queries import SELECT_UNIQUE_SAVINGS_GOAL_QUERY
from src.database.db_operations import grabAllDatabaseData
from src.utils import flatTuple, isFloat, isValidDate


def createSavingsInputGUI(root: tk.Tk, submit_callback: callable) -> None:

    goal_options = flatTuple(grabAllDatabaseData(SELECT_UNIQUE_SAVINGS_GOAL_QUERY))

    # Create the main window
    input_window = tk.Toplevel(root)

    # Set the title of the window
    input_window.title("Savings Entry Form")

    labels = SAVINGS_TABLE_LABEL

    entries = [tk.StringVar() for _ in labels]

    for i, (label_text, entry_var) in enumerate(zip(labels, entries)):
        label = tk.Label(input_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10)

        if i == 0:  # First input as a dropdown (OptionMenu)
            # Create the dropdown menu
            dropdown = tk.OptionMenu(input_window, entry_var, *goal_options)
            dropdown.config(width=37)  # Adjust width of dropdown
            dropdown.grid(row=i, column=1, padx=10, pady=10)

        else:  # Other inputs as normal Entry widgets
            entry = tk.Entry(input_window, textvariable=entry_var, width=40)
            entry.grid(row=i, column=1, padx=10, pady=10)

    def submit():

        # Initialize an empty list to store missing field labels
        missing_fields = []

        # Collect data from the entries
        inputs = [entry_var.get() for entry_var in entries]

        print(f"Collected inputs: {inputs}")  # Add debug print for inputs

        # If date is empty, set it to today's date
        if inputs[2] == "":
            inputs[2] = datetime.now().strftime("%m/%d/%Y")

        else:
            if not isValidDate(inputs[2]):
                missing_fields.append(labels[2] + " Must be a valid Date")

        # Validate Amount Input Field
        if not isFloat(inputs[1]):
            missing_fields.append(labels[1] + " Must be a valid Amount")

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
