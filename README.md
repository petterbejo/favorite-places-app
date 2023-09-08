# A simple map app for favorite places

This app is a simple way to mark your favorite places and display them on a map along with a description. 

The app is made with Flask, folium, and a SQL database. It is currently in development. The plan is to dockerize the whole thing. 

## How to use

### The database

You can store your favorite places with the following attributes:

1. Name
2. Description
3. Category (can be fireplace, hike, scenic spot/general point of interest, museum, parking area)
4. Distance to nearest road/place that is accesible by car
5. Rating (1-3)
6. Visited (boolean - set to true for already visited places, false if it's on your wish list)
7. Location (using decimal degrees)


