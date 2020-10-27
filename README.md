# lawrence-api
Python REST API for books catalog

Make sure Docker is installed.

To run application in container: in root directory type:
docker-compose up -d --build

If you want to run test display list of running containers:
docker ps
Then take your CONTAINER ID
docker exec -it CONTAINER_ID sh

To run tests and falke8 type:
python manage.py & flake8
