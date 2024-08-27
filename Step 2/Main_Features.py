from datetime import datetime


# Main Features
# --------------------------------------------- Income Tracker --------------------------------------------- #

# Log sources of Incomes
def getIncomeName() -> str:
    income_input = input("Please enter you weekly income ('12324.23'): ")

    return income_input

def getIncomeType() -> str:
    income_option_input = input("Please enter the type of income (Salary, Freelance, etc...): ")

    return income_option_input

def getIncomeDate():
    income_date_input = input("Please enter date (MM/DD/YYYY) of income (*Leave blank for Today): ")

    if income_date_input == "":
        income_date_input = datetime.now().strftime("%m/%d/%Y")

    return income_date_input

# --------------------------------------------- Expense Tracker --------------------------------------------- #

# Log sources of Expenses
def getExpenseName() -> str:
    expense_input = input("Please enter expense: ")
    
    return expense_input

def getExpenseType() -> str:
    expense_type_input = input("Please enter expense type (Rent, groceries, entertainment, etc...): ")

    return expense_type_input

def getExpenseDate():
    expense_date_input = input("Please enter date of expense (Leave blank for Today): ")

    if expense_date_input == "":
        expense_date_input = datetime.now().strftime("%m/%d/%Y")

    return expense_date_input

# --------------------------------------------- Saving Goals --------------------------------------------- #

# Log Savings Goals
def getSavingsName() -> str:
    savings_input = input("Please enter what you Savings Goal is: ")

    return savings_input

def getSavingsType() -> str:
    savings_type_input = input("Please enter the type of Savings Goal (Vacation, Emergencies, etc...): ")

    return savings_type_input

def getSavingsStartDate():
    savings_start_date_input = input("Please enter start date of Savings Goal (Leave blank for Today): ")

    if savings_start_date_input == "":
        savings_start_date_input = datetime.now().strftime("%m/%d/%Y")

    return savings_start_date_input

def getSavingsEndDate():
    savings_end_date_input = input("Please enter end date of Savings Goal (MM/DD/YYYY): ")

    return savings_end_date_input


# --------------------------------------------- Reporting --------------------------------------------- #

# Create visual report of income vs expenses

# Create Visual report of Category-wise expense break down

# Create visual report of Progress towards savings goal

### Optional Features
# --------------------------------------------- Budgeting --------------------------------------------- #

# Set monthly budget (Maybe for different categories and alerts when exceeding)
def getMonthlyBudget():
    monthly_budget_input = input("Please enter the monthly budget: ")

    return monthly_budget_input

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
