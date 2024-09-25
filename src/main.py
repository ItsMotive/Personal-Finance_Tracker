import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import os
import sys

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.gui.util_gui import createEditableTable, createTableGUI
from src.utils import applyDarkTheme, centerWindow
from src.gui.savings_gui import createSavingsInputGUI
from src.gui.savings_goal_gui import createSavingsGoalInputGUI
from src.gui.expense_gui import createExpenseGraphOptions, createExpenseInputGUI
from src.gui.income_gui import createIncomeGraphOptions, createIncomeInputGUI
from DB_Setup.Database_Table_Creation_Script import createTables
from src.visualization.income_expense_graphs import generateExpenseAndIncomeGraph
from src.constants import (
    EXPENSE_TABLE_HEADERS,
    INCOME_TABLE_HEADERS,
    MODIFY_EXPENSE_TABLE_HEADERS,
    MODIFY_INCOME_TABLE_HEADERS,
    MODIFY_SAVINGS_TABLE_HEADERS,
    SAVINGS_TABLE_HEADERS,
)
from src.database.SQL_Queries import (
    SELECT_EXPENSE_QUERY,
    SELECT_INCOME_QUERY,
    SELECT_SAVINGS_QUERY,
)
from src.database.db_operations import (
    addExpenseCallback,
    addIncomeCallback,
    addSavingsCallback,
    addSavingsGoalCallback,
    grabAllDatabaseData,
    updateExpenseCallback,
    updateIncomeCallback,
    updateSavingsGoalCallback,
)

# Used for getting window size
# def get_window_size(root):
#     root.update_idletasks()  # Ensure the window has been drawn and sized
#     width = root.winfo_width()
#     height = root.winfo_height()
#     print(f"Current window size: {width}x{height}")


def main():

    # Create the main application window
    root = tk.Tk()

    # Setting Title of Application
    root.title("Personal Finance Tracker")

    # Setting Application Window Size
    window_width = 484
    window_height = 260
    centerWindow(root, window_width, window_height)

    # Load the icon
    icon_path = os.path.join("assets/icons", "app_icon.ico")
    root.iconbitmap(icon_path)

    # Configure the main window grid
    root.grid_rowconfigure(0, weight=0)  # Top empty space
    root.grid_rowconfigure(1, weight=0)  # Content area (Notebook)
    root.grid_rowconfigure(2, weight=0)  # Content area (Notebook)
    root.grid_rowconfigure(3, weight=1)  # Bottom empty space
    root.grid_rowconfigure(4, weight=0)  # Bottom empty space
    root.grid_columnconfigure(0, weight=1)  # Center horizontally

    # Create a Frame and add it to the window
    frame = ttk.Frame(root)
    frame.grid(row=1, column=0, padx=25, pady=5, sticky="nsew")

    # Configure the frame grid to expand horizontally
    frame.grid_rowconfigure(0, weight=1)  # Row for the Notebook to expand
    frame.grid_columnconfigure(0, weight=1)  # Center horizontally and allow expansion

    # Apply the dark theme
    applyDarkTheme(root)

    # Create a Notebook (tabbed interface)
    notebook = ttk.Notebook(frame)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Create frames for each tab content
    main_tab = ttk.Frame(notebook)
    income_tab = ttk.Frame(notebook)
    expense_tab = ttk.Frame(notebook)
    savings_tab = ttk.Frame(notebook)
    report_tab = ttk.Frame(notebook)

    try:
        # Load the icons
        home_icon = ImageTk.PhotoImage(
            Image.open("assets/icons/database.png").resize((20, 20))
        )
        income_icon = ImageTk.PhotoImage(
            Image.open("assets/icons/wallet.png").resize((20, 20))
        )
        expense_icon = ImageTk.PhotoImage(
            Image.open("assets/icons/receipt.png").resize((20, 20))
        )
        savings_icon = ImageTk.PhotoImage(
            Image.open("assets/icons/piggybank.png").resize((20, 20))
        )
        report_icon = ImageTk.PhotoImage(
            Image.open("assets/icons/graph.png").resize((20, 20))
        )
    except Exception as e:
        print(f"Error loading icons: {e}")
        return

    def add_tab_with_icon(frame, text, icon):
        """Adds a tab with an icon to the notebook."""
        # Create a StringVar for the tab text
        tab_text = text

        # Add the frame to the notebook with the icon and text as a compound string
        notebook.add(frame, text=tab_text)

        # Set the icon to the tab
        notebook.tab(frame, image=icon, compound="left")

    # Add tabs with icons to the notebook
    add_tab_with_icon(main_tab, "Home", home_icon)
    add_tab_with_icon(income_tab, "Income", income_icon)
    add_tab_with_icon(expense_tab, "Expense", expense_icon)
    add_tab_with_icon(savings_tab, "Savings", savings_icon)
    add_tab_with_icon(report_tab, "Reports", report_icon)

    # # Add frames to notebook as tabs
    # notebook.add(main_tab, text="Home")
    # notebook.add(income_tab, text="Income")
    # notebook.add(expense_tab, text="Expense")
    # notebook.add(savings_tab, text="Saving")
    # notebook.add(report_tab, text="Reports")

    # Configure each tab frame to center its contents
    for tab in [main_tab, income_tab, expense_tab, savings_tab, report_tab]:
        tab.grid_rowconfigure(0, weight=1)  # Top row for buttons
        tab.grid_rowconfigure(1, weight=0)  # Row for additional buttons
        tab.grid_rowconfigure(2, weight=1)  # Row for additional buttons
        tab.grid_rowconfigure(3, weight=1)  # Row for additional buttons
        tab.grid_columnconfigure(0, weight=1)  # Center horizontally
    # # ----------------------- Main Tab ----------------------- #

    # Home Page Welcome Message
    title_label = tk.Label(
        main_tab,
        text="Welcome to your Personal Finance Tracker",
        font=("Arial", 12),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
        padx=20,
        pady=10,
        relief="flat",
    )
    title_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

    # button = tk.Button(
    #     main_tab, text="Get Window Size", command=lambda: get_window_size(root)
    # )
    # button.grid(pady=20)

    # Display Income Table button
    display_db_setup_button = tk.Button(
        main_tab,
        text="Setup PostgreSQL Database",
        command=lambda: createTables(),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_db_setup_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # # ----------------------- Income Tab ----------------------- #

    # Display Income Table button
    display_income_table_button = tk.Button(
        income_tab,
        text="Display Income Table",
        command=lambda: createTableGUI(
            root,
            "Income Table",
            lambda: grabAllDatabaseData(SELECT_INCOME_QUERY),
            INCOME_TABLE_HEADERS,
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_table_button.grid(row=0, column=0, padx=5, pady=(20, 5), sticky="n")

    # Display Income Input button
    display_income_input_button = tk.Button(
        income_tab,
        text="Add Income Entry",
        command=lambda: createIncomeInputGUI(root, addIncomeCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Income Report button
    display_income_graph_button = tk.Button(
        income_tab,
        text="View Income Report",
        command=lambda: createIncomeGraphOptions(root),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # Display Income Manual Input button
    display_income_update_button = tk.Button(
        income_tab,
        text="Update Income Table",
        command=lambda: createEditableTable(
            root,
            grabAllDatabaseData(SELECT_INCOME_QUERY),
            MODIFY_INCOME_TABLE_HEADERS,
            updateIncomeCallback,
            "Income",
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_update_button.grid(row=3, column=0, padx=5, pady=5, sticky="n")

    # ----------------------- Expense Tab ----------------------- #

    # Display Expense Table button
    display_expense_table_button = tk.Button(
        expense_tab,
        text="Display Expense Table",
        command=lambda: createTableGUI(
            root,
            "Expense Table",
            lambda: grabAllDatabaseData(SELECT_EXPENSE_QUERY),
            EXPENSE_TABLE_HEADERS,
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_table_button.grid(row=0, column=0, padx=5, pady=(20, 5), sticky="n")

    # Display Expense Input button
    display_expense_input_button = tk.Button(
        expense_tab,
        text="Add Expense Entry",
        command=lambda: createExpenseInputGUI(root, addExpenseCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Expense Report button
    display_expense_graph_button = tk.Button(
        expense_tab,
        text="View Expense Report",
        command=lambda: createExpenseGraphOptions(root),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_graph_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # Display Expense Manual Input button
    display_expense_update_button = tk.Button(
        expense_tab,
        text="Update Expense Table",
        command=lambda: createEditableTable(
            root,
            grabAllDatabaseData(SELECT_EXPENSE_QUERY),
            MODIFY_EXPENSE_TABLE_HEADERS,
            updateExpenseCallback,
            "Expense",
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_expense_update_button.grid(row=3, column=0, padx=5, pady=5, sticky="n")

    # ----------------------- Savings Tab ----------------------- #

    # Display Savings Goal Table button
    display_savings_goal_table_button = tk.Button(
        savings_tab,
        text="Display Savings Table",
        command=lambda: createTableGUI(
            root,
            "Income Table",
            lambda: grabAllDatabaseData(SELECT_SAVINGS_QUERY),
            SAVINGS_TABLE_HEADERS,
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_goal_table_button.grid(
        row=0, column=0, padx=5, pady=(20, 5), sticky="n"
    )

    # Display Savings Goal Input button
    display_savings_goal_input_button = tk.Button(
        savings_tab,
        text="Add Savings Goal Entry",
        command=lambda: createSavingsGoalInputGUI(root, addSavingsGoalCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_goal_input_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Input button
    display_savings_goal_input_button = tk.Button(
        savings_tab,
        text="Add Savings Entry",
        command=lambda: createSavingsInputGUI(root, addSavingsCallback),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_goal_input_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Report button
    display_savings_graph_button = tk.Button(
        savings_tab,
        text="View Savings Report",
        command=lambda: print("WIP"),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_graph_button.grid(row=3, column=0, padx=5, pady=5, sticky="n")

    # Display Savings Manual Input button
    display_savings_update_button = tk.Button(
        savings_tab,
        text="Update Savings Goal Table",
        command=lambda: createEditableTable(
            root,
            grabAllDatabaseData(SELECT_SAVINGS_QUERY),
            MODIFY_SAVINGS_TABLE_HEADERS,
            updateSavingsGoalCallback,
            "SavingsGoal",
        ),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_savings_update_button.grid(
        row=4, column=0, padx=5, pady=(5, 20), sticky="n"
    )

    # ----------------------- Reports Tab ----------------------- #

    # Display Comparison Table button
    display_income_expense_comparison_button = tk.Button(
        report_tab,
        text="Display Income vs Expense Report",
        command=lambda: generateExpenseAndIncomeGraph(),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_expense_comparison_button.grid(
        row=0, column=0, padx=5, pady=(20, 5), sticky="n"
    )

    # ----------------------- Other ----------------------- #

    # Bind closing event of the main window to close all windows
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    # Run the application
    root.mainloop()


# Call the main function to start the application
if __name__ == "__main__":
    main()
