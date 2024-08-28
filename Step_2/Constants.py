# ------------ Variables ------------ #

INCOME_TABLE_NAME = "public.\"Test_Income_Table\""
EXPENSE_TABLE_NAME = "public.\"Test_Expenses_Table\""
SAVINGS_TABLE_NAME = "public.\"Test_Savings_Goals_Table\""

SELECT_INCOME_QUERY = """SELECT * 
    FROM 
    """ + INCOME_TABLE_NAME + ";"

SELECT_EXPENSE_QUERY = """SELECT * 
    FROM 
    """ + EXPENSE_TABLE_NAME + ";"

SELECT_SAVINGS_QUERY = """SELECT * 
    FROM 
    """ + SAVINGS_TABLE_NAME + ";"

