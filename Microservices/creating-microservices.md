# Creating Microservices

The few basic steps that we follow while deciding to create an app with the microservices architecture are:

1. Divide all the services into singular components and assign the modular apps to different teams. If only one team is working on the apps one at a time, start off with the app that forms the core of the entire application.
1. Initialise the app using the traditional steps dictated by the framework that powers the microservice. For example, the `django-admin createproject` command that initialises a Django app.
1. Create a Dockerfile that describes the containerization of the microservices.
1. Write the docker-compose file for building the services and make the necessary connections of the app with the Docker container.