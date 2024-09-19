from datetime import datetime
import tkinter as tk
from tkinter import Toplevel, ttk

from src.utils import sort_column


def createInputWindow(root: tk.Tk, title: str, labels: list, entries: list, submit_callback: callable) -> None:
    # Create the main window
    input_window = Toplevel(root)
    
    # Set the title of the window
    input_window.title(title)

    # Create and place the Label and Entry widgets using grid layout
    for i, (label_text, entry_var) in enumerate(zip(labels, entries)):
        label = tk.Label(input_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10)

        # Use `textvariable` to link the Entry widget to the `entry_var`
        entry = tk.Entry(input_window, textvariable=entry_var, width=40)
        entry.grid(row=i, column=1, padx=10, pady=10)

    def submit():
        # Collect data from the entries
        inputs = [entry_var.get() for entry_var in entries]
        
        # If date is empty, set it to today's date
        for i in range(len(inputs)):
            if i in {3, 4} and inputs[i] == '':  # Assuming date fields are at index 3 and 4
                inputs[i] = datetime.now().strftime("%m/%d/%Y")
        
        # Check if all required fields are filled
        missing_fields = [label for i, (label, entry_var) in enumerate(zip(labels, entries)) if inputs[i] == '' and i < 4]
        if missing_fields:
            result_label.config(text=f"{', '.join(missing_fields)} are required!")
            return
        
        # Call the provided callback function
        submit_callback(*inputs)

        # Display success message
        result_label.config(text=f"Submission Successful! \n {'\n'.join([f'{label}: {input}' for label, input in zip(labels, inputs)])}")

    # Create a Submit button widget
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Create a Submit label widget to display the result
    result_label = tk.Label(input_window, text="Input will be displayed here")
    result_label.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

def createTableGUI(root: tk.Tk, title: str, fetch_data_func: callable, columns: list) -> None:
    # Create the main window
    window = Toplevel(root)
    window.title(title)

    # Create a Treeview widget
    tree = ttk.Treeview(window)

    # Insert data
    row_entries = fetch_data_func()

    # Define the columns
    tree["columns"] = columns

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
    for col in columns:
        tree.column(col, anchor=tk.W, width=120)

    # Create headings with sorting functionality
    for col in tree["columns"]:
        tree.heading(col, text=col, anchor=tk.W, command=lambda _col=col: sort_column(tree, _col, False))

    # Insert Row Data
    for row_entry in row_entries:
        tree.insert("", tk.END, values=row_entry)

    # Add the Treeview to the window
    tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

