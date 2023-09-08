"""
Make a test database.
"""
import sqlite3

db_path = 'test.db'

conn = sqlite3.connect(db_path)

create_tables = """ CREATE TABLE IF NOT EXISTS markers (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    DD_latitude REAL,
                                    DD_longitude REAL
                                ); """

c = conn.cursor()
c.execute(create_tables)

records = [(1, 'test1', 55.73931038034454, 12.24586002073197),
           (2, 'test2', 55.703214, 12.485766)]
c.executemany('INSERT INTO markers VALUES(?, ?, ?, ?);', records)

conn.commit()
conn.close()