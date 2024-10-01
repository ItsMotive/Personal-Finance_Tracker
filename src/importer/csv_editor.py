import csv
from tkinter import filedialog, messagebox, simpledialog, ttk
import tkinter as tk


def csvEditor(root: tk.Tk):
    # Create a Toplevel window
    editor_window = tk.Toplevel(root)
    editor_window.title("CSV Editor")
    editor_window.geometry("600x400")

    # Initialize state variables
    csv_file_path = None
    entry_popup = None

    # Function to open a CSV file
    def open_csv():
        nonlocal csv_file_path
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            csv_file_path = file_path
            load_csv(file_path)

    # Function to load a CSV file into the Treeview
    def load_csv(file_path):
        with open(file_path, newline="", mode="r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            # Clear existing data
            tree.delete(*tree.get_children())
            tree["columns"] = rows[0]
            for col in rows[0]:
                tree.heading(col, text=col)

            for row in rows[1:]:
                tree.insert("", "end", values=row)

    # Function to save the CSV file
    def save_csv():
        if csv_file_path:
            with open(csv_file_path, mode="w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(tree["columns"])
                for row_id in tree.get_children():
                    row = tree.item(row_id)["values"]
                    writer.writerow(row)
            messagebox.showinfo("CSV Editor", "CSV file saved successfully!")
        else:
            messagebox.showwarning("CSV Editor", "No file is opened yet.")

    # Function to add a new row
    def add_row():
        columns = tree["columns"]
        empty_row = [""] * len(columns)
        tree.insert("", "end", values=empty_row)

    # Function to delete the selected row
    def delete_row():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
        else:
            messagebox.showwarning("CSV Editor", "No row selected to delete.")

    # Function to delete a column
    def delete_column():
        # Prompt user to select a column to delete
        selected_column = simpledialog.askstring(
            "Delete Column", "Enter the column name to delete:"
        )
        if selected_column in tree["columns"]:
            col_index = tree["columns"].index(selected_column)
            columns = list(tree["columns"])
            del columns[col_index]
            tree["columns"] = columns

            for item in tree.get_children():
                values = list(tree.item(item)["values"])
                del values[col_index]
                tree.item(item, values=values)

            # Re-create column headings
            for col in columns:
                tree.heading(col, text=col)
        else:
            messagebox.showwarning("CSV Editor", "Column not found!")

    # Function to handle double-clicks on a cell
    def on_double_click(event):
        nonlocal entry_popup

        # Identify the row and column that was clicked
        region = tree.identify_region(event.x, event.y)
        if region == "cell":
            column = tree.identify_column(event.x)
            row = tree.identify_row(event.y)
            column_index = int(column.replace("#", "")) - 1

            # Get the value in the clicked cell
            item = tree.item(row)
            cell_value = item["values"][column_index]

            # Create an Entry widget to edit the cell
            x, y, width, height = tree.bbox(row, column)
            entry_popup = tk.Entry(editor_window, width=width)
            entry_popup.place(x=x, y=y, width=width, height=height)
            entry_popup.insert(0, cell_value)
            entry_popup.focus()

            # Bind events for saving the value or canceling the edit
            entry_popup.bind("<Return>", lambda e: save_cell_edit(row, column_index))
            entry_popup.bind("<FocusOut>", lambda e: cancel_edit())

    # Function to save the edited cell value
    def save_cell_edit(row, column_index):
        nonlocal entry_popup

        # Get the new value from the Entry widget
        new_value = entry_popup.get()

        # Update the Treeview with the new value
        values = list(tree.item(row)["values"])
        values[column_index] = new_value
        tree.item(row, values=values)

        # Destroy the Entry widget after saving
        entry_popup.destroy()
        entry_popup = None

    # Function to cancel the cell edit
    def cancel_edit():
        nonlocal entry_popup

        # Destroy the Entry widget without saving
        if entry_popup:
            entry_popup.destroy()
            entry_popup = None

    # Table setup using Treeview
    tree = ttk.Treeview(editor_window, show="headings")
    tree.pack(expand=True, fill="both")

    # Add buttons
    button_frame = tk.Frame(editor_window)
    button_frame.pack(fill="x")

    open_button = tk.Button(button_frame, text="Open CSV", command=open_csv)
    open_button.pack(side="left")

    save_button = tk.Button(button_frame, text="Save CSV", command=save_csv)
    save_button.pack(side="left")

    add_row_button = tk.Button(button_frame, text="Add Row", command=add_row)
    add_row_button.pack(side="left")

    delete_row_button = tk.Button(button_frame, text="Delete Row", command=delete_row)
    delete_row_button.pack(side="left")

    delete_column_button = tk.Button(
        button_frame, text="Delete Column", command=delete_column
    )
    delete_column_button.pack(side="left")

    # Bind double-click event to edit a cell
    tree.bind("<Double-1>", on_double_click)
