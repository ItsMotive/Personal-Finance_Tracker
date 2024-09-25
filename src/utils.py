from datetime import datetime
from tkinter import messagebox, ttk


# Sorting Columns inside GUI Table
def sortColumn(tree, col, reverse):

    # Get all the rows (children) in the Treeview
    rows = tree.get_children("")

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
                return float("inf")  # Handle conversion errors

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
        tree.move(item, "", index)

    # Reverse the sorting order for next click
    tree.heading(col, command=lambda: sortColumn(tree, col, not reverse))


def convertToTwoDecimals(value):
    """
    Attempts to convert the input value to a float rounded to two decimal places.
    Returns the formatted value as a string with two decimal places if conversion is successful.
    Returns string if value is unable to convert to float
    """
    try:
        # Convert to float and round to two decimal places
        float_value = float(value)
        formatted_value = f"{float_value:.2f}"
        return formatted_value

    except ValueError:
        # Return None or an error message if conversion fails
        return value


def isString(value: str) -> bool:
    return isinstance(value, str) and bool(value.strip())


def isFloat(value: str) -> bool:
    try:
        float(value)
        return True

    except ValueError:
        return False


def isValidDate(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True

    except ValueError:
        return False


def isValidStatus(value: str) -> bool:
    try:
        if value in ["Active", "Inactive"]:
            return True

    except ValueError:
        return False


def validateInput(column_name: str, new_value: str) -> bool:
    # Define validation rules for different columns
    validation_rules = {
        "name": (isString, "Name must be a non-empty string."),
        "source": (isString, "Source must be a non-empty string."),
        "amount": (isFloat, "Amount must be a valid float."),
        "date": (isValidDate, "Date must be in YYYY-MM-DD format."),
        "goal": (isString, "Goal must be a non-empty string."),
        "goal_type": (isString, "Goal Type must be a non-empty string."),
        "goal_amount": (isFloat, "Goal Amount must be a valid float."),
        "start_date": (isValidDate, "Start Date must be in YYYY-MM-DD format."),
        "end_date": (isValidDate, "End Date must be in YYYY-MM-DD format."),
        "status": (isValidStatus, "Status must be 'Inactive' or 'Active'"),
    }

    # Check if the column name is in the validation rules
    if column_name in validation_rules:
        validator, error_message = validation_rules[column_name]
        if not validator(new_value):
            messagebox.showerror("Input Error", error_message)
            return False

    return True  # Input is valid


def applyDarkTheme(root):
    style = ttk.Style(root)
    # Use 'clam' theme which can be fully customized
    style.theme_use("clam")

    # Modify background and foreground colors
    style.configure("TFrame", background="#2b2b2b")  # Dark background
    style.configure("TNotebook", background="#2b2b2b", borderwidth=0)
    style.configure(
        "TNotebook.Tab",
        background="#4e4e4e",  # Tab background color
        foreground="white",  # Text color
        padding=[10, 5],
        borderwidth=0,
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", "#1e1e1e")],  # Active tab background
        foreground=[("selected", "white")],  # Active tab text color
    )
    style.configure("TLabel", background="#2b2b2b", foreground="white")
    style.configure("TButton", background="#4e4e4e", foreground="white")
    style.map("TButton", background=[("active", "#1e1e1e")])

    # Ensure all elements use dark backgrounds
    root.configure(bg="#2b2b2b")


def centerWindow(window, width, height):
    """Centers the Tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def flatTuple(data: tuple):
    return tuple(item[0] for item in data)
