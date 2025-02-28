import mysql.connector
import json
import os

def create_and_add_to_sql(host, user, password, database_name, table_name, data):
    """Creates/connects to a database, creates a table, and inserts data."""
    try:
        # Connect to MySQL (create database if needed)
        mydb = mysql.connector.connect(host=host, user=user, password=password)
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        mydb.commit()

        # Connect to the specific database
        mydb = mysql.connector.connect(
            host=host, user=user, password=password, database=database_name
        )
        mycursor = mydb.cursor()

        # Create table if it doesn't exist
        mycursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                Expression VARCHAR(255),
                Definition TEXT
            )
        """)
        mydb.commit()

        # Insert data
        sql = f"INSERT INTO {table_name} (Expression, Definition) VALUES (%s, %s)"
        mycursor.executemany(sql, data)
        mydb.commit()

        print(f"Inserted {len(data)} rows successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = ""
    database_name = "dictionary"
    table_name = "dictionary_table"  # Changed to "dictionary_table"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_dir, "data.json")

    with open(data_file_path, 'r') as f:
        dict_data = json.load(f)

    data = []
    for key, value in dict_data.items():
        if isinstance(value, list):
            value = ", ".join(map(str, value))
        data.append((key, value))

    chunk_size = 100
    for i in range(0, len(data), chunk_size):
        chunk = data[i : i + chunk_size]
        create_and_add_to_sql(host, user, password, database_name, table_name, chunk)