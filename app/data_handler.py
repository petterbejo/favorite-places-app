"""
The DataHandler class that interacts with the database and the flask app.
"""
import os

import psycopg2

class DataHandler():
    def __init__(self):
        self.conn_str = f'host={"db"} port=5432 '\
                        f'dbname={os.environ.get("POSTGRES_DB")} '\
                        f'user={os.environ.get("POSTGRES_USER")} '\
                        f'password={os.environ.get("POSTGRES_PASSWORD")}'

    def _get_db_connection(self):
        """Open a connection to the database."""
        return psycopg2.connect(self.conn_str)

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
        query = """SELECT * FROM markers"""
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.cursor()
        return rows

    def get_single_marker(self, id):
        conn = self._get_db_connection()
        cur = conn.cursor()
        query = """SELECT * FROM markers WHERE id = %s"""
        cur.execute(query, (id, ))
        row = cur.fetchone()
        cur.close()
        conn.cursor()
        return row

    def insert_new_single_marker(self, insert_dict):
        try:
            latitude, longitude = self._format_location(
                insert_dict['location'])
            data_insert_str = \
                (f"""INSERT INTO markers """
                     f"""(name, description, category, link, """
                     f"""access_distance, rating, visited, """
                     f"""country_code, region, DD_latitude, DD_longitude) """
                 f"""VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                [insert_dict["name"], insert_dict["description"],
                 insert_dict["category"], insert_dict["link"],
                 insert_dict["access_distance"], insert_dict["rating"],
                 insert_dict["visited"],insert_dict["country_code"],
                 insert_dict["region"],latitude, longitude]
                 )
            print(data_insert_str)
            conn = self._get_db_connection()
            cur = conn.cursor()
            cur.execute(data_insert_str)
            conn.commit()
            conn.close()
        except Exception:
            raise Exception('Something went wrong. Probably some of your data '
                            'was not formatted correctly.')

