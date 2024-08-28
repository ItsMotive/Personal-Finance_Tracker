# Functions to generate queries

def addIncomeQuery(name: str, source: str, amount: float, date: str, table_name:str):
    query = "INSERT INTO " + table_name + \
        "(\"Name\", \"Source\", \"Amount\", \"Date\") VALUES ('" + \
            name + "', '" + source + "', " + amount + ", '" + date + "')"

    return query

def addExpenseQuery(name: str, source: str, amount: float, date: str, table_name:str):
    query = "INSERT INTO " + table_name + \
        "(\"Name\", \"Source\", \"Amount\", \"Date\") VALUES ('" + \
            name + "', '" + source + "', " + amount + ", '" + date + "')"

    return query

def addSavingsQuery(name: str, source: str, amount: float, start_date: str, end_date:str, table_name:str):
    query = "INSERT INTO " + table_name + \
        "(\"Goal\", \"Goal Type\", \"Goal Amount\", \"Start Date\", \"End Date\", \"Status\") VALUES ('" + \
            name + "', '" + source + "', " + amount + ", '" + start_date + "', '" + end_date + "', 'Active')"

    return query