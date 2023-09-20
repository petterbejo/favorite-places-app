-- Create the markers table
CREATE TABLE IF NOT EXISTS markers (
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
);

-- Create the categories table
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    category TEXT NOT NULL
);


