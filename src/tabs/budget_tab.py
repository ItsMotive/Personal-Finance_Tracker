import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.visualization.income_expense_graphs import generateExpenseAndIncomeGraph


def createBudgetTab(notebook: ttk.Notebook, root: tk.Tk):

    budget_tab = ttk.Frame(notebook)

    budget_icon = ImageTk.PhotoImage(
        Image.open("assets/icons/graph.png").resize((20, 20))
    )

    budget_tab.expense_icon = budget_icon

    notebook.add(budget_tab, text="Budget")
    notebook.tab(budget_tab, image=budget_icon, compound="left")

    budget_tab.grid_columnconfigure(0, weight=1)  # Centers elements in the center

    # Display Comparison Table button
    display_income_expense_comparison_button = tk.Button(
        budget_tab,
        text="Display Income vs Expense Report",
        command=lambda: generateExpenseAndIncomeGraph(root),
        fg="white",
        bg="#3e3e3e",
        activebackground="#1e1e1e",
    )
    display_income_expense_comparison_button.grid(
        row=0, column=0, padx=5, pady=(20, 5), sticky="n"
    )
