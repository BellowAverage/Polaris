import pandas as pd
from database_operations import polaris_db

def read_csv_file(file_path):
    # Read the CSV file into a DataFrame
    return pd.read_csv(file_path)

def generate_insert_query(table_name, row):
    # Generate an SQL INSERT statement for a single row of a DataFrame
    columns = ', '.join(row.index)
    values = ', '.join([f"'{str(item).replace("'", "''")}'" for item in row])
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"

def insert_csv_to_database(file_path, table_name):
    df = read_csv_file(file_path)
    for _, row in df.iterrows():
        query = generate_insert_query(table_name, row)
        result = polaris_db(query)
        if not result:
            print(f"Failed to insert row: {row}")
        else:
            print(f"Successfully inserted row: {row}")

# Example usage
csv_file_path = 'Polaris\\app01\\utils\\preprocessed_diary_info_obt.csv'
table_name = 'notes'
insert_csv_to_database(csv_file_path, table_name)
