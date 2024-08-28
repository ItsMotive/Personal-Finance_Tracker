import psycopg2 # type: ignore
from psycopg2 import sql # type: ignore
import pandas as pd
from prettytable import PrettyTable # type: ignore
from Main_Features import (
    getIncomeName, 
    getIncomeDate,
    getIncomeType,
    getIncomeAmount
)

from Credentials import USERNAME, PASSWORD, DATABASE_NAME, HOST, PORT
from Constants import (
    SELECT_INCOME_QUERY, SELECT_EXPENSE_QUERY, SELECT_SAVINGS_QUERY, 
    INCOME_TABLE_NAME, EXPENSE_TABLE_NAME, SAVINGS_TABLE_NAME
)
from Database_Queries import addIncomeQuery, addExpenseQuery, addSavingsQuery
from Main_Features import (
    getIncomeName, getIncomeType, getIncomeAmount, getIncomeDate, 
    getExpenseName, getExpenseType, getExpenseAmount, getExpenseDate,
    getSavingsName, getSavingsType, getSavingsAmount, getSavingsStartDate, getSavingsEndDate
)


def DB_Connection() -> None:
    conn = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
    )

    return conn

# ------------------------------------ Display Tables ------------------------------------ #

def displayIncomeTable() -> None:
    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")
        
        # Execute a query to select data from the table
        cur.execute(SELECT_INCOME_QUERY)

        # Fetch column names
        # Creates a tuple with all the columns in the table
        columns = [desc[0] for desc in cur.description]
        
        # Fetch all rows from the executed query
        rows = cur.fetchall()
        
        # Create a PrettyTable object
        table = PrettyTable()
        table.field_names = columns

        for row in rows:
            table.add_row(row)
        
        # Display the table
        print(table)


    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def displayExpenseTable() -> None:
    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")
        
        # Execute a query to select data from the table
        cur.execute(SELECT_EXPENSE_QUERY)

        # Fetch column names
        # Creates a tuple with all the columns in the table
        columns = [desc[0] for desc in cur.description]
        
        # Fetch all rows from the executed query
        rows = cur.fetchall()
        
        # Create a PrettyTable object
        table = PrettyTable()
        table.field_names = columns

        for row in rows:
            table.add_row(row)
        
        # Display the table
        print(table)


    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def displaySavingsTable() -> None:

    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")
        
        # Execute a query to select data from the table
        cur.execute(SELECT_SAVINGS_QUERY)

        # Fetch column names
        # Creates a tuple with all the columns in the table
        columns = [desc[0] for desc in cur.description]
        
        # Fetch all rows from the executed query
        rows = cur.fetchall()
        
        # Create a PrettyTable object
        table = PrettyTable()
        table.field_names = columns

        for row in rows:
            table.add_row(row)
        
        # Display the table
        print(table)


    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

# ------------------------------------ Table Actions ------------------------------------ #

def addIncome():
    income_name, income_type, income_amount, income_date = getIncomeName(), getIncomeType(), getIncomeAmount(), getIncomeDate()

    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")

        # Execute a query to select data from the table
        cur.execute(addIncomeQuery(income_name, income_type, income_amount, income_date, INCOME_TABLE_NAME))

        conn.commit()

        print("Adding Successful")

    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def addExpense():
    expense_name, expense_type, expense_amount, expense_date = getExpenseName(), getExpenseType(), getExpenseAmount(), getExpenseDate()

    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")

        # Execute a query to select data from the table
        cur.execute(addExpenseQuery(expense_name, expense_type, expense_amount, expense_date, EXPENSE_TABLE_NAME))

        conn.commit()

        print("Adding Successful")

    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def addSavingsGoal():
    savings_name, savings_type, savings_amount, start_date, end_date = getSavingsName(), getSavingsType(), getSavingsAmount(), getSavingsStartDate(), getSavingsEndDate()

    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")

        # Execute a query to select data from the table
        cur.execute(addSavingsQuery(savings_name, savings_type, savings_amount, start_date, end_date, SAVINGS_TABLE_NAME))

        conn.commit()

        print("Adding Successful")

    except Exception as e:
        # Display error message
        print("Error Occurred")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()
