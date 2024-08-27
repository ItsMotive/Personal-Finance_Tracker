import psycopg2
from psycopg2 import sql
import pandas as pd
from prettytable import PrettyTable

from Credentials import USERNAME, PASSWORD, DATABASE_NAME, HOST, PORT
from Constants import SELECT_INCOME_QUERY, SELECT_EXPENSE_QUERY, SELECT_SAVINGS_QUERY


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
    
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute a query to select data from the table
        cursor.execute(SELECT_INCOME_QUERY)

        # Fetch column names
        # Creates a tuple with all the columns in the table
        columns = [desc[0] for desc in cursor.description]
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
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
    
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute a query to select data from the table
        cursor.execute(SELECT_EXPENSE_QUERY)

        # Fetch column names
        # Creates a tuple with all the columns in the table
        columns = [desc[0] for desc in cursor.description]
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
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
    
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute a query to select data from the table
        cursor.execute(SELECT_SAVINGS_QUERY)

        # Fetch column names
        # Creates a tuple with all the columns in the table
        columns = [desc[0] for desc in cursor.description]
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
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


def addIncome():
    pass

def addExpense():
    pass

def addSavingsGoal():
    pass
