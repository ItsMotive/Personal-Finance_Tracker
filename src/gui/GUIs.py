from datetime import datetime
import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import messagebox

from src.utils import convertToTwoDecimals, sortColumn

def show_error_popup(error: str) -> None:
    # This function will trigger the error popup
    messagebox.showerror("Error", error)

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

    try: 
        # Get data
        row_entries = fetch_data_func()

        # Create the main window
        window = Toplevel(root)
        window.title(title)

        # Create a frame to hold the Treeview and Scrollbar
        frame = ttk.Frame(window)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create the Treeview widget
        tree = ttk.Treeview(frame)

        # Define the columns
        tree["columns"] = columns

        # Format columns
        tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
        for col in columns:
            tree.column(col, anchor=tk.W, width=120)

        # Create headings with sorting functionality
        for col in tree["columns"]:
            tree.heading(col, text=col, anchor=tk.W, command=lambda _col=col: sortColumn(tree, _col, False))

        # Insert Row Data
        for row_entry in row_entries:
            tree.insert("", tk.END, values=row_entry)

        # Create vertical scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        # Use grid to position Treeview and scrollbar
        tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')

        # Configure the frame to expand
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    except Exception as e:
        show_error_popup(e)

def inputDataToTable(root: tk.Tk, label: list, gui_title: str, func: callable) -> None:
    entries = [tk.StringVar() for _ in label]
    createInputWindow(root, gui_title, label, entries, func)

def createEditableTable(root: tk.Tk, data: list, columns: list, update_data_func: callable) -> ttk.Treeview:

    try: 
        # Get data
        row_entries = data

        # Create the main window
        window = Toplevel(root)
        window.title("Manual Table Editor")

        # Create a frame to hold the Treeview and Scrollbar
        frame = ttk.Frame(window)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create the Treeview widget
        tree = ttk.Treeview(frame)

        # Define the columns
        tree["columns"] = columns

        # Format columns
        tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
        for col in columns:
            tree.column(col, anchor=tk.W, width=120)

        # Create headings with sorting functionality
        for col in tree["columns"]:
            tree.heading(col, text=col, anchor=tk.W, command=lambda _col=col: sortColumn(tree, _col, False))

        # Insert Row Data
        for row_entry in row_entries:
            tree.insert("", tk.END, values=row_entry)

        # Create vertical scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        # Use grid to position Treeview and scrollbar
        tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')

        # Configure the frame to expand
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Bind double-click to editing a cell
        tree.bind("<Double-1>", lambda event: updateTableGUI(event, tree, root, update_data_func, columns))

        return tree

    except Exception as e:
        show_error_popup(e)

def updateTableGUI(event: tk.Event, tree: ttk.Treeview, root: tk.Tk, update_data_func: callable, columns: list) -> None:
    selected_item = tree.focus()  # Get the selected row
    item_values = tree.item(selected_item, 'values')  # Get the values of the selected row
    
    col_index = tree.identify_column(event.x)[-1]  # Identify the clicked column index

    def update_value(new_value):

        new_value = convertToTwoDecimals(new_value)

        # Call the update callback to update the database and conditionally update the GUI
        updateDatabase(item_values, col_index, new_value, columns, tree, selected_item, col_index, update_data_func)
        
        popup.destroy()

    # Create a pop-up window to get the new value
    popup = tk.Toplevel(root)
    popup.title("Update Value")

    entry = tk.Entry(popup)
    entry.insert(0, item_values[int(col_index) - 1])  # Get the current value
    entry.pack(padx=10, pady=10)

    # Add a button to save the new value
    save_button = tk.Button(popup, text="Save", command=lambda: update_value(entry.get()))
    save_button.pack(pady=5)

def updateDatabase(row_values, column_index, new_value, columns, tree, selected_item, col_index, update_data_func: callable) -> None:

    column_name = columns[int(column_index) - 1]  # Get the column name

    # Extract the name, amount, and date values from the row
    name_value = row_values[0]
    amount_value = row_values[2]
    date_value = row_values[3]

    # Attempt to update the database
    success = update_data_func(column_name, new_value, name_value, amount_value, date_value)

    if success:
        # Update the GUI table if the database update succeeded
        tree.set(selected_item, column=str(int(col_index) - 1), value=new_value)
        messagebox.showinfo("Update Successful", f"Updated Row: \nName = {name_value}, \nAmount = {amount_value}, \nDate = {date_value}, \nColumn '{column_name}' to new value: {new_value}")

    else:
        messagebox.showerror("Database Error", "Failed to update the database. Please try again.")