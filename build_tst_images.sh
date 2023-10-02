docker rm -f favorite-places-app-app-1 
docker image rmi -f favorite-places-app-app
docker-compose -f docker-compose.dev.yaml up -d
