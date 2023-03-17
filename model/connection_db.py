import sqlite3 as sql

class ConnectionDB:
    def __init__(self):
        self.data_base = 'database/data.db'
        self.connection = sql.connect(self.data_base)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.commit()
        self.connection.close()