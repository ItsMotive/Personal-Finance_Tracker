from tkinter import ttk
import tkinter as tk

import os
import sys

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tabs.budget_tab import createBudgetTab
from src.tabs.expense_tab import createExpenseTab
from src.tabs.home_tab import createHomeTab
from src.tabs.income_tab import createIncomeTab
from src.tabs.savings_goal_tab import createSavingGoalsTab
from src.tabs.savings_tab import createSavingsTab
from src.utils import applyDarkTheme, centerWindow


def main():

    # Create the main application window
    root = tk.Tk()

    # Setting Title of Application
    root.title("Personal Finance Tracker")

    # Setting Application Window Size
    window_width = 605
    window_height = 235
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

    # Create tabs
    createHomeTab(notebook, root)
    createIncomeTab(notebook, root)
    createExpenseTab(notebook, root)
    createSavingGoalsTab(notebook, root)
    createSavingsTab(notebook, root)
    createBudgetTab(notebook, root)

    # Bind window close event
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()
