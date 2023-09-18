"""
Make a test database.
"""
import sqlite3

db_path = 'test.db'

conn = sqlite3.connect(db_path)

create_markers_table = """ CREATE TABLE IF NOT EXISTS markers (
                                    id INTEGER PRIMARY KEY,
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
                                ); """

create_categories_table = """ CREATE TABLE IF NOT EXISTS categories (
                                    id INTEGER PRIMARY KEY,
                                    category TEXT NOT NULL
                                ); """

cur = conn.cursor()
cur.execute(create_markers_table)
cur.execute(create_categories_table)

markers = [
    (1, 'test1', 'nice place', 'fireplace', 'example.com', 50, 2, 1, 'dk',
     'sj',
     55.73931038034454, 12.24586002073197),
    (2, 'test2', 'great hike', 'hike', 'example.com', 0, 3, 1, 'dk', ' sj',
     55.703214, 12.485766),
    (3, 'test3', 'long hike', 'hike', 'example.com', 100, 2, 1, 'dk',  'sj',
     56.73931038034454, 12.24586002073197),
    ]

categories =[
    (1, 'Fireplace'),
    (2, 'Hike'),
    (3, 'Nice spot'),
    (5, 'Museum'),
    (6, 'Parking area'),
    (7, 'Other'),
]

cur.executemany('INSERT INTO markers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
              markers)
cur.executemany('INSERT INTO categories VALUES(?, ?);',
              categories)

conn.commit()
conn.close()