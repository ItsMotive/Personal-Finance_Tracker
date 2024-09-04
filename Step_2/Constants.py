# ------------ Variables ------------ #

INCOME_TABLE_NAME = "public.\"Test_Income_Table\""
EXPENSE_TABLE_NAME = "public.\"Test_Expenses_Table\""
SAVINGS_TABLE_NAME = "public.\"Test_Savings_Goals_Table\""
SAVINGS_ENTRIES_TABLE_NAME = "public.\"Test_Savings_Goals_Table\""

# ------------ SQL Queries ------------ #

SELECT_INCOME_QUERY = """SELECT * 
    FROM 
    """ + INCOME_TABLE_NAME + ";"

SELECT_EXPENSE_QUERY = """SELECT * 
    FROM 
    """ + EXPENSE_TABLE_NAME + ";"

SELECT_SAVINGS_QUERY = """SELECT * 
    FROM 
    """ + SAVINGS_TABLE_NAME + ";"

SELECT_SAVINGS_ENTRIES_QUERY = """SELECT * 
    FROM 
    """ + SAVINGS_ENTRIES_TABLE_NAME + ";"