import sqlite3

class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.database_name)

    def disconnect(self):
        self.conn.close()

    def create_table(self, table_name, columns):
        cursor = self.conn.cursor()
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        cursor.execute(query)
        self.conn.commit()

    def get_last_inserted_id(self, table_name):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE ID = (SELECT MAX(ID) FROM {table_name})"
        # query = f"SELECT LAST_INSERT_ROWID() FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        last_id = result[0] if result is not None else None
        return last_id

    def retrieve_table_contents(self, table_name):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def retrieve_row_by_id(self, table_name, row_id):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE id = ?"
        cursor.execute(query, (row_id,))
        row = cursor.fetchone()
        return row

    def retrieve_value_by_id(self, table_name, row_id, column_name):
        cursor = self.conn.cursor()
        query = f"SELECT {column_name} FROM {table_name} WHERE id = ?"
        cursor.execute(query, (row_id,))
        value = cursor.fetchone()
        return value[0] if value is not None else None

    def insert_row(self, table_name, values):
        cursor = self.conn.cursor()
        placeholders = ", ".join(["?" for _ in values])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(query, values)
        self.conn.commit()

    def insert_rows(self, table_name, rows):
        cursor = self.conn.cursor()
        placeholders = ", ".join(["?" for _ in rows[0]])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.executemany(query, rows)
        self.conn.commit()

    # def update_row(self, table_name, row_id, values):
    #     cursor = self.conn.cursor()
    #     set_values = ", ".join([f"{column} = ?" for column in values])
    #     f"UPDATE {table_name} SET column1 = value1, column2 = value2, WHERE condition;" 
    #     query = f"UPDATE {table_name} SET {set_values} WHERE id = ?"
    #     cursor.execute(query, (*values, row_id))
    #     self.conn.commit()

    def update_row(self, table_name, row_id, values):
        cursor = self.conn.cursor()
        set_values = ", ".join([f"{column} = ?" for column in values])
        query = f"UPDATE {table_name} SET {set_values} WHERE id = ?"
        query_values = tuple(values.values()) + (row_id,)
        cursor.execute(query, query_values)
        self.conn.commit()


    def delete_row(self, table_name, row_id):
        cursor = self.conn.cursor()
        query = f"DELETE FROM {table_name} WHERE id = ?"
        cursor.execute(query, (row_id,))
        self.conn.commit()


# use case 
if __name__ == "__main__":
    database_name = "test.db"
    db = Database(database_name)
    db.connect()

    # Create table
    table_name = "simple_table"
    
    columns = [
        "id INTEGER",        
        "name TEXT NOT NULL",
        "age INTEGER",
    ]
    db.create_table(table_name, columns)

    # Insert row
    values = [1, "John", 25]
    db.insert_row(table_name, values)

    # Insert multiple rows at once
    rows = [
        [2, "Jane", 30],
        [3, "Mark", 35],
        [4, "Emily", 28]
    ]
    db.insert_rows(table_name, rows)

    # Update a row
    row_id = 1
    new_values = {"name": "John Doe", "age": 30}
    db.update_row(table_name, row_id, new_values)

    # Delete a row
    row_id = 2
    db.delete_row(table_name, row_id)

    db.disconnect()
