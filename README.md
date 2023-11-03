# A simple map app for favorite places

This app is a simple way to mark your favorite places and display them on a map along with a description. 

The app is made with Flask, folium, and a SQL database. It is currently in development. The plan is to dockerize the whole thing. 

Note that the database tables are created the first time the site is loaded since the setup script is part of the DataHandler class. In this way, you can simply spin up the app with the `docker-compose.yaml` file. This will pull the image from my repo and the PostgreSQL repo on Docker Hub. Three environment variables should be set beforehand: PGDB for the database, PDPWD for the database password, and PGUSR for the database user (I will maybe change this to Docker Secrets at some point). I've decided to make the setup script part of the DataHandler class because it allows for simpler packaging of the app since all you need is one file, `docker-compose.yaml`.

## How to use

### The database

You can store your favorite places with the following attributes:

1. Name
2. Description
3. Category (can be fireplace, hike, scenic spot/general point of interest, museum, parking area, other)
4. Link to the place
5. Distance to nearest road/place that is accesible by car
6. Rating (1-3)
7. Visited (boolean - set to true for already visited places, false if it's on your wish list)
8. Country code (e.g. 'F' or 'DK')
9. Region within the country
10. Location (using decimal degrees)

## Development plan

This development plan is actually more of a to do-list. I'm planning to do thing more or less in the order described here:

1. Deploy to start using it
3. Make confirmation page when inserting new marker
3. Create endpoint to upload a CSV with multiple markers
6. Make it possible to add more than one link
6. Make it possible to add photos
5. Handle data inserting errors in a way that makes it clear to the user what the error is, and without having to retype/reinsert the correct data
7. Make it possible to add tracks (e.g. in GPX format) instead of single points only (maybe even with an export function)
8. Make it possible to filter the list view
