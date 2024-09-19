import psycopg2
import tkinter as tk
from src.Credentials import USERNAME, PASSWORD, DATABASE_NAME, HOST, PORT
from src.gui.GUIs import createInputWindow
from src.database.SQL_Queries import EXPENSE_TABLE_NAME, INCOME_TABLE_NAME, SAVINGS_TABLE_NAME, addExpenseQuery, addIncomeQuery, addSavingsQuery

def DB_Connection() -> None:
    conn = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
    )

    return conn

# Grab All Data from table
def grabAllDatabaseData(query: str) -> list:

    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")
        
        # Execute a query to select data from the table
        cur.execute(query)

        # Fetch all rows from the executed query
        rows = cur.fetchall()

    except Exception as e:

        # Display error message
        print("Error Occurred")

    finally:

        # Close the cursor and connection
        cur.close()
        conn.close()

        return rows

# Add to Table
def addToDatabaseGUI(query: callable, params: tuple, table_name: str):

    # Establish a connection to the PostgreSQL database
    conn = DB_Connection()

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    try:
        print("Connection successful!")

        # Execute the query with the provided parameters
        cur.execute(query(*params, table_name))

        conn.commit()

        print("Adding Successful")

    except Exception as e:

        # Display error message
        print(f"Error Occurred: {e}")

    finally:

        # Close the cursor and connection
        cur.close()
        conn.close()

def addIncomeCallback(name: str, source: str, amount: float, date: str):
    addToDatabaseGUI(addIncomeQuery, (name, source, amount, date), INCOME_TABLE_NAME)

def addExpenseCallback(name: str, source: str, amount: float, date: str):
    addToDatabaseGUI(addExpenseQuery, (name, source, amount, date), EXPENSE_TABLE_NAME)

def addSavingsCallback(name: str, source: str, amount: float, start_date: str, end_date: str):
    addToDatabaseGUI(addSavingsQuery, (name, source, amount, start_date, end_date), SAVINGS_TABLE_NAME)

def inputDataToTable(root: tk.Tk, label: list, gui_title: str, func: callable) -> None:
    entries = [tk.StringVar() for _ in label]
    createInputWindow(root, gui_title, label, entries, func)