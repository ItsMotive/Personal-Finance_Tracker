from GUI_Table_Setup import (
    grabIncomeTableData, grabExpenseTableData, grabSavingTableData,
    incomeTableGUI, expenseTableGUI, savingsTableGUI
)

# Grabbing Data Test
def testIncomeDataGrab():
    print(grabIncomeTableData())

# Displaying Income Table Test
def testIncomeTableDisplayGUI():
    incomeTableGUI()

# Grabbing Data Test
def testExpenseDataGrab():
    print(grabExpenseTableData())

# Displaying Income Table Test
def testExpenseTableDisplayGUI():
    expenseTableGUI()

# Grabbing Data Test
def testSavingsDataGrab():
    print(grabSavingTableData())

# Displaying Income Table Test
def testSavingsTableDisplayGUI():
    savingsTableGUI()

testExpenseTableDisplayGUI()
testSavingsTableDisplayGUI()