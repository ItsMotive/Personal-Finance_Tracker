# ------------ Table Names ------------ #

INCOME_TABLE_NAME = "public.\"income_table\""
EXPENSE_TABLE_NAME = "public.\"expense_table\""
SAVINGS_GOALS_TABLE_NAME = "public.\"savings_goals_table\""
SAVINGS_TABLE_NAME = "public.\"savings_table\""

# ------------ SQL Queries ------------ #

SELECT_INCOME_QUERY = f"SELECT * FROM {INCOME_TABLE_NAME};"

SELECT_EXPENSE_QUERY = f"SELECT * FROM {EXPENSE_TABLE_NAME};"

SELECT_SAVINGS_QUERY = f"SELECT * FROM {SAVINGS_GOALS_TABLE_NAME};"

SELECT_SAVINGS_ENTRIES_QUERY = f"SELECT * FROM {SAVINGS_TABLE_NAME};"

# ------------ SQL Query Functions ------------ #

def addIncomeQuery():
    query = f'INSERT INTO {INCOME_TABLE_NAME} (\"name\", \"source\", \"amount\", \"date\") VALUES (%s, %s, %s, %s);'
    return query

def addExpenseQuery():
    query = f'INSERT INTO {EXPENSE_TABLE_NAME} (\"name\", \"source\", \"amount\", \"date\") VALUES (%s, %s, %s, %s);'
    return query

def addSavingsGoalQuery():
    query = f"INSERT INTO {SAVINGS_GOALS_TABLE_NAME} (\"goal\", \"goal_type\", \"goal_amount\", \"start_date\", \"end_date\", \"status\") VALUES (%s, %s, %s, %s, %s, 'Active');"
    return query

def updateIncomeQuery(update_column: str):
    query = f"UPDATE {INCOME_TABLE_NAME} SET {update_column} = %s WHERE name = %s AND amount = %s AND date = %s;"
    return query

def updateExpenseQuery(update_column: str):
    query = f"UPDATE {EXPENSE_TABLE_NAME} SET {update_column} = %s WHERE name = %s AND amount = %s AND date = %s;"
    return query

def updateSavingsGoalQuery(update_column: str):
    query = f"UPDATE {SAVINGS_GOALS_TABLE_NAME} SET {update_column} = %s WHERE goal = %s AND goal_type = %s AND goal_amount = %s AND start_date = %s AND end_date = %s AND status = %s;"
    return query