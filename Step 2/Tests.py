from Database import displayIncomeTable, displayExpenseTable, displaySavingsTable
from Main_Features import (
        getIncomeDate, 
        getIncomeType,
        getIncomeName,
        getExpenseDate,
        getExpenseName,
        getExpenseType,
        getSavingsName,
        getSavingsType,
        getSavingsStartDate,
        getSavingsEndDate
)

# Test Display of Tables
def testIncomeTableDisplay():
    print("\nIncome Table: \n")
    displayIncomeTable()

def testExpenseTableDisplay():
    print("\nExpense Table: \n")
    displayExpenseTable()

def testSavingsTableDisplay():
    print("\nSavings Table: \n")
    displaySavingsTable()

# Income Functions
def testIncomeDateBlank():
    print("Date = ''\n")
    print(getIncomeDate() + "\n")

def testIncomeType():
    print(getIncomeType() + "\n")

def testIncomeName():
    print(getIncomeName() + "\n")

# Expense Functions
def testExpenseDateBlank():
    print("Date = ''\n")
    print(getExpenseDate() + "\n")

def testExpenseType():
    print(getExpenseType() + "\n")

def testExpenseName():
    print(getExpenseName() + "\n")

# Savings Functions
def testSavingsName():
    print(getSavingsName() + "\n")

def testSavingsType():
    print(getSavingsType() + "\n")

def testSavingsStartDate():
    print(getSavingsStartDate() + "\n")

def testSavingsEndDate():
    print(getSavingsEndDate() + "\n")

