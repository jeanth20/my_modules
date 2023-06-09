import sqlite3
import pprint


class MySQLite:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def execute_query_with_results(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_query(query)

    def insert_into_table(self, table_name, values):
        query = f"INSERT INTO {table_name} VALUES ({values})"
        self.execute_query(query)

    def select_from_table(self, table_name, columns="*"):
        query = f"SELECT {columns} FROM {table_name}"
        return self.execute_query_with_results(query)

    def delete_from_table(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query)

    def update_table(self, table_name, set_values, condition):
        query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
        self.execute_query(query)

    def get_all_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        result = self.execute_query_with_results(query)
        return [row[0] for row in result]

    def pretty_print_result(self, result):
        pprint.pprint(result)


# Example usage
db_file = "example.db"
db = MySQLite(db_file)

# Create a table
db.create_table("users", "id INTEGER PRIMARY KEY, name TEXT, age INTEGER")

# Insert data into the table
db.insert_into_table("users", "1, 'John Doe', 25")
db.insert_into_table("users", "2, 'Jane Smith', 30")

# Select all rows from the table
result = db.select_from_table("users")
db.pretty_print_result(result)

# Delete a row from the table
db.delete_from_table("users", "id = 2")

# Update a row in the table
db.update_table("users", "age = 26", "id = 1")

# Get all tables in the database
tables = db.get_all_tables()
print(tables)

# Other function calls...
