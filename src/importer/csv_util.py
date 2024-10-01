def getIncomeData(row) -> list:
    data = (row["Name"], row["Type"], float(row["Amount"]), row["Date"])
    return data


def getExpenseData(row) -> list:
    data = (row["Name"], row["Type"], float(row["Amount"]), row["Date"])
    return data


def getSavingGoalData(row) -> list:
    data = (
        row["Name"],
        row["Type"],
        float(row["Amount"]),
        row["Start_Date"],
        row["End_Date"],
        row["Status"],
    )
    return data


def getSavingsData(row) -> list:
    data = (row["Name"], float(row["Amount"]), row["Date"])
    return data
