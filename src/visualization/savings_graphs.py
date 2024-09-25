from collections import defaultdict
from decimal import Decimal
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from src.database.SQL_Queries import (
    SELECT_INACTIVE_SAVINGS_GOAL_QUERY,
    SELECT_SAVINGS_ENTRIES_QUERY,
)
from src.database.db_operations import grabAllDatabaseData
from src.utils import flatTuple


def savingsDataPrep(raw_data: list, exclude_inactive: list) -> dict:
    savings_data = defaultdict(dict)
    all_months = set()
    exclude_list = flatTuple(exclude_inactive)

    # Collect data and track all months across categories
    for category, amount, date in raw_data:

        if category in exclude_list:
            continue

        month = date.strftime("%Y-%m")  # Convert date to "YYYY-MM" format
        all_months.add(month)

        if month in savings_data[category]:
            savings_data[category][month] += amount  # Sum amounts if same month
        else:
            savings_data[category][month] = amount

    # Ensure each category has data for all months
    for category in savings_data:
        for month in all_months:
            if month not in savings_data[category]:
                savings_data[category][month] = Decimal("0.00")

    return savings_data


def getCumulativeSavings(data: list):
    cumulative = {}
    total = 0
    for month, amount in sorted(data.items()):
        total += amount
        cumulative[month] = total
    return cumulative


def formatMonth(month_str: str) -> datetime.date:
    """Convert 'YYYY-MM' format to 'Month YYYY'."""
    year, month = map(int, month_str.split("-"))
    return datetime.date(year, month, 1).strftime("%B %Y")  # Format as 'Month YYYY'


def generateSavingsReport(root: tk.Tk) -> None:

    # Create a new Toplevel window for the graph
    graph_window = tk.Toplevel(root)
    graph_window.title("Savings Report")  # Set title for the new window

    savings_data = savingsDataPrep(
        grabAllDatabaseData(SELECT_SAVINGS_ENTRIES_QUERY),
        grabAllDatabaseData(SELECT_INACTIVE_SAVINGS_GOAL_QUERY),
    )

    fig, ax = plt.subplots(figsize=(8, 5))  # Adjusting figure size

    months = sorted(next(iter(savings_data.values())).keys())  # Sorted list of months
    for label, data in savings_data.items():
        cumulative = getCumulativeSavings(data)
        ax.plot(months, list(cumulative.values()), marker="o", label=label)

        for month, value in cumulative.items():
            ax.text(month, value + 2, str(value), fontsize=10, ha="center", va="bottom")

    # Format the month labels
    formatted_months = [formatMonth(month) for month in months]

    max_value = max(
        max(cumulative.values())
        for cumulative in map(getCumulativeSavings, savings_data.values())
    )
    ax.set_ylim(0, max_value + 25)

    ax.set_xticks(
        months
    )  # Set x-ticks to the original month format for correct alignment
    ax.set_xticklabels(
        formatted_months
    )  # Set the labels to the formatted month strings
    ax.set_xlabel("Months")
    ax.set_ylabel("Cumulative Savings")
    ax.set_title("Cumulative Savings Over Months")
    ax.legend()

    # Create a canvas for the graph in the new window
    canvas = FigureCanvasTkAgg(
        fig, master=graph_window
    )  # Use graph_window instead of root
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)  # Use pack here

    canvas.draw()
