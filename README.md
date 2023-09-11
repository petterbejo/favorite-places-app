# A simple map app for favorite places

This app is a simple way to mark your favorite places and display them on a map along with a description. 

The app is made with Flask, folium, and a SQL database. It is currently in development. The plan is to dockerize the whole thing. 

## How to use

### The database

You can store your favorite places with the following attributes:

1. Name
2. Description
3. Category (can be fireplace, hike, scenic spot/general point of interest, museum, parking area)
4. Link to the place
5. Distance to nearest road/place that is accesible by car
6. Rating (1-3)
7. Visited (boolean - set to true for already visited places, false if it's on your wish list)
8. Country code (e.g. 'F' or 'DK')
9. Region within the country
10. Location (using decimal degrees)

## Development plan

This development plan is actually more of a to do-list. I'm planning to do thing more or less in the order described here:

1. View single marker on map
2. Create endpoint to add new markers one by one
3. Create endpoint to upload a CSV with multiple markers
4. Switch to postgres
5. Dockerize and deploy to start using it
6. Make it possible to add photos
7. Make it possible to add tracks (e.g. in GPX format) instead of single points only (maybe even with an export function)
