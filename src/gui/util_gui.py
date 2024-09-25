import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import messagebox

from src.utils import (
    convertToTwoDecimals,
    sortColumn,
    validateInput,
)


def show_error_popup(error: str) -> None:
    # This function will trigger the error popup
    messagebox.showerror("Error", error)


def createTableGUI(
    root: tk.Tk, title: str, fetch_data_func: callable, columns: list
) -> None:

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
            tree.heading(
                col,
                text=col,
                anchor=tk.W,
                command=lambda _col=col: sortColumn(tree, _col, False),
            )

        # Insert Row Data
        for row_entry in row_entries:
            tree.insert("", tk.END, values=row_entry)

        # Create vertical scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        # Use grid to position Treeview and scrollbar
        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        # Configure the frame to expand
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    except Exception as e:
        show_error_popup(e)


def createEditableTable(
    root: tk.Tk, data: list, columns: list, update_data_func: callable, table_type: str
) -> ttk.Treeview:

    try:
        # Get data
        row_entries = data

        # Create the main window
        window = Toplevel(root)
        window.title(f"Manual Table Editor - {table_type}")

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
            tree.heading(
                col,
                text=col,
                anchor=tk.W,
                command=lambda _col=col: sortColumn(tree, _col, False),
            )

        # Insert Row Data
        for row_entry in row_entries:
            tree.insert("", tk.END, values=row_entry)

        # Create vertical scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        # Use grid to position Treeview and scrollbar
        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        # Configure the frame to expand
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Bind double-click to editing a cell
        tree.bind(
            "<Double-1>",
            lambda event: updateTableGUI(
                event, tree, root, update_data_func, columns, table_type
            ),
        )

        return tree

    except Exception as e:
        show_error_popup(e)


def updateTableGUI(
    event: tk.Event,
    tree: ttk.Treeview,
    root: tk.Tk,
    update_data_func: callable,
    columns: list,
    table_type: str,
) -> None:
    selected_item = tree.focus()  # Get the selected row
    item_values = tree.item(
        selected_item, "values"
    )  # Get the values of the selected row

    col_index = tree.identify_column(event.x)[-1]  # Identify the clicked column index

    def update_value(new_value):
        new_value = convertToTwoDecimals(new_value)
        # Call the update callback with the necessary arguments based on the table type
        updateDatabase(
            item_values,
            col_index,
            new_value,
            columns,
            tree,
            selected_item,
            col_index,
            update_data_func,
            table_type,
        )
        popup.destroy()

    # Create a pop-up window to get the new value
    popup = tk.Toplevel(root)
    popup.title("Update Value")

    entry = tk.Entry(popup)
    entry.insert(0, item_values[int(col_index) - 1])  # Get the current value
    entry.pack(padx=10, pady=10)

    # Add a button to save the new value
    save_button = tk.Button(
        popup, text="Save", command=lambda: update_value(entry.get())
    )
    save_button.pack(pady=5)


def updateDatabase(
    row_values,
    column_index,
    new_value,
    columns,
    tree,
    selected_item,
    col_index,
    update_data_func: callable,
    table_type: str,
) -> None:

    column_name = columns[int(column_index) - 1]  # Get the column name
    success = False

    # Validate the input using the general validation function
    if not validateInput(column_name, new_value):
        return  # Exit if validation fails

    if table_type in ["Income", "Expense"]:

        # Both income and expense tables have the same structure
        name_value, amount_value, date_value = (
            row_values[0],
            row_values[2],
            row_values[3],
        )
        success = update_data_func(
            column_name, new_value, name_value, amount_value, date_value
        )

    elif table_type == "SavingsGoal":

        # For savings goal table with more fields
        (
            name_value,
            type_value,
            amount_value,
            start_date_value,
            end_date_value,
            status_value,
        ) = row_values[0:6]

        success = update_data_func(
            column_name,
            new_value,
            name_value,
            type_value,
            amount_value,
            start_date_value,
            end_date_value,
            status_value,
        )

    elif table_type == "Savings":

        # For savings goal table with more fields
        (
            name_value,
            amount_value,
            date_value,
        ) = row_values[0:3]

        success = update_data_func(
            column_name,
            new_value,
            name_value,
            amount_value,
            date_value,
        )

    # Update the GUI table if the database update succeeded
    if success:
        tree.set(selected_item, column=str(int(col_index) - 1), value=new_value)
        messagebox.showinfo(
            "Update Successful",
            f"Updated Column '{column_name}' to new value: {new_value}",
        )
    else:
        messagebox.showerror(
            "Database Error", "Failed to update the database. Please try again."
        )
