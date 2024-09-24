from matplotlib import pyplot as plt


def pieGraph(sums: dict, graph_name: str):

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

    # Create a matplotlib figure
    plt.figure(figsize=(11, 10))

    # Create a pie chart with customized settings
    plt.pie(
        filtered_values,  # Provide the values for each slice of the pie
        autopct=lambda p: (  # Format the percentage label for each slice
            "{:.2f}%".format(
                p
            )  # Format the percentage value to two decimal places followed by a '%' sign
            if p > 0  # Only apply this formatting if the percentage is greater than 0
            else ""
        ),  # Otherwise, return an empty string to leave the label blank
        explode=filtered_explode,  # Define the explode effect for each slice to highlight certain slices
        labels=labels,  # Add labels next to each slice of the pie
    )

    plt.title(graph_name)
    plt.show()


def barGraph(sums: dict, graph_name: str, x_axis_name: str, y_axis_name: str):
    types = []
    type_values = []

    # Store the results
    for key, total_sum in sums.items():
        types.append(key)
        type_values.append(float(total_sum))
        # print(f"{key}: {total_sum}")

    # Create bars with a color
    plt.bar(types, type_values, color="skyblue")

    # Add titles and labels
    plt.title(graph_name)  # Set the title
    plt.xlabel(x_axis_name)  # Set the x-axis label
    plt.ylabel(y_axis_name)  # Set the y-axis label

    # Add value labels on top of bars
    for i, value in enumerate(type_values):
        plt.text(i, value + 0.5, f"{value:.2f}", ha="center", va="bottom")

    # Show the plot
    plt.tight_layout()  # Adjust layout to fit labels
    plt.show()  # Display the graph
