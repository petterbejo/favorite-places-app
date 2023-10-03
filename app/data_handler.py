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
        if not self._database_exists():
            self._setup_database()

    def _database_exists(self):
        try:
            rows = self.get_all_markers()
            if rows:
                return True
        except Exception:
            return False

    def _setup_database(self):
        conn = self._get_db_connection()
        cur = conn.cursor()

        create_markers_table = \
                """CREATE TABLE IF NOT EXISTS markers (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                category INTEGER NOT NULL,
                link TEXT,
                access_distance INTEGER,
                rating INTEGER,
                visited INTEGER,
                country_code TEXT NOT NULL,
                region TEXT,
                DD_latitude REAL NOT NULL,
                DD_longitude REAL NOT NULL
                );"""
        cur.execute(create_markers_table)

        create_categories_table = \
                """CREATE TABLE IF NOT EXISTS categories (
                id SERIAL PRIMARY KEY,
                category TEXT NOT NULL
                );"""
        cur.execute(create_categories_table)

        conn.commit()
        cur.close()
        conn.close()


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
        conn.close()
        return rows

    def get_all_markers(self):
        conn = self._get_db_connection()
        cur = conn.cursor()
        query = """
                    SELECT
                        markers.id,
                        markers.name,
                        markers.description,
                        categories.category,
                        markers.link,
                        markers.access_distance,
                        markers.rating,
                        markers.visited,
                        markers.country_code,
                        markers.region,
                        markers.DD_latitude,
                        markers.DD_longitude
                    FROM
                        markers
                    INNER JOIN
                        categories
                    ON
                        markers.category = categories.id
                    ORDER BY markers.country_code, markers.region;
                """
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_single_marker(self, id):
        conn = self._get_db_connection()
        cur = conn.cursor()
        query = """SELECT
                        markers.id,
                        markers.name,
                        markers.description,
                        categories.category,
                        markers.link,
                        markers.access_distance,
                        markers.rating,
                        markers.visited,
                        markers.country_code,
                        markers.region,
                        markers.DD_latitude,
                        markers.DD_longitude
                    FROM
                        markers 
                    INNER JOIN
                        categories
                    ON
                        markers.category = categories.id
                    WHERE markers.id = %s;
                """
        cur.execute(query, (id, ))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def insert_new_single_marker(self, insert_dict):
        try:
            latitude, longitude = self._format_location(
                insert_dict['location'])
            data_insert_str = """INSERT INTO markers """ \
                        """(name, description, category, link, """ \
                        """access_distance, rating, visited, """ \
                        """country_code, region, """ \
                        """DD_latitude, DD_longitude) """ \
                        """VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            conn = self._get_db_connection()
            cur = conn.cursor()
            cur.execute(data_insert_str,
                        [insert_dict["name"], insert_dict["description"],
                         insert_dict["category"], insert_dict["link"],
                         insert_dict["access_distance"], insert_dict["rating"],
                         insert_dict["visited"], insert_dict["country_code"],
                         insert_dict["region"], latitude, longitude]
                        )
            conn.commit()
            conn.close()
        except Exception:
            raise Exception('Something went wrong. Probably some of your data '
                            'was not formatted correctly.')

