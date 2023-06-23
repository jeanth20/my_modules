import psycopg2
import random
import string

class PostgresDB:
    def init(self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None


def connect(self):
    try:
        self.conn = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        print("Connected to PostgreSQL database: " + self.db_name)
    except psycopg2.Error as e:
        print(e)

def disconnect(self):
    if self.conn:
        self.conn.close()

def get_all_data(self, table_name):
    cursor = self.conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

def get_row(self, table_name, row_id):
    cursor = self.conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE id=%s", (row_id,))
    row = cursor.fetchone()
    return row

def get_single_value(self, table_name, column_name, row_id):
    cursor = self.conn.cursor()
    cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE id=%s", (row_id,))
    value = cursor.fetchone()[0]
    return value

def create_random_data(self, table_name, num_entries):
    cursor = self.conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            name TEXT,
            age INTEGER,
            email TEXT
        )
    """)

    for _ in range(num_entries):
        name = ''.join(random.choices(string.ascii_letters, k=8))
        age = random.randint(18, 50)
        email = ''.join(random.choices(string.ascii_lowercase, k=5)) + '@example.com'
        cursor.execute(f"INSERT INTO {table_name} (name, age, email) VALUES (%s, %s, %s)", (name, age, email))

    self.conn.commit()



# database_name = "University"
# user = "your_username"
# password = "your_password"
# host = "localhost"
# port = "5432"
# table_name = "students"
# num_entries = 10

# db = PostgresDB(database_name, user, password, host, port)
# db.connect()
# db.create_random_data(table_name, num_entries)

# all_data = db.get_all_data(table_name)
# print("All data:")
# for row in all_data:
# print(row)

# row_id = 1
# row_data = db.get_row(table_name, row_id)
# print(f"Row with ID {row_id}:")
# print(row_data)

# column_name = "name"
# value = db.get_single_value(table_name, column_name, row_id)
# print(f"Value of column '{column_name}' for row with ID {row_id}:")
# print(value)