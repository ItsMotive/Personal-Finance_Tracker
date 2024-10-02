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

            if not rows:
                messagebox.showwarning("CSV Editor", "The CSV file is empty.")
                return

            # Clear existing data
            tree.delete(*tree.get_children())
            tree["columns"] = rows[0] if rows else []
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

            for col in columns:
                tree.heading(col, text=col)
        else:
            messagebox.showwarning("CSV Editor", "Column not found!")

    # Function to handle double-clicks on a cell
    def on_double_click(event):
        nonlocal entry_popup

        region = tree.identify_region(event.x, event.y)
        if region == "cell":
            column = tree.identify_column(event.x)
            row = tree.identify_row(event.y)
            column_index = int(column.replace("#", "")) - 1

            item = tree.item(row)
            cell_value = item["values"][column_index]

            x, y, width, height = tree.bbox(row, column)
            entry_popup = tk.Entry(editor_window, width=width)
            entry_popup.place(x=x, y=y, width=width, height=height)
            entry_popup.insert(0, cell_value)
            entry_popup.focus()

            entry_popup.bind("<Return>", lambda e: save_cell_edit(row, column_index))
            entry_popup.bind("<FocusOut>", lambda e: cancel_edit())

        elif region == "heading":
            column = tree.identify_column(event.x)
            column_index = int(column.replace("#", "")) - 1
            edit_column_header(column_index)

    # Function to edit a column header
    def edit_column_header(column_index):
        nonlocal entry_popup

        # Ensure the column index is valid
        columns = tree["columns"]
        if column_index < 0 or column_index >= len(columns):
            messagebox.showwarning("CSV Editor", "Invalid column index!")
            return

        # Get the first row to determine the bounding box for the specified column
        first_row = tree.get_children()[0] if tree.get_children() else None
        if first_row is None:
            messagebox.showwarning(
                "CSV Editor", "No data available to edit column header."
            )
            return

        # Get the bounding box for the first row and the specified column
        try:
            bbox = tree.bbox(first_row, column=f"#{column_index + 1}")
            if bbox:
                x, y, width, height = bbox

                # Adjust the x coordinate and width to fit better
                x -= 1  # Move left by 1 pixel (adjust as needed)
                width -= 2  # Reduce width by 2 pixels to prevent going too far

                # Create an Entry widget to edit the column header
                entry_popup = tk.Entry(editor_window, width=width)
                entry_popup.place(x=x, y=y, width=width, height=height)
                entry_popup.insert(0, tree.heading(columns[column_index])["text"])
                entry_popup.focus()

                # Bind events for saving the new header or canceling the edit
                entry_popup.bind(
                    "<Return>", lambda e: save_column_header_edit(column_index)
                )
                entry_popup.bind("<FocusOut>", lambda e: cancel_edit())
            else:
                messagebox.showwarning(
                    "CSV Editor", "Unable to determine the bounding box for the column."
                )
        except tk.TclError:
            messagebox.showwarning(
                "CSV Editor", f"Column index {column_index} out of bounds."
            )

    # Function to save the edited column header
    def save_column_header_edit(column_index):
        nonlocal entry_popup

        if column_index < 0 or column_index >= len(tree["columns"]):
            messagebox.showwarning("CSV Editor", "Invalid column index!")
            return

        new_column_name = entry_popup.get()
        columns = list(tree["columns"])
        columns[column_index] = new_column_name
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col)

        entry_popup.destroy()
        entry_popup = None

    # Function to save the edited cell value
    def save_cell_edit(row, column_index):
        nonlocal entry_popup

        new_value = entry_popup.get()
        values = list(tree.item(row)["values"])
        values[column_index] = new_value
        tree.item(row, values=values)

        entry_popup.destroy()
        entry_popup = None

    # Function to cancel the cell or header edit
    def cancel_edit():
        nonlocal entry_popup
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

    # Bind double-click event to edit a cell or column header
    tree.bind("<Double-1>", on_double_click)
