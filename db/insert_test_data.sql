INSERT INTO markers (name, description, category, link, access_distance, rating, visited, country_code, region, DD_latitude, DD_longitude)
VALUES
    ('test1', 'nice place', 1, 'example.com', 50, 2, 1, 'dk', 'sj', 55.73931038034454, 12.24586002073197),
    ('test2', 'great hike', 2, 'example.com', 0, 3, 1, 'dk', 'sj', 55.703214, 12.485766),
    ('test3', 'long hike', 2, 'example.com', 100, 2, 1, 'dk', 'sj', 56.73931038034454, 12.24586002073197);

-- Insert data into the categories table
INSERT INTO categories (category)
VALUES
    ('Fireplace'),
    ('Hike'),
    ('Nice spot'),
    ('Museum'),
    ('Parking area'),
    ('Other');
