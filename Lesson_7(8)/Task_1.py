import sqlite3


class MyConMan:

    def __init__(self, DB_name):
        self.DB_name = DB_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.DB_name)
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

