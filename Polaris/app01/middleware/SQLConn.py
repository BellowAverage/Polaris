import mysql.connector

def connect_to_mysql(schema):
    # Establish a connection to the MySQL server
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=schema,
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


def polaris_db(query, schema="po"):
    connection = connect_to_mysql(schema=schema)
    if connection:
        return execute_query_and_return_result(connection, query)
    else:
        return "database connection failed"

# connection = connect_to_mysql()
# if connection:
#     query = "SELECT * FROM users LIMIT 10;"
#     results = execute_query_and_return_result(connection, query)
#     if results is not None:
#         for row in results:
#             print(row)
#     connection.close()