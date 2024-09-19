# ------------ Table Names ------------ #

INCOME_TABLE_NAME = "public.\"income_table\""
EXPENSE_TABLE_NAME = "public.\"expense_table\""
SAVINGS_TABLE_NAME = "public.\"savings_goals_table\""
SAVINGS_ENTRIES_TABLE_NAME = "public.\"savings_table\""

# ------------ SQL Queries ------------ #

SELECT_INCOME_QUERY = f"SELECT * FROM {INCOME_TABLE_NAME};"

SELECT_EXPENSE_QUERY = f"SELECT * FROM {EXPENSE_TABLE_NAME};"

SELECT_SAVINGS_QUERY = f"SELECT * FROM {SAVINGS_TABLE_NAME};"

SELECT_SAVINGS_ENTRIES_QUERY = f"SELECT * FROM {SAVINGS_ENTRIES_TABLE_NAME};"

# ------------ SQL Query Functions ------------ #

def addIncomeQuery(name: str, source: str, amount: float, date: str, table_name: str):
    query = f"INSERT INTO {table_name} (\"name\", \"source\", \"amount\", \"date\") VALUES ('{name}', '{source}', {amount}, '{date}')"
    return query

def addExpenseQuery(name: str, source: str, amount: float, date: str, table_name: str):
    query = f"INSERT INTO {table_name} (\"name\", \"source\", \"amount\", \"date\") VALUES ('{name}', '{source}', {amount}, '{date}')"
    return query

def addSavingsQuery(name: str, source: str, amount: float, start_date: str, end_date: str, table_name: str):
    query = f"INSERT INTO {table_name} (\"goal\", \"goal_type\", \"goal_amount\", \"start_date\", \"end_date\", \"status\") VALUES ('{name}', '{source}', {amount}, '{start_date}', '{end_date}', 'Active')"
    return query

