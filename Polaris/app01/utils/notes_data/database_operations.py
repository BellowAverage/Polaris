
import mysql.connector
import pandas as pd
import random
import string

def connect_to_mysql():
    # Establish a connection to the MySQL server
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="polaris"
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database:", error)
        return None

def execute_query_and_return_result(connection, query):
    # Execute the SQL query and return the result
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            if query.strip().lower().startswith('select'):
                results = cursor.fetchall()
                return results  # Return the fetched rows for SELECT queries
            else:
                connection.commit()
                return cursor.rowcount  # Return the number of rows affected for other queries
    except mysql.connector.Error as error:
        print("Failed to execute query:", error)
        return None


def polaris_db(query):
    connection = connect_to_mysql()
    if connection:
        return execute_query_and_return_result(connection, query)
    else:
        return "database connection failed"

# print(polaris_db('''CREATE TABLE notes (
#     nid INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255),
#     content TEXT,
#     location VARCHAR(255),
#     time DATETIME
# );'''))

# print(polaris_db("ALTER TABLE notes ADD uid INT;"))

# data = pd.read_csv(r'Polaris\app01\utils\user_list.csv')

# for each in data['User']:
#     password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#     print(polaris_db(f"INSERT INTO users (user_name, password) VALUES ('{each}', '{password}');"))

# print(polaris_db("ALTER TABLE notes MODIFY COLUMN time VARCHAR(255);"))

# print(polaris_db("SELECT title, content FROM notes WHERE uid='9';"))

print(polaris_db("select * from users limit 10;"))