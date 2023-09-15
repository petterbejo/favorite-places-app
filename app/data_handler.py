"""
The DataHandler class that interacts with the database and the flask app.
"""
import sqlite3

db_path = '../db/test.db'

class DataHandler():
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_db_connection(self):
        """Open a connection to the database."""
        return sqlite3.connect(self.db_path)

    def get_all_categories(self):
        conn = self._get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM categories')
        rows = cur.fetchall()
        cur.close()
        conn.cursor()
        return rows


    def get_all_markers(self):
        conn = self._get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM markers')
        rows = cur.fetchall()
        cur.close()
        conn.cursor()
        return rows

    def get_single_marker(self, id):
        conn = self._get_db_connection()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM markers WHERE id={id}')
        row = cur.fetchone()
        cur.close()
        conn.cursor()
        return row

    def insert_new_single_marker(self, insert_dict):
        print(insert_dict)
        # check that data is correct
    '''
    data_insert_str = (f"INSERT INTO markers (name, description, "
                       f"category, link, access_distance, rating, visited, "
                       f"country_code, region, DD_latitude, DD_longitude) "
                       f"VALUES ({request.form['name']}, "
                       f"{request.form['description']}," f" "
                       f"{request.form['category']},"
                       f" {request.form['link']}, "
                       f"{request.form['access_distance']},"
                       f" {request.form['rating']}, {request.form['visited']},"
                       f" {request.form['country_code']},"
                       f" {request.form['region']},"
                       f" {request.form['']}, )")
    f" {request.form['name']}, )")
    print(data_insert_str)
'''
