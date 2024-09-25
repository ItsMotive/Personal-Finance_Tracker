from datetime import datetime
from src.database.SQL_Queries import SELECT_INCOME_QUERY
from src.database.db_operations import grabAllDatabaseData
from src.visualization.graphs_util import barGraph, pieGraph


def getIncomeData() -> list:
    return grabAllDatabaseData(SELECT_INCOME_QUERY)


def incomePieGraph():

    # Get Income Data
    data = getIncomeData()

    # Dictionary to store the sums
    sums = {}

    for array in data:

        # Getting Income Type
        key = array[1]

        # Getting the Income Amount
        value = array[2]

        # Check if the key is already in the dictionary
        if key in sums:

            # If the Income Type is present, add the Income Amount
            sums[key] += value

        else:

            # Else, create an initial value for Income Type
            sums[key] = value

    pieGraph(sums, "Income Pie Graph")


def incomeBarGraph():

    # Get Income Data
    data = getIncomeData()

    # Dictionary to store the sums
    sums = {}

    # Get the current year
    current_year = datetime.now().strftime("%Y")

    for array in data:

        # Getting Income Date and format it to 'YYYY-MM'
        key = array[3].strftime("%Y-%m")

        # Getting the Income Amount
        value = array[2]

        # Check if the key is from the current year
        if key.startswith(current_year):
            # Check if the key is already in the dictionary
            if key in sums:
                # If the Income Type is present, add the Income Amount
                sums[key] += value
            else:
                # Else, create an initial value for Income Type
                sums[key] = value

    # Convert the dictionary items to a list and sort by date
    sorted_items = sorted(
        sums.items(), key=lambda item: datetime.strptime(item[0], "%Y-%m")
    )

    # Convert the sorted list of tuples back into a dictionary
    sums = dict(sorted_items)

    # Call the function to generate the bar graph
    barGraph(
        sums,
        f"Income Bar Graph for {current_year}",
        "Income Month",
        "Income Totals",
    )
