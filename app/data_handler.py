"""
The DataHandler class that interacts with the database and the flask app.
"""
import sqlite3

db_path = '../db/test.db'

class DataHandler():
    def __init__(self, db_path):
        self.db_path = db_path

    def get_db_connection(self):
        """Open a connection to the database."""
        return sqlite3.connect(self.db_path)

    def get_all_markers(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM markers')
        rows = cur.fetchall()
        cur.close()
        conn.cursor()
        return rows

    def get_single_marker(self, id):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM markers WHERE id={id}')
        row = cur.fetchone()
        cur.close()
        conn.cursor()
        return row

