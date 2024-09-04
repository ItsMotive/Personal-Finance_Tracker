import psycopg2
from psycopg2 import sql

import sys
import os

# Add the parent directory of Step_2 to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Step_2.Credentials import DATABASE_NAME, USERNAME, PASSWORD, HOST, PORT

# Database connection details
DB_NAME = DATABASE_NAME
DB_USER = USERNAME
DB_PASSWORD = PASSWORD
DB_HOST = HOST 
DB_PORT = PORT

def initialSetup():
    try: 
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        return connection
    except Exception as error:
        print(f"Error occurred: {error}")

def createIncomeTable(connection):

    try: 

        # Create a cursor object
        cursor = connection.cursor()

        # SQL command to create a table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS income_table (
            name TEXT NOT NULL,
            source TEXT NOT NULL,
            amount NUMERIC(10, 2) NOT NULL DEFAULT 0.00,
            date DATE NOT NULL
        );
        '''
        # Execute the SQL command
        cursor.execute(create_table_query)
        connection.commit()

        print("Table created successfully.")

    except Exception as error:
        print(f"Error occurred: {error}")

    finally:
        # Close the cursor and connection to the database
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def createExpenseTable(connection):

    try: 

        # Create a cursor object
        cursor = connection.cursor()

        # SQL command to create a table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS expense_table (
            name TEXT NOT NULL,
            source TEXT NOT NULL,
            amount NUMERIC(10, 2) NOT NULL DEFAULT 0.00,
            date DATE NOT NULL
        );
        '''
        # Execute the SQL command
        cursor.execute(create_table_query)
        connection.commit()

        print("Table created successfully.")

    except Exception as error:
        print(f"Error occurred: {error}")

    finally:
        # Close the cursor and connection to the database
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def createSavingsTable(connection):

    try: 

        # Create a cursor object
        cursor = connection.cursor()

        # SQL command to create a table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS savings_goals_table (
            goal TEXT NOT NULL,
            goal_type TEXT NOT NULL,
            goal_amount NUMERIC(10, 2) NOT NULL DEFAULT 0.00,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            status TEXT NOT NULL
        );
        '''
        # Execute the SQL command
        cursor.execute(create_table_query)
        connection.commit()

        print("Table created successfully.")

    except Exception as error:
        print(f"Error occurred: {error}")

    finally:
        # Close the cursor and connection to the database
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def createSavingsEntriesTable(connection):

    try: 

        # Create a cursor object
        cursor = connection.cursor()

        # SQL command to create a table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS savings_table (
            savings_goal TEXT NOT NULL,
            savings_amount NUMERIC(10, 2) NOT NULL DEFAULT 0.00,
            date DATE NOT NULL
        );
        '''

        # Execute the SQL command
        cursor.execute(create_table_query)
        connection.commit()

        print("Table created successfully.")

    except Exception as error:
        print(f"Error occurred: {error}")

    finally:
        # Close the cursor and connection to the database
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# --------------------------- Table Creation --------------------------- #

createIncomeTable(initialSetup())
createExpenseTable(initialSetup())
createSavingsTable(initialSetup())
createSavingsEntriesTable(initialSetup())