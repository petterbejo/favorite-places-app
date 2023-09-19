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

    def _format_location(self, location):
        """Checks that the location is formatted in decimal degrees.

        For the  precision (see
        https://en.wikipedia.org/wiki/Decimal_degrees#Precision), at
        least one decimal place (e.g. 55.7, 12.4) is required."""
        location_split = location.split(',')
        latitude = location_split[0].replace(' ', '')
        longitude = location_split[1].replace(' ', '')
        return latitude, longitude


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
        try:
            latitude, longitude = self._format_location(
                insert_dict['location'])
            data_insert_str = (f"""INSERT INTO markers (name, description, """
                       f"""category, link, access_distance, rating, visited, """
                       f"""country_code, region, DD_latitude, DD_longitude) """
                       f"""VALUES ('{insert_dict["name"]}', """
                       f"""'{insert_dict["description"]}', """ 
                       f"""'{insert_dict["category"]}', """
                       f"""'{insert_dict["link"]}', """
                       f"""'{insert_dict["access_distance"]}', """
                       f"""'{insert_dict["rating"]}', '{insert_dict["visited"]}', """
                       f"""'{insert_dict["country_code"]}', """
                       f"""'{insert_dict["region"]}', """
                       f"""'{latitude}', """
                       f"""'{longitude}' )""")
            print(data_insert_str)
            conn = self._get_db_connection()
            cur = conn.cursor()
            cur.execute(data_insert_str)
            conn.commit()
            conn.close()
        except Exception:
            raise Exception('Something went wrong. Probably some of your data '
                            'was not formatted correctly.')

