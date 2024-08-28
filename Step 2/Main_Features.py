from datetime import datetime


# Main Features
# --------------------------------------------- Income Tracker --------------------------------------------- #

# Log sources of Incomes
def getIncomeName() -> str:
    return input("Please enter Income name: ")

def getIncomeType() -> str:
    return input("Please enter the type of Income (Salary, Freelance, etc...): ")

def getIncomeAmount() -> float:
    return str(round(float(input("Please enter the Income amount (24421.45): ")), 2))

def getIncomeDate() -> str:
    income_date_input = input("Please enter date (MM/DD/YYYY) of Income (*Leave blank for Today): ")

    if income_date_input == "":
        income_date_input = datetime.now().strftime("%m/%d/%Y")

    return income_date_input

# --------------------------------------------- Expense Tracker --------------------------------------------- #

# Log sources of Expenses
def getExpenseName() -> str:
    return input("Please enter Expense name: ")

def getExpenseType() -> str:
    return input("Please enter Expense type (Rent, groceries, entertainment, etc...): ")

def getExpenseAmount() -> float:
    return str(round(float(input("Please enter the Expense amount (24421.45): ")), 2))

def getExpenseDate() -> str:
    expense_date_input = input("Please enter date (MM/DD/YYYY) of Expense (Leave blank for Today): ")

    if expense_date_input == "":
        expense_date_input = datetime.now().strftime("%m/%d/%Y")

    return expense_date_input

# --------------------------------------------- Saving Goals --------------------------------------------- #

# Log Savings Goals
def getSavingsName() -> str:
    return input("Please enter what you Savings Goal is: ")

def getSavingsType() -> str:
    return input("Please enter the type of Savings Goal (Vacation, Emergencies, etc...): ")

def getSavingsAmount() -> float:
    return str(round(float(input("Please enter the Savings Goal amount (24421.45): ")), 2))

def getSavingsStartDate():
    savings_start_date_input = input("Please enter start date of Savings Goal (Leave blank for Today): ")

    if savings_start_date_input == "":
        savings_start_date_input = datetime.now().strftime("%m/%d/%Y")

    return savings_start_date_input

def getSavingsEndDate():
    return input("Please enter end date of Savings Goal (MM/DD/YYYY): ")


# --------------------------------------------- Reporting --------------------------------------------- #

# Create visual report of income vs expenses

# Create Visual report of Category-wise expense break down

# Create visual report of Progress towards savings goal

### Optional Features
# --------------------------------------------- Budgeting --------------------------------------------- #

# Set monthly budget (Maybe for different categories and alerts when exceeding)
def getMonthlyBudget():
    return input("Please enter the monthly budget: ")

def getBudgetType():
    monthly_budget_type_input = input("Please enter the category for the budget (Leave blank if overall budget): ")
    
    if monthly_budget_type_input == "":
        return "Overall"
    
    return monthly_budget_type_input

# --------------------------------------------- Recurring Transactions --------------------------------------------- #

def getRecurringTransactions():
    if expense_date == expense_date + 7:

        if expense_name == expense_name:

            pass
            # Then log recurring payments somewhere
