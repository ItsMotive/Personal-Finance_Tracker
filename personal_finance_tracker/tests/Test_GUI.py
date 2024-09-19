import sys
import os

# Add the parent directory of Step_2 to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.visualization.graph import (
    grabIncomeTableData, grabExpenseTableData, grabSavingTableData,
    incomeTableGUI, expenseTableGUI, savingsTableGUI,
    incomeInputDataGUI
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

def testIncomeInputGUI():
    incomeInputDataGUI()

def testOverallGUI():
 pass