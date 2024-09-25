import psycopg2
import tkinter as tk
from src.Credentials import USERNAME, PASSWORD, DATABASE_NAME, HOST, PORT
from src.database.SQL_Queries import (
    addExpenseQuery,
    addIncomeQuery,
    addSavingsGoalQuery,
    addSavingsQuery,
    updateExpenseQuery,
    updateIncomeQuery,
    updateSavingsGoalQuery,
)


def DB_Connection() -> None:

    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    return conn, cursor


# --------------------------- Grab Table Data Functions --------------------------- #


def grabAllDatabaseData(query: str) -> list:

    conn, cur = DB_Connection()

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


# --------------------------- Add to Table Functions --------------------------- #


def addToDatabaseGUI(query: callable, params: tuple) -> None:

    conn, cur = DB_Connection()

    try:
        print("Connection successful!")

        # Execute the query with the provided parameters
        cur.execute(query(), params)

        conn.commit()

        print("Adding Successful")

    except Exception as e:

        # Display error message
        print(f"Error Occurred: {e}")

    finally:

        # Close the cursor and connection
        cur.close()
        conn.close()


def addIncomeCallback(name: str, source: str, amount: float, date: str) -> None:
    addToDatabaseGUI(addIncomeQuery, (name, source, amount, date))


def addExpenseCallback(name: str, source: str, amount: float, date: str) -> None:
    addToDatabaseGUI(addExpenseQuery, (name, source, amount, date))


def addSavingsGoalCallback(
    name: str, source: str, amount: float, start_date: str, end_date: str
) -> None:
    addToDatabaseGUI(addSavingsGoalQuery, (name, source, amount, start_date, end_date))


def addSavingsCallback(name: str, amount: float, date: str):
    addToDatabaseGUI(addSavingsQuery, (name, amount, date))


# --------------------------- Update Table Functions --------------------------- #


def update_db_cell(query: callable, params: tuple, update_column) -> bool:
    try:
        # Establish database connection
        conn, cursor = DB_Connection()

        # Execute the SQL query
        cursor.execute(query(update_column), params)

        # Commit changes if the query was successful
        conn.commit()
        return True  # Success

    except psycopg2.Error as e:
        print(f"Failed to update the database: {e}")
        return False  # Failure

    finally:
        # Close the connection
        cursor.close()
        conn.close()


def updateIncomeCallback(
    update_column: str,
    new_value: str,
    name_value: str,
    amount_value: str,
    date_value: str,
) -> bool:
    return update_db_cell(
        updateIncomeQuery,
        (new_value, name_value, amount_value, date_value),
        update_column,
    )


def updateExpenseCallback(
    update_column: str,
    new_value: str,
    name_value: str,
    amount_value: str,
    date_value: str,
) -> bool:
    return update_db_cell(
        updateExpenseQuery,
        (new_value, name_value, amount_value, date_value),
        update_column,
    )


def updateSavingsGoalCallback(
    update_column: str,
    new_value: str,
    name_value: str,
    type_value: str,
    amount_value: str,
    start_date_value: str,
    end_date_value: str,
    status_value: str,
) -> bool:
    return update_db_cell(
        updateSavingsGoalQuery,
        (
            new_value,
            name_value,
            type_value,
            amount_value,
            start_date_value,
            end_date_value,
            status_value,
        ),
        update_column,
    )
