from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def pieGraph(sums: dict, graph_name: str, root: tk.Tk):

    # Data Variable Initialization
    types = []  # Stores Income Type
    type_values = []  # Stores Income Amount

    # Identify categories with less than 5% and group them into 'Other'
    other_value = 0
    other_percentage = 0
    filtered_types = []
    filtered_values = []
    filtered_explode = []

    # Store the results
    for key, total_sum in sums.items():
        types.append(key)
        type_values.append(float(total_sum))

    # Calculate the total income
    total_value = sum(type_values)

    # Calculate the percentage for each income source
    percentages = []
    for value in type_values:
        percentage = (value / total_value) * 100
        percentages.append(percentage)

    # Iterate over each index and percentage in the 'percentages' list
    for i, percentage in enumerate(percentages):
        # Creates 'Other' Income Type
        if percentage < 1:
            other_value += type_values[i]
            other_percentage += percentage
        # Creates Income Type
        else:
            filtered_types.append(types[i])
            filtered_values.append(type_values[i])
            filtered_explode.append(0.05)

    # After the loop, check if there is any accumulated value in 'other_value'
    if other_value > 0:
        filtered_types.append("Other")
        filtered_values.append(other_value)
        filtered_explode.append(0.05)

    # Create a list of formatted labels combining source names and their corresponding percentages
    labels = [
        f"{source} - ${value:,.2f}"  # Use a formatted string to combine each source with its value
        for source, value in zip(
            filtered_types, filtered_values
        )  # Iterate over the pairs of source names and their corresponding values using zip
    ]

    # Create a new Toplevel window for the pie chart
    pie_window = tk.Toplevel(root)
    pie_window.title(graph_name)  # Set title for the pie chart window

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 10))

    # Create a pie chart with customized settings
    ax.pie(
        filtered_values,  # Provide the values for each slice of the pie
        autopct=lambda p: (  # Format the percentage label for each slice
            "{:.2f}%".format(p)
            if p > 0
            else ""  # Only apply this formatting if the percentage is greater than 0
        ),
        explode=filtered_explode,  # Define the explode effect for each slice to highlight certain slices
        labels=labels,  # Add labels next to each slice of the pie
    )

    plt.title(graph_name)

    # Create a canvas for the pie chart in the new window
    canvas = FigureCanvasTkAgg(fig, master=pie_window)  # Use pie_window instead of root
    canvas_widget = canvas.get_tk_widget()

    # Use grid to place the canvas widget
    canvas_widget.grid(
        row=0, column=0, sticky="nsew"
    )  # Place the canvas in row 0, column 0, and expand

    # Optional: Configure grid weights for proper resizing
    pie_window.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
    pie_window.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

    canvas.draw()  # Draw the pie chart on the canvas


def barGraph(
    sums: dict, graph_name: str, x_axis_name: str, y_axis_name: str, root: tk.Tk
):
    types = []
    type_values = []

    # Store the results
    for key, total_sum in sums.items():
        types.append(key)
        type_values.append(float(total_sum))

    # Create a new Toplevel window for the bar chart
    bar_window = tk.Toplevel(root)
    bar_window.title(graph_name)  # Set title for the bar chart window

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 5))  # Set the figure size

    # Create bars with a color
    ax.bar(types, type_values, color="skyblue")

    # Add titles and labels
    ax.set_title(graph_name)  # Set the title
    ax.set_xlabel(x_axis_name)  # Set the x-axis label
    ax.set_ylabel(y_axis_name)  # Set the y-axis label

    # Add value labels on top of bars
    for i, value in enumerate(type_values):
        ax.text(i, value + 0.5, f"{value:.2f}", ha="center", va="bottom")

    # Create a canvas for the bar chart in the new window
    canvas = FigureCanvasTkAgg(fig, master=bar_window)  # Use bar_window instead of root
    canvas_widget = canvas.get_tk_widget()

    # Use grid to place the canvas widget
    canvas_widget.grid(
        row=0, column=0, sticky="nsew"
    )  # Place the canvas in row 0, column 0, and expand

    # Optional: Configure grid weights for proper resizing
    bar_window.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
    bar_window.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

    canvas.draw()  # Draw the bar chart on the canvas
