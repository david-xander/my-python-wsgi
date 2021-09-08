# The main goal of this project is to build a custom WSGI for python
The WSGI will be behind an nginx and will use a very super simple framework to check the WSGI behaviour. 

It is actually a Docker based project for now. The idea is to be able to focus only in the WSGI.


## In order to build the image
docker-compose build

## To run the image
docker-compose up -d

## To run and build the image
docker-compose up -d --build

## To stop the image
docker-compose down -v

## To check if something goes wrong
docker-compose logs -f
