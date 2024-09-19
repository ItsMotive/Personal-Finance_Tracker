from src.Constants import INCOME_TABLE_NAME, SAVINGS_TABLE_NAME, EXPENSE_TABLE_NAME
from src.database.Database import (
    displayIncomeTable, displayExpenseTable, displaySavingsTable, 
    addIncome, addExpense, addSavingsGoal
)
from src.Main_Features import (
        getIncomeDate, getIncomeType, getIncomeName, getIncomeAmount, 
        getExpenseDate, getExpenseName, getExpenseAmount, getExpenseType,
        getSavingsName, getSavingsType, getSavingsAmount, getSavingsStartDate, getSavingsEndDate
)

from src.database.Database_Queries import addIncomeQuery, addExpenseQuery, addSavingsQuery

# ------------------------ Test Display of Tables ------------------------ #
def testIncomeTableDisplay():
    print("\nIncome Table: \n")
    displayIncomeTable()

def testExpenseTableDisplay():
    print("\nExpense Table: \n")
    displayExpenseTable()

def testSavingsTableDisplay():
    print("\nSavings Table: \n")
    displaySavingsTable()

# ------------------------ Income Functions ------------------------ #
def testIncomeDateBlank():
    print("Date = ''\n")
    print(getIncomeDate() + "\n")

def testIncomeType():
    print(getIncomeType() + "\n")

def testIncomeName():
    print(getIncomeName() + "\n")

def testIncomeAmount():
    print(getIncomeAmount())

def testAddingIncomeToTable():
    print("\nBefore Table:")
    displayIncomeTable()

    addIncome()

    print("\nAfter Table:")
    displayIncomeTable()

# ------------------------ Expense Functions ------------------------ #
def testExpenseDateBlank():
    print("Date = ''\n")
    print(getExpenseDate() + "\n")

def testExpenseType():
    print(getExpenseType() + "\n")

def testExpenseName():
    print(getExpenseName() + "\n")

def testIncomeAmount():
    print(getExpenseAmount())

def testAddingExpenseToTable():
    print("\nBefore Table:")
    displayExpenseTable()

    addExpense()

    print("\nAfter Table:")
    displayExpenseTable()

# ------------------------ Savings Functions ------------------------ #
def testSavingsName():
    print(getSavingsName() + "\n")

def testSavingsType():
    print(getSavingsType() + "\n")

def testSavingsAmount():
    print(getSavingsAmount() + "\n")

def testSavingsStartDate():
    print(getSavingsStartDate() + "\n")

def testSavingsEndDate():
    print(getSavingsEndDate() + "\n")

def testAddingSavingsToTable():
    print("\nBefore Table:")
    displaySavingsTable()

    addSavingsGoal()

    print("\nAfter Table:")
    displaySavingsTable()

# ------------------------ Database Query Functions ------------------------ #
def testAddIncomeQueryReturn():
    print(addIncomeQuery(getIncomeName(), getIncomeType(), getIncomeAmount(), getIncomeDate(), INCOME_TABLE_NAME))

def testAddIncomeQueryReturnManual():
    query = addIncomeQuery("Hello", "Source", "123.45", '12/12/1212', INCOME_TABLE_NAME)

    print(query)

def testAddSavingsQueryReturn():
    print(addSavingsQuery(getSavingsName(), getSavingsType(), getSavingsAmount(), getSavingsStartDate(), getSavingsEndDate(), SAVINGS_TABLE_NAME))

# ------------------------ Execution of Test ------------------------ #

testIncomeTableDisplay()