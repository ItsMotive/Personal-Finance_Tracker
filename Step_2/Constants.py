# ------------ Variables ------------ #

INCOME_TABLE_NAME = "public.\"income_table\""
EXPENSE_TABLE_NAME = "public.\"expense_table\""
SAVINGS_TABLE_NAME = "public.\"savings_goals_table\""
SAVINGS_ENTRIES_TABLE_NAME = "public.\"savings_table\""

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