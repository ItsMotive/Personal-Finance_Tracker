from collections import defaultdict
from matplotlib import pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from src.database.SQL_Queries import SELECT_EXPENSE_QUERY, SELECT_INCOME_QUERY
from src.database.db_operations import grabAllDatabaseData

# ---------------------------- Table Functions ---------------------------- #


# Need to look into (WIP)
def generateExpenseAndIncomeGraph(root: tk.Tk):
    income_data = grabAllDatabaseData(SELECT_INCOME_QUERY)
    expense_data = grabAllDatabaseData(SELECT_EXPENSE_QUERY)

    # Initialize dictionaries to hold income and expense sums by month
    income_by_month = defaultdict(float)
    expense_by_month = defaultdict(float)

    # Process income data
    for category, subcategory, amount, date in income_data:
        month = date.strftime("%Y-%m")
        income_by_month[month] += float(amount)

    # Process expense data
    for category, subcategory, amount, date in expense_data:
        month = date.strftime("%Y-%m")
        expense_by_month[month] += float(amount)

    # Get all unique months
    months = sorted(set(income_by_month.keys()).union(set(expense_by_month.keys())))

    # Create lists of income and expense values corresponding to the months
    income_values = [income_by_month[month] for month in months]
    expense_values = [expense_by_month[month] for month in months]

    # Set the positions and width for the bars
    bar_width = 0.4
    positions = range(len(months))

    # Calculate the differences between income and expense
    differences = [income_by_month[month] - expense_by_month[month] for month in months]

    # Create a new Toplevel window for the graph
    graph_window = tk.Toplevel(root)
    graph_window.title("Monthly Income and Expenses")

    # Create a matplotlib figure
    fig, ax = plt.subplots(
        figsize=(14, 7)
    )  # Increase figure size to accommodate legend

    # Plot income and expense bars
    bars1 = ax.bar(
        positions,
        income_values,
        width=bar_width,
        label="Income",
        color="blue",
        align="center",
    )

    bars2 = ax.bar(
        [p + bar_width for p in positions],
        expense_values,
        width=bar_width,
        label="Expenses",
        color="red",
        align="center",
    )

    # Add labels above each bar
    for bar in bars1:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval,
            f"{yval:.2f}",
            va="bottom",
            ha="center",
            color="black",
            fontsize=10,
        )

    for bar in bars2:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval,
            f"{yval:.2f}",
            va="bottom",
            ha="center",
            color="black",
            fontsize=10,
        )

    # Add labels and title
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    ax.set_title("Monthly Income and Expenses")

    # Create custom legend handles for differences
    handles = []
    labels = []

    # Handles and labels for Income and Expenses
    handles.append(plt.Line2D([0], [0], color="blue", lw=4))
    handles.append(plt.Line2D([0], [0], color="red", lw=4))
    labels.append("Income")
    labels.append("Expenses")

    # Add custom handles and labels for differences
    for i, month in enumerate(months):
        diff_label = f"{month}: {differences[i]:.2f}"
        handles.append(plt.Line2D([0], [0], color="gray", lw=2))  # Dummy handle
        labels.append(diff_label)

    # Create the legend
    ax.legend(
        handles=handles,
        labels=labels,
        loc="upper right",
        bbox_to_anchor=(1, 1),
        fontsize="small",
        borderaxespad=0.5,
    )

    # Set x-axis ticks
    ax.set_xticks([p + bar_width / 2 for p in positions])
    ax.set_xticklabels(months)  # Set x-tick labels to months

    # Create a canvas for the graph in the new window
    canvas = FigureCanvasTkAgg(
        fig, master=graph_window
    )  # Use graph_window instead of root
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, sticky="nsew")  # Use grid for layout

    # Optional: Configure grid weights for proper resizing
    graph_window.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
    graph_window.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

    # Call tight_layout to adjust subplots and legend
    plt.tight_layout()

    canvas.draw()  # Draw the graph on the canvas
