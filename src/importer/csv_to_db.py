import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from src.database.SQL_Queries import (
    EXPENSE_TABLE_NAME,
    INCOME_TABLE_NAME,
    SAVING_GOALS_TABLE_NAME,
    SAVINGS_TABLE_NAME,
    addExpenseQuery,
    addIncomeQuery,
    addSavingsGoalQuery,
    addSavingsQuery,
)
from src.database.db_operations import DB_Connection
from src.importer.csv_util import (
    getExpenseData,
    getIncomeData,
    getSavingGoalData,
    getSavingsData,
)


def importToDatabase(root: tk.Tk):
    """
    Imports data from a CSV file into a PostgreSQL database.

    Args:
        importer_window (tk.Tk): The importer_window window.
    """

    # Create a Toplevel window
    importer_window = tk.Toplevel(root)
    importer_window.title("CSV Importer")
    importer_window.geometry("200x200")

    importer_window.grid_columnconfigure(0, weight=1)

    # Dictionary mapping user-friendly table names to actual table names
    table_config = {
        "Expense": {
            "table_name": EXPENSE_TABLE_NAME,
            "insert_query": addExpenseQuery(),
            "data_function": getExpenseData,
        },
        "Income": {
            "table_name": INCOME_TABLE_NAME,
            "insert_query": addIncomeQuery(),
            "data_function": getIncomeData,
        },
        "Saving Goals": {
            "table_name": SAVING_GOALS_TABLE_NAME,
            "insert_query": addSavingsGoalQuery(),
            "data_function": getSavingGoalData,
        },
        "Savings": {
            "table_name": SAVINGS_TABLE_NAME,
            "insert_query": addSavingsQuery(),
            "data_function": getSavingsData,
        },
    }

    def select_csv_file():
        return filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    def getTableName():
        return table_dropdown.get()

    def import_data():
        csv_file = select_csv_file()

        selected_table = getTableName()

        try:
            actual_table_name = table_config[selected_table]["table_name"]

        except Exception as e:
            messagebox.showerror("Error", "Invalid Table Selection!")

        query = table_config[selected_table]["insert_query"]

        if not csv_file:
            messagebox.showwarning("Warning", "No CSV file selected.")
            return

        if not actual_table_name:
            messagebox.showwarning("Warning", "No table name selected.")
            return

        try:

            # Establish a connection to the PostgreSQL database
            conn, cur = DB_Connection()

            # Open the CSV file and read its content
            with open(csv_file, mode="r", newline="") as infile:
                reader = csv.DictReader(infile)

                # Loop through the rows in the CSV
                for row in reader:

                    # Extract the columns in the correct order for the DB table
                    data = table_config[selected_table]["data_function"](row)

                    # Execute the query
                    cur.execute(query, data)

            # Commit the transaction
            conn.commit()
            cur.close()
            conn.close()

            messagebox.showinfo(
                "Success",
                f"Data from {csv_file} imported into {selected_table} successfully.",
            )

        except Exception as e:
            messagebox.showerror("Error", str(f"Missing: {e}"))

    # Create and set up the dropdown for table selection
    table_label = tk.Label(importer_window, text="CSV to Database")
    table_label.grid(row=0, column=0, padx=5, pady=(20, 0), sticky="n")

    # Create a Combobox
    table_dropdown = ttk.Combobox(
        importer_window,
        values=list(table_config.keys()),
        state="readonly",
    )
    table_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky="n")
    table_dropdown.set("Select a Table")  # Set a default value

    # Create the import button
    import_button = tk.Button(
        importer_window, text="Import CSV to Postgres", command=import_data
    )
    import_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    requirements_button = tk.Button(
        importer_window,
        text="Requirements",
        command=lambda: messagebox.showinfo(
            "Requirements",
            (
                "Income/Expense Required Headers:\n"
                "  - Name\n"
                "  - Type\n"
                "  - Amount\n"
                "  - Date\n\n"
                "Saving Goals Required Headers:\n"
                "  - Name\n"
                "  - Type\n"
                "  - Start_Date\n"
                "  - End_Date\n"
                "  - Status\n\n"
                "Savings Required Headers:\n"
                "  - Name\n"
                "  - Amount\n"
                "  - Date"
            ),
        ),
    )
    requirements_button.grid(row=3, column=0, padx=5, pady=(5, 20), sticky="n")
